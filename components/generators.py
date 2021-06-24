from components.mytrie import common_prefixes
import json
from copy import deepcopy
from .utils import *
from .node import Node

from random import choices
from string import ascii_lowercase

# these are JSON objects that should be loaded at runtime

groups = {}
connections = {}

default_group_id = '000000000000'

qv2ray_multi_port_template = {}
qv2ray_balancer_template = {}

inbound_http_template = {}
inbound_socks_template = {}

outbound_block_template = {}
outbound_direct_template = {}

switchyomega_template = {}

outbound_direct_tag = 'direct'
outbound_proxy_tag = 'proxy'
outbound_block_tag = 'block'

# special nodes
block_node = Node(id='0'*12, name=outbound_block_tag)
direct_node = Node(id='1'*12, name=outbound_direct_tag)


def get_display_name(connection_id):
    return connections[connection_id]['displayName']


def get_connection_id(group_id, display_name):
    connection_ids = groups[group_id]['connections']
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
    connection_ids = groups[group_id]['connections']
    nodes = []
    for connection_id in connection_ids:
        nodes.append(Node(
            id=connection_id,
            name=get_display_name(connection_id),
            group=groups[group_id]['displayName'],
            group_id=group_id
        ))
    return nodes


def get_connection_names_in_group(group_name):
    group_id = get_group_id(group_name)
    connection_ids = groups[group_id]['connections']
    return [get_display_name(connection_id) for connection_id in connection_ids]


def get_random_node_id():
    return ''.join( choices(ascii_lowercase, k=12) )


def generate_qv2ray_multi_port_config(
        nodes :List[Node],
        ports :List[int],
        inbound_template :dict,
        route_rules=[],
        block_rules=[],
        formats={}
    ):
    formats = deepcopy(formats)

    # inbounds
    inbound_template = inbound_template # qv2ray_multi_port_template['inbounds'][0]
    # outbounds
    outbound_template = qv2ray_multi_port_template['outbounds'][0]
    # rules
    rule_template = qv2ray_multi_port_template['routing']['rules'][0]
    # result
    result = deepcopy(qv2ray_multi_port_template)
    result.update({
        'inbounds': [],
        'outbounds': [],
    })
    result['routing']['rules'] = []
    
    # fix duplicate tag error
    _inbound_tags_d = {}
    _outbound_tags_d = {}
    index = 0
    for index, node in enumerate(nodes):
        port = ports[index]
        d = get_repr_mapping(node, port=port)
        _inbound_tags_d[ format_repr(formats['inbound_tag_format'], d) ] = ''
        _outbound_tags_d[ format_repr(formats['outbound_tag_format'], d) ] = ''

    if (index + 1) > len(_inbound_tags_d):
        formats['inbound_tag_format'] += ' ({node.id})'
    if (index + 1) > len(_outbound_tags_d):
        formats['outbound_tag_format'] += ' ({node.id})'

    # generate inbounds, outbounds, route rules
    for index, node in enumerate(nodes):
        port = ports[index]
        d = get_repr_mapping(node, port=port)
        inbound_tag = format_repr(formats['inbound_tag_format'], d)
        outbound_tag = format_repr(formats['outbound_tag_format'], d)
        
        # inbound
        inbound = deepcopy(inbound_template)
        inbound.update({
            'port': port,
            'tag': inbound_tag
        })
        result['inbounds'].append(inbound)

        # outbound
        outbound = deepcopy(outbound_template)
        outbound['QV2RAY_OUTBOUND_METADATA'].update({
            'connectionId': node.id,
            'displayName': outbound_tag
        })
        result['outbounds'].append(outbound)

        # rule
        rule = deepcopy(rule_template)
        rule.update({
            'QV2RAY_RULE_TAG': format_repr(formats['rule_tag_format'], d),
            'inboundTag': [inbound_tag],
            'outboundTag': outbound_tag
        })
        ruleListDomain = route_rules.get('domains', [])
        ruleListIp = route_rules.get('ips', [])
        if ruleListDomain or ruleListIp:
            if ruleListDomain:
                ruleDomain = deepcopy(rule)
                ruleDomain.update({'domain': ruleListDomain})
                if ruleListIp: # deduplicate
                    ruleDomain.update({'QV2RAY_RULE_TAG': format_repr(formats['rule_tag_format'], d) + ' (domain)'})
                result['routing']['rules'].append(ruleDomain)
            if ruleListIp:
                ruleIp = deepcopy(rule)
                ruleIp.update({'ip': ruleListIp})
                if ruleDomain: # deduplicate
                    ruleIp.update({'QV2RAY_RULE_TAG': format_repr(formats['rule_tag_format'], d) + ' (ip)'})
                result['routing']['rules'].append(ruleIp)
        else:
            result['routing']['rules'].append(rule)

    # block rule
    if block_rules.get('domains') or block_rules.get('ips'):
        rule = deepcopy(rule_template)
        rule.pop('inboundTag')
        rule.update({'outboundTag': 'block'})

        if block_rules.get('domains'):
            ruleDomain = deepcopy(rule)
            ruleDomain.update({
                'QV2RAY_RULE_TAG': 'block-domain',
                'domain': block_rules['domains']
            })
            result['routing']['rules'].insert(0, ruleDomain) # block rule be the first rule
        if block_rules.get('ips'):
            ruleIp = deepcopy(rule)
            ruleIp.update({
                'QV2RAY_RULE_TAG': 'block-ip',
                'ip': block_rules['ips']
            })
            result['routing']['rules'].insert(0, ruleIp)
        result['outbounds'].append({"QV2RAY_OUTBOUND_METADATA": {},"mux": {},"protocol": "blackhole","sendThrough": "0.0.0.0","settings": {"response": {"type": "none"}},"streamSettings": {},"tag": "block"})

    return result



