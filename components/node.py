
# using 'node' == 'connection'
# for example:
#   'node id' stands for 'connection id'
#   'group of node' stands for 'group name of connection'

from components.utils import format_repr

_node_repr_format = "[{node.group}] {node.name}"


class Node():

    def __init__(self, id='', name='', group='', group_id='', fmt=_node_repr_format):
        self.set_default_format(fmt)

        self.id = id  # e.g. connection_id
        self.name = name  # e.g. diaplay name of connection
        self.group = group
        self.group_id = group_id

        # these values better describes a node (or 'connection'), but take more effort to acquire.

        # self.protocol = 'vmess'
        # self.address = 'proxy.google.com' # remote address
        # self.port = 11325 # remote port

    def set_default_format(self, fmt: str):
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
