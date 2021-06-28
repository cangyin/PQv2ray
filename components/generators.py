from .utils import *
from .node import Node, NodeComplexityType
from .config import g_config
from .mytrie import common_prefixes

from random import choices
from string import ascii_lowercase

logger = logging.getLogger(__name__)


# these are JSON objects that should be loaded at runtime

groups = {}
connections = {}
qv2ray_conf = {}

default_group_id = '000000000000'

inbound_http_template = {}
inbound_socks_template = {}

outbound_direct_tag = 'direct'
outbound_proxy_tag = 'proxy'
outbound_block_tag = 'block'
outbound_classified_tags = (outbound_direct_tag, outbound_proxy_tag, outbound_block_tag)

# special nodes
block_node = Node(id='0'*12, name=outbound_block_tag)
direct_node = Node(id='1'*12, name=outbound_direct_tag)


def load():
    clear_cache()
    folder = g_config['qv2ray']['config_folder']
    groups.update( load_json(folder + '/groups.json') )
    connections.update( load_json(folder + '/connections.json') )
    qv2ray_conf.update( load_json(folder + '/Qv2ray.conf') )
    inbound_http_template.update( load_json(g_config["v2ray_object_templates"]["inbound_http"]) )
    inbound_socks_template.update( load_json(g_config["v2ray_object_templates"]["inbound_socks"]) )
    block_node.profile_path = g_config["v2ray_object_templates"]["outbound_block"]
    direct_node.profile_path = g_config["v2ray_object_templates"]["outbound_direct"]
    logger.info('loaded.')


def get_display_name(connection_id):
    return connections[connection_id].get('displayName', '')


def get_connection_id(group_id, display_name):
    connection_ids = groups[group_id].get('connections', [])
    for connection_id in connection_ids:
        if connections[connection_id]['displayName'] == display_name:
            return connection_id
    return None


def get_group_id(group_name :str):
    for group_id in groups:
        if groups[group_id]['displayName'].lower() == group_name.lower():
            return group_id
    return None


def get_nodes_in_group(group_id :str):
    connection_ids = groups[group_id].get('connections', [])
    nodes = []
    for connection_id in connection_ids:
        nodes.append(Node(
            id=connection_id,
            name=get_display_name(connection_id),
            group=groups[group_id]['displayName'],
            group_id=group_id
        ))
    return nodes


def get_random_node_id():
    return ''.join( choices(ascii_lowercase, k=12) )