def prepare_qv2ray_balancer_template(config):
    # balancer strategy type
    qv2ray_balancer_template['routing']['balancers'][0]['strategy']['type'] = config['v2ray']['balancer_strategy']
    ## domainMatcher
    qv2ray_balancer_template['routing']['domainMatcher'] = config['v2ray']['domainMatcher']


def generate_qv2ray_balancer_config(
        nodes :List[Node],
        listenIp,
        ports :dict,
        route_settings=[],    
        route_type_order = ['block', 'direct', 'proxy'],
        bypassCN=True,
        bypassLAN=True,
        config: dict={}
    ):
    '''
        ports = {
            'http': 1081,
            'socks': 1080,
        }
    '''
    assert(len(route_type_order) == 3)
    
    # result
    result = deepcopy(qv2ray_balancer_template)
    
    outbound_tag_format = config['balancer']['outbound_tag_format']

    # fix duplicate tag error
    _outbound_tags_d = {}
    index = 0
    for index, node in enumerate(nodes):
        d = get_repr_mapping(node)
        _outbound_tags_d[ format_repr(outbound_tag_format, d) ] = ''

    if (index + 1) > len(_outbound_tags_d):
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

    result['inbounds'] = inbounds

    ## outbounds, balancer selector
    outbounds = []
    selector = []

    block_rule_in = False
    direct_rule_in = False
    for index, node in enumerate(nodes):
        d = get_repr_mapping(node)
        outbound_tag = format_repr(outbound_tag_format, d)
        # outbound
        if node in (block_node, direct_node):
            if node == block_node:
                outbounds.append(outbound_block_template)
                block_rule_in = True
            elif node == direct_node:
                outbounds.append(outbound_direct_template)
                direct_rule_in = True
            # selector.append(node.name) # NO !
        else:
            outbounds.append({
                "QV2RAY_OUTBOUND_METADATA": {
                    'connectionId': node.id,
                    'displayName': outbound_tag,
                    "metaType": 1
                }
            })
            selector.append(outbound_tag)

    if not block_rule_in:
        outbounds.append(outbound_block_template)
    if not direct_rule_in:
        outbounds.append(outbound_direct_template)

    result['outbounds'] = outbounds
    # common prefixes of tags in selector
    if config['v2ray']['selector_use_prefixes']:
        selector = common_prefixes(selector)

    result['routing']['balancers'][0]['selector'] = selector

    ## route rules
    rules = []
    rule_common = {
        "QV2RAY_RULE_ENABLED": True,
        "QV2RAY_RULE_TAG": "",
        "type": "field",
        "inboundTag": inbound_tags,
    }
    for rule_type in route_type_order:
        for domain_or_ip in ('ip', 'domain'):
            rule = deepcopy(rule_common)
            rule.update({
                "QV2RAY_RULE_TAG": f"{rule_type}-{domain_or_ip}",
                # 'domain': route_settings.get('domains', {}).get(rule_type, [])
                # 'ip': route_settings.get('ips', {}).get(rule_type, [])
                domain_or_ip: route_settings.get(domain_or_ip + 's', {}).get(rule_type, [])
            })
            if rule_type == 'proxy':
                rule["balancerTag"] = "balancer"
            else: # block, direct
                rule["outboundTag"] = rule_type
            rules.append(rule)

    # delete empty rules
    for index in range(len(rules) - 1, -1, -1):
        if not rules[index].get('domain') and not rules[index].get('ip'):
            del rules[index]

    # 'bypass' rules
    if bypassCN:
        # find starting index of 'direct' rules 
        index_direct = 0
        for index_direct, rule in enumerate(rules):
            if rule.get('outboundTag', '') == 'direct':
                break
        rules_bypassCN = load_json(config["v2ray_object_templates"]['rules_bypassCN'])
        rules_bypassCN = format_json_obj(rules_bypassCN, globals())
        rules = rules[0:index_direct] + rules_bypassCN + rules[index_direct:]

    if bypassLAN:
        rules_bypassLAN = load_json(config["v2ray_object_templates"]['rules_bypassLAN'])
        rules_bypassLAN = format_json_obj(rules_bypassLAN, globals())
        rules = rules_bypassLAN + rules

    result['routing']['rules'] = rules

    ## balancer stategy type
    balancer_strategy = config['v2ray']['balancer_strategy']
    if balancer_strategy == 'leastPing': # ( v2ray 4.38.0+ )
        observatory = {
            "observatory": {
                "subjectSelector": selector
            }}
        result.update(observatory)
    else:
        result.pop('observatory', {})

    ## domainStrategy
    result['routing']['domainStrategy'] = route_settings.get('domainStrategy', 'AsIs')

    return result



if __name__ == '__main__':
    # see test.py
    pass
