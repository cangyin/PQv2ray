
# PyQt5 imports
from sys import argv
from ui.scratchwin import ScratchWin
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from components import RunOnce, Node, NodeListModel
from components.utils import *
from components import generators as gen

from ui import *


app = QApplication(argv)


def balancer_test():

    win = MainWindow()
    win.reloadQv2rayConfigs()
    
    # use Qv2ray current route settings
    qv2ray_conf =  win.qv2ray_conf
    route_settings = qv2ray_conf.get('defaultRouteConfig', {}).get('routeConfig', {})

    nodes = gen.get_nodes_in_group(gen.default_group_id)

    nodes.insert(0, Node(
        name='block'
    ))

    ports = {'http': 1083, 'socks': 1082}

    subconfig = win.config['balancer']

    # generate Qv2ray complex config
    qv2ray_result = gen.generate_qv2ray_balancer_config(
        nodes=nodes,
        listenIp='127.0.0.1',
        ports=ports,
        route_settings=route_settings, # route_rules
        route_type_order=['direct', 'block', 'proxy'],
        bypassCN=False,
        bypassLAN=False,
        formats=subconfig,
    )

    dump_json(qv2ray_result, 'test.json')

def scratch_test():
    win = ScratchWin()
    win.show()

    return(app.exec_())


if __name__ == "__main__":
    # balancer_test()
    scratch_test()