def generate_qv2ray_multi_port_config(
        nodes :List[Node],
        ports :List[int],
        inbound_template :dict,
        route_rules=[],
        block_rules=[],
    ):
    inbound_tag_format = g_config['multi_port']['inbound_tag_format']
    outbound_tag_format = g_config['multi_port']['outbound_tag_format']
    rule_tag_format = g_config['multi_port']['rule_tag_format']
    
    # fix duplicate tag error
    _inbound_tags = []
    _outbound_tags = []
    for port, node in zip(ports, nodes):
        d = get_repr_mapping(node, port=port)
        _inbound_tags.append( format_repr(inbound_tag_format, d) )
        _outbound_tags.append( format_repr(outbound_tag_format, d) )

    if len(deduplicate(_inbound_tags)) < len(_inbound_tags):
        inbound_tag_format += ' ({node.id})'
    if len(deduplicate(_outbound_tags)) < len(_outbound_tags):
        outbound_tag_format += ' ({node.id})'

    # generate inbounds, outbounds, route rules
    inbounds = []
    outbounds = []
    rules = []

    balancers= []
    subject_selector = []

    rule_common = {
        "QV2RAY_RULE_ENABLED": True,
        "QV2RAY_RULE_TAG": "",
        "type": "field",
    }
    for port, node in zip(ports, nodes):
        d = get_repr_mapping(node, port=port)
        inboundTag = format_repr(inbound_tag_format, d)
        outboundTag = None
        balancerTag = None

        if node.complexity_type == NodeComplexityType.Simple:
            outboundTag = format_repr(outbound_tag_format, d)
        elif node.complexity_type == NodeComplexityType.Balancer:
            balancerTag = '_' + get_random_node_id()[0:4] # random suffix to avoid duplicated tag
        else:
            logger.warn(f'unable to handle {node}, ignored.')
            continue # leaves an unused port.
        
        # inbound
        inbound = deepcopy(inbound_template)
        inbound.update({
            'port': port,
            'tag': inboundTag
        })
        inbounds.append(inbound)

        # outbound (or outbounds in complex node)
        if outboundTag:
            outbounds.append({
                'QV2RAY_OUTBOUND_METADATA': {
                    'connectionId': node.id,
                    'displayName': outboundTag,
                    "metaType": 1
                }
            })
        elif balancerTag:
            # gather all outbounds and the (first) balancer object
            balancer_outbounds = node.profile['outbounds']
            # filter out block or direct outbound
            balancer_outbounds = [o for o in balancer_outbounds if o.get('protocol') not in ('blackhole', 'freedom')]
            outbounds.extend(balancer_outbounds)
            balancer = deepcopy(node.profile['routing']['balancers'][0])
            balancerTag = balancer['tag'] + balancerTag
            balancer['tag'] =  balancerTag
            balancers.append(balancer)
            if balancer['strategy']['type'] == 'leastPing':
                subject_selector.extend(balancer['selector'])
        
        # rule
        rule = deepcopy(rule_common)
        rule.update({
            'QV2RAY_RULE_TAG': format_repr(rule_tag_format, d),
            'inboundTag': [inboundTag],
        })
        if outboundTag:
            rule['outboundTag'] = outboundTag
        elif balancerTag:
            rule["balancerTag"] = balancerTag
            
        domains = route_rules.get('domains', [])
        ips = route_rules.get('ips', [])
        if domains or ips:
            if domains:
                rule_domain = deepcopy(rule)
                rule_domain.update({'domain': domains})
                if ips: # deduplicate
                    rule_domain['QV2RAY_RULE_TAG'] = format_repr(rule_tag_format, d) + ' (domain)'
                rules.append(rule_domain)
            if ips:
                rule_ip = deepcopy(rule)
                rule_ip.update({'ip': ips})
                if rule_domain: # deduplicate
                    rule_ip['QV2RAY_RULE_TAG'] = format_repr(rule_tag_format, d) + ' (ip)'
                rules.append(rule_ip)
        else:
            rules.append(rule)

    # block rule
    if block_rules.get('domains') or block_rules.get('ips'):
        rule = deepcopy(rule_common)
        rule.update({'outboundTag': outbound_block_tag})

        if block_rules.get('domains'):
            rule_domain = deepcopy(rule)
            rule_domain.update({
                'QV2RAY_RULE_TAG': 'block-domain',
                'domain': block_rules['domains']
            })
            rules.insert(0, rule_domain) # block rule be the first rule
        if block_rules.get('ips'):
            rule_ip = deepcopy(rule)
            rule_ip.update({
                'QV2RAY_RULE_TAG': 'block-ip',
                'ip': block_rules['ips']
            })
            rules.insert(0, rule_ip)
        outbounds.append(block_node.profile)

    # TODO what if the outbound is not a reference ? 
    outbounds = deduplicate(outbounds, key=lambda d: d.get('QV2RAY_OUTBOUND_METADATA', {}).get('connectionId', get_random_node_id()))

    result = {
        "PQV2RAY_META": {
            "type": "multi-port"
        },
        'inbounds': inbounds,
        'outbounds': outbounds,
        'routing': {
            'domainStrategy': g_config['v2ray']['domainStrategy'],
            'domainMatcher': g_config['v2ray']['domainMatcher'],
            'balancers': balancers,
            'rules': rules,
        }
    }
    if subject_selector:
        result.update({
            "observatory": {
                "subjectSelector": deduplicate(subject_selector)
            }})
    return result


