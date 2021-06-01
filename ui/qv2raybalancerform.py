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

        self.config = parent.config
        self.nodes = parent.getUserPickedNodes()
        self.group_names = parent.group_names

        self.route_type_mapping = {
            '阻断': 'block',
            '代理': 'proxy',
            '直连': 'direct',
        }
        # mapping from special groups to nodes
        self.special_group_mapping = {
            '阻断': gen.block_node,
            '直连': gen.direct_node
        }

        self.ui = Ui_Qv2rayBalancerForm()
        self.ui.setupUi(self)
        ui = self.ui

        ui.comboFallbackOutboundGroup.addItems(self.group_names)
        ui.comboFallbackOutboundGroup.insertSeparator(len(self.group_names))
        ui.comboFallbackOutboundGroup.addItems(self.special_group_mapping)

        ui.comboAutoImportGroup.addItems(self.group_names)

        ui.listRouteTypes.addItems(self.route_type_mapping)

        picked_groups = deduplicate([node.group for node in self.nodes])
        if len(picked_groups) == 1:
            auto_import_name = '负载均衡 - ' + picked_groups[0] + ' - ' + str(len(self.nodes))
        else:
            auto_import_name = '负载均衡 - (多个分组) - ' + str(len(self.nodes))
        ui.editAutoImportName.setText(auto_import_name)

        parent.reloadQv2rayConfigs()
        self.qv2ray_conf = parent.qv2ray_conf

        inboundConfig = self.qv2ray_conf.get('inboundConfig', {})
        ui.editListenIp.setText( inboundConfig.get('listenip', '127.0.0.1') )
        ui.spinSocksPort.setValue( inboundConfig.get('socksSettings', {}).get('port', 1089) )

        http_port = inboundConfig.get('httpSettings', {}).get('port', 0)
        if http_port:
            ui.spinHttpPort.setValue(http_port)
        ui.chkHttpPort.setEnabled(http_port != 0)

        connectionConfig = self.qv2ray_conf.get('defaultRouteConfig', {}).get('connectionConfig', {})
        ui.chkBypassLAN.setChecked( connectionConfig.get('bypassLAN', True) )
        ui.chkBypassCN.setChecked( connectionConfig.get('bypassCN', True) )


    def getFallBackNode(self):
        ui = self.ui
        fb_group_name = ui.comboFallbackOutboundGroup.currentText()
        if fb_group_name in self.special_group_mapping:
            return self.special_group_mapping[fb_group_name]
        else:
            return ui.comboFallbackOutboundNode.itemData(ui.comboFallbackOutboundNode.currentIndex())

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
            ui.editQvExportedRouteSettings.setText(file_name)

    @pyqtSlot(str)
    def on_comboFallbackOutboundGroup_currentTextChanged(self, text):
        ui = self.ui
        if text in self.special_group_mapping:
            ui.widgetFallBackNode.setVisible(False)
        else:
            ui.comboFallbackOutboundNode.clear()
            for node in gen.get_nodes_in_group(gen.get_group_id(text)):
                ui.comboFallbackOutboundNode.addItem(node.name, node)
            ui.widgetFallBackNode.setVisible(True)

    @pyqtSlot(bool)
    def on_rbtnAutoImport_toggled(self, b):
        self.ui.autoImportSettingPane.setEnabled(b)
        
    @pyqtSlot()
    def on_btnCommit_clicked(self):
        ui = self.ui
        subconfig = self.config['balancer']

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
        nodes = [
            gen.block_node,
            gen.direct_node
        ]
        nodes.extend(deepcopy(self.nodes))

        # fallback node
        fallback_node = self.getFallBackNode()
        if fallback_node.id and self.parent().isQv2rayComplexConfig(fallback_node.id):
            QMessageBox.information(self, '选中了复杂配置节点', '您选择的默认出站节点属于复杂配置节点，而一个复杂配置节点不能引用另外一个复杂配置节点作为出站节点。')
            return
        if fallback_node in nodes:
            del nodes[ nodes.index(fallback_node) ]
        nodes.insert(0, fallback_node)

        # ports
        ports = {
            'http': ui.spinHttpPort.value() if ui.chkHttpPort.isChecked() else 0,
            'socks': ui.spinSocksPort.value()  if ui.chkSocksPort.isChecked() else 0
        }

        gen.prepare_qv2ray_balancer_template(self.config)

        # generate Qv2ray complex config
        qv2ray_result = gen.generate_qv2ray_balancer_config(
            nodes=nodes,
            listenIp=ui.editListenIp.text(),
            ports=ports,
            route_settings=route_settings, # route_rules
            route_type_order=route_type_order,
            bypassCN=ui.chkBypassCN.isChecked(),
            bypassLAN=ui.chkBypassLAN.isChecked(),
            config=self.config,
        )
        
        # always write result to file
        dump_json(qv2ray_result, subconfig['qv2ray_result_path'])

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
                qv2ray_node_file=subconfig['qv2ray_result_path']
            )
        else: # manual import
            shouldClose = self.parent().showJsonContent(
                json=qv2ray_result,
                title='手动导入复杂配置到Qv2ray',
                description='您可以复制以下全部内容，并使用Qv2ray的JSON导入功能导入节点。'
            )

        # finally, close the dialog
        if shouldClose:
            self.accept()
