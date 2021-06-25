# PyQt5 imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ui.qv2ray_balancer import *

from components import Node
from components.utils import *
from components import generators as gen


class Qv2rayBalancerForm(QDialog):

    def __init__(self, parent: Optional['QWidget'], flags: Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType]=Qt.Dialog) -> None:
        super().__init__(parent=parent, flags=flags)

        self.config = parent.config['balancer']
        self.nodes = parent.getUserPickedNodes()
        self.group_names = parent.group_names

        self.route_type_mapping = {
            '阻断': 'block',
            '代理': 'proxy',
            '直连': 'direct',
        }
        # mapping from special groups to nodes
        self.special_group_mapping = {
            '阻断': [ gen.block_node ],
            '直连': [ gen.direct_node ]
        }

        ## setup UI
        self.ui = Ui_Qv2rayBalancerForm()
        self.ui.setupUi(self)
        ui = self.ui

        ## post setup UI
        ui.comboFallbackOutboundNode.link_comboBox(ui.comboFallbackOutboundGroup)
        ui.comboFallbackOutboundNode.set_special_group_mapping(self.special_group_mapping)
        ui.comboFallbackOutboundNode.set_selector(lambda node: not self.parent().isQv2rayComplexConfig(node))

        ui.comboFallbackOutboundGroup.addItems(self.group_names)
        ui.comboFallbackOutboundGroup.insertSeparator(len(self.group_names))
        ui.comboFallbackOutboundGroup.addItems(self.special_group_mapping)

        ui.comboUpdateNodeName.link_comboBox(ui.comboUpdateNodeGroup)
        ui.comboUpdateNodeName.set_selector(lambda node: self.parent().isQv2rayComplexConfig(node))
        ui.comboUpdateNodeGroup.addItems(self.group_names)

        ui.comboAutoImportGroup.addItems(self.group_names)

        ui.listRouteTypes.addItems(self.route_type_mapping)

        picked_groups = deduplicate([node.group for node in self.nodes])
        if len(picked_groups) == 1:
            ui.editAutoImportName.setText( f'负载均衡 - {picked_groups[0]} - {len(self.nodes)}' )
        else:
            ui.editAutoImportName.setText( f'负载均衡 - (多个分组) - {len(self.nodes)}' )

        parent.reloadQv2rayConfigs()
        self.qv2ray_conf = parent.qv2ray_conf

        inboundConfig = self.qv2ray_conf.get('inboundConfig', {})
        ui.editListenIp.setText( inboundConfig.get('listenip', '127.0.0.1') )

        socks_port = inboundConfig.get('socksSettings', {}).get('port', 1089)
        if socks_port:
            ui.spinSocksPort.setValue(socks_port)
        ui.chkSocksPort.setChecked(socks_port != 0)

        http_port = inboundConfig.get('httpSettings', {}).get('port', 0)
        if http_port:
            ui.spinHttpPort.setValue(http_port)
        ui.chkHttpPort.setChecked(http_port != 0)

        connectionConfig = self.qv2ray_conf.get('defaultRouteConfig', {}).get('connectionConfig', {})
        ui.chkBypassLAN.setChecked( connectionConfig.get('bypassLAN', True) )
        ui.chkBypassCN.setChecked( connectionConfig.get('bypassCN', True) )

    @pyqtSlot(bool)
    def on_chkHttpPort_toggled(self, b):
        self.ui.spinHttpPort.setEnabled(b)

    @pyqtSlot(bool)
    def on_chkSocksPort_toggled(self, b):
        self.ui.spinSocksPort.setEnabled(b)

    @pyqtSlot(bool)
    def on_rbtnImportQvRouteSettings_toggled(self, b):
        self.ui.widgetQvExportedRouteBrwsPane.setEnabled(b)
        if b and not self.ui.editQvExportedRouteSettings.text():
            self.on_btnBrwsQvExportedRouteSettings_clicked()

    @pyqtSlot()
    def on_btnBrwsQvExportedRouteSettings_clicked(self):
        ui = self.ui
        file_name = QFileDialog.getOpenFileName(self, '选择由 Qv2ray 导出的路由方案', '.', '.JSON 文件 (*.json);; 任何文件 (*.*)')[0]
        if file_name:
            file_name = relative_path(file_name)
            ui.editQvExportedRouteSettings.setText(file_name)

    @pyqtSlot(str)
    def on_comboFallbackOutboundGroup_currentTextChanged(self, text):
        self.ui.comboFallbackOutboundNode.setVisible(text not in self.special_group_mapping)

    @pyqtSlot(bool)
    def on_rbtnAutoImport_toggled(self, b):
        if b:
            self.ui.importSettingStack.setCurrentIndex(0)

    @pyqtSlot(bool)
    def on_rbtnUpdateNode_toggled(self, b):
        if b:
            self.ui.importSettingStack.setCurrentIndex(1)
        
    @pyqtSlot(bool)
    def on_rbtnManualImport_toggled(self, b):
        self.ui.importSettingStack.setEnabled(not b)
    
    @pyqtSlot()
    def on_btnCommit_clicked(self):
        ui = self.ui

        if not ui.chkHttpPort.isChecked() and not ui.chkSocksPort.isChecked():
            QMessageBox.information(self, '请选择端口类型', '请至少选择一种端口类型')
            return
        
        # route settings
        if ui.rbtnImportQvRouteSettings.isChecked():
            route_settings_file = ui.editQvExportedRouteSettings.text()
            if path.exists(route_settings_file):
                route_settings =  load_json(route_settings_file)
            else:
                QMessageBox.warning(self, '文件不存在', f'无法打开文件 {route_settings_file}')
                return
        else:
            # use Qv2ray current route settings
            self.parent().reloadQv2rayConfigs()
            self.qv2ray_conf = self.parent().qv2ray_conf
            route_settings = self.qv2ray_conf.get('defaultRouteConfig', {}).get('routeConfig', {})

        # route order
        route_type_order = []
        for index in  range(len(self.route_type_mapping)):
            route_type = ui.listRouteTypes.item(index).text()
            route_type = self.route_type_mapping[route_type]
            route_type_order.append(route_type)

        # nodes
        nodes = deepcopy(self.nodes)
        nodes.extend([
            gen.direct_node,
            gen.block_node
        ])

        # fallback node
        fallback_node = ui.comboFallbackOutboundNode.currentData()
        if fallback_node:
            if fallback_node in nodes:
                del nodes[ nodes.index(fallback_node) ]
            nodes.insert(0, fallback_node)

        # ports
        ports = {
            'http': ui.spinHttpPort.value() if ui.chkHttpPort.isChecked() else 0,
            'socks': ui.spinSocksPort.value()  if ui.chkSocksPort.isChecked() else 0
        }

        # generate Qv2ray complex config
        qv2ray_result = gen.generate_qv2ray_balancer_config(
            nodes=nodes,
            listenIp=ui.editListenIp.text(),
            ports=ports,
            route_settings=route_settings, # route_rules
            route_type_order=route_type_order,
            bypassCN=ui.chkBypassCN.isChecked(),
            bypassLAN=ui.chkBypassLAN.isChecked(),
            config=self.parent().config,
        )
        
        # always write result to file
        dump_json(qv2ray_result, self.config['qv2ray_result_path'])

        # merge into Qv2ray connection config system
        shouldClose = False
        if ui.rbtnAutoImport.isChecked():
            qv2ray_new_node = Node(
                id=gen.get_random_node_id(),
                name=ui.editAutoImportName.text(),
                group=ui.comboAutoImportGroup.currentText(),
            )
            shouldClose = self.parent().addNodeToQv2rayUi(
                new_node=qv2ray_new_node,
                qv2ray_node_file=self.config['qv2ray_result_path']
            )
        elif ui.rbtnUpdateNode.isChecked():
            node = ui.comboUpdateNodeName.currentData()
            if not node:
                QMessageBox.warning(self, "未选择欲更新的节点", "请选择一个已有节点")
                return
            shouldClose = self.parent().replaceNodeInQv2ray(node.id, qv2ray_result)
        else: # manual import
            shouldClose = self.parent().showJsonContent(
                json=qv2ray_result,
                title='手动导入复杂配置到Qv2ray',
                description='您可以复制以下全部内容，并使用Qv2ray的JSON导入功能导入节点。'
            )

        # finally, close the dialog
        if shouldClose:
            self.accept()
