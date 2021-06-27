from enum import Enum
from .utils import *
from .config import g_config


class NodeComplexityType(Enum):
    Simple = 'simple'
    General = 'general'
    Balancer = 'balancer'
    MultiPort = 'multi-port'


_node_repr_format = "[{node.group}] {node.name}"


class Node():

    def __init__(self, id='', name='', group='', group_id=''):

        self.id = id  # e.g. connection_id
        self.name = name  # e.g. display name of connection
        self.group = group
        self.group_id = group_id

    @staticmethod
    def set_default_format(fmt: str):
        global _node_repr_format
        _node_repr_format = fmt

    def format(self, fmt=_node_repr_format):
        return format_repr(fmt, self.get_format_dict())

    def get_format_dict(self):
        return {'node.'+k: v for k, v in self.__dict__.items()}

    def __repr__(self) -> str:
        return self.format(_node_repr_format)

    def __str__(self) -> str:
        return self.format()
        
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id
        elif isinstance(other, str):
            return self.id == other

    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            _path = self.profile_path
            if path.exists(_path):
                self._profile = load_json(_path)
            else:
                self._profile = {}
        return self._profile

    @property
    def profile_path(self):
        if not hasattr(self, '_pf_path'):
            self._pf_path = g_config['qv2ray']['config_folder'] + f'/connections/{self.id}.qv2ray.json'
        return self._pf_path

    @property
    def complexity_type(self):
        if not hasattr(self, '_cp_type'):
            if not self.is_qv2ray_complex_node():
                self._cp_type = NodeComplexityType.Simple
            elif self.is_balancer_node():
                self._cp_type = NodeComplexityType.Balancer
            elif self.is_multi_port_node():
                self._cp_type = NodeComplexityType.MultiPort
            else:
                self._cp_type = NodeComplexityType.General
        return self._cp_type

    def is_qv2ray_complex_node(self):
        profile = self.profile
        bRule = ('routing' in profile) and ('rules' in profile['routing'])
        bRules = bRule and len(profile['routing']['rules']) > 0
        bInboundCount  = ('inbounds' in profile) and len(profile['inbounds']) > 0
        bOutboundCount = ('outbounds' in profile) and len(profile['outbounds']) > 1
        return bRules or bInboundCount or bOutboundCount

    def is_balancer_node(self):
        profile = self.profile
        bBalancers = ('routing' in profile) and ('balancers' in profile['routing'])
        bSelector = bBalancers and ('selector' in profile['routing']['balancers'])
        if not bSelector:
            return False
        selector = profile['routing']['balancers']['selector']
        bSelectorLen = bSelector and len(selector) > 0
        return bSelectorLen and len(selector[0]) > 0

    def is_multi_port_node(self):
        profile = self.profile
        return ("inbounds" in profile) and len(profile['inbounds']) > 1