def generate_qv2ray_balancer_config(
        nodes :List[Node],
        listenIp,
        ports :dict,
        route_settings={},    
        route_type_order=outbound_classified_tags,
        bypassCN=True,
        bypassLAN=True,
        balancerTag='balancer'
    ):
    '''
        ports = {
            'http': 1081,
            'socks': 1080,
        }
    '''
    assert(len(route_type_order) == 3)
    
    outbound_tag_format = g_config['balancer']['outbound_tag_format']

    # fix duplicate tag error
    _outbound_tags = []
    for node in nodes:
        d = get_repr_mapping(node)
        _outbound_tags.append( format_repr(outbound_tag_format, d) )

    if len(deduplicate(_outbound_tags)) < len(_outbound_tags):
        outbound_tag_format += ' ({node.id})'

    ## inbounds
    inbounds = []
    inbound_tags = [] # for later use
    for porttype, template in (('http', inbound_http_template), ('socks', inbound_socks_template)):
        if ports.get(porttype):
            inbound = deepcopy(template)
            inbound['listen'] = listenIp
            inbound['port'] = ports[porttype]
            inbound_tags.append(inbound['tag'])
            inbounds.append(inbound)

    ## outbounds, balancer selector
    outbounds = []
    selector = []

    for node in nodes:
        outbound_tag = format_repr(outbound_tag_format, get_repr_mapping(node))
        outbounds.append({
            "QV2RAY_OUTBOUND_METADATA": {
                'connectionId': node.id,
                'displayName': outbound_tag,
                "metaType": 1
            }
        })
        selector.append(outbound_tag)

    # common prefixes of tags in selector
    if g_config['v2ray']['selector_use_prefixes']:
        selector = common_prefixes(selector)

    ## route rules
    rules = []
    rule_common = {
        "QV2RAY_RULE_ENABLED": True,
        "QV2RAY_RULE_TAG": "",
        "type": "field",
        "inboundTag": inbound_tags,
    }
    empty = True
    for route_type in route_type_order:
        for domain_or_ip in ('ip', 'domain'):
            domains_or_ips = route_settings.get(domain_or_ip + 's', {}).get(route_type, [])
            if not domains_or_ips:
                continue

            rule = deepcopy(rule_common)
            rule.update({
                "QV2RAY_RULE_TAG": f"{route_type}-{domain_or_ip}",
                domain_or_ip: domains_or_ips
            })
            if route_type == outbound_proxy_tag:
                rule["balancerTag"] = balancerTag
            else:
                rule["outboundTag"] = route_type
            rules.append(rule)
            empty = False
    if empty:
        rule = deepcopy(rule_common)
        rule.update({
            "balancerTag": balancerTag,
            "QV2RAY_RULE_TAG": 'rule',
        })
        rules.append(rule)

    ## 'bypass' rules
    if bypassCN:
        # find starting index of 'direct' rules 
        index_direct = 0
        for index_direct, rule in enumerate(rules):
            if rule.get('outboundTag', '') == outbound_direct_tag:
                break
        rules_bypassCN = load_json(g_config["v2ray_object_templates"]['rules_bypassCN'])
        rules_bypassCN = format_json_obj(rules_bypassCN, globals())
        rules = rules[0:index_direct] + rules_bypassCN + rules[index_direct:]

    if bypassLAN:
        rules_bypassLAN = load_json(g_config["v2ray_object_templates"]['rules_bypassLAN'])
        rules_bypassLAN = format_json_obj(rules_bypassLAN, globals())
        rules = rules_bypassLAN + rules

    # we need to supply the special outbounds
    if route_settings.get('ips', {}).get('block') or route_settings.get('domains', {}).get('block'):
        outbounds.append(block_node.profile)
    if bypassCN or bypassLAN or route_settings.get('ips', {}).get('direct') or route_settings.get('domains', {}).get('direct'):
        outbounds.append(direct_node.profile)

    result = {
        "PQV2RAY_META": {
            "type": "balancer"
        },
        'inbounds': inbounds,
        'outbounds': outbounds,
        'routing': {
            'domainStrategy': route_settings.get('domainStrategy') or g_config['v2ray']['domainStrategy'],
            'domainMatcher': g_config['v2ray']['domainMatcher'],
            'balancers': [{
                'selector': selector,
                'tag': balancerTag,
                "strategy": {
                    "type": g_config['v2ray']['balancer_strategy']
                }
            }],
            'rules': rules,
        }
    }
    if g_config['v2ray']['balancer_strategy'] == 'leastPing': # ( v2ray 4.38.0+ )
        result.update({
            "observatory": {
                "subjectSelector": selector
            }})
    return result



if __name__ == '__main__':
    pass
