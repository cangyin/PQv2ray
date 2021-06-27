from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from .qv2ray_multi_port import Ui_Qv2rayMultiPortForm

from components import *


class Qv2rayMultiPortForm(QDialog):

    def __init__(self, parent: Optional['QWidget'], flags: Union[Qt.WindowFlags, Qt.WindowType]=Qt.Dialog) -> None:
        super().__init__(parent=parent, flags=flags)
        self.config = g_config['multi_port']
        self.nodes = parent.getUserPickedNodes()
        self.group_names = parent.group_names

        self.ui = Ui_Qv2rayMultiPortForm()
        self.ui.setupUi(self)
        ui = self.ui

        self.block_rule_schemes = ['（无）', '（自定义）', '使用 Qv2ray 阻断规则']
        self.route_schemes = ['（空白）', '（自定义）', '直连', '代理', '阻断']
        
        ui.spinPortStart.setValue(self.config['default_port_start'])
        ui.comboBlockRuleScheme.addItems(self.block_rule_schemes)
        ui.comboRouteScheme.addItems(self.route_schemes)

        ui.comboUpdateNodeName.link_comboBox(ui.comboUpdateNodeGroup)
        ui.comboUpdateNodeName.set_selector(lambda node: node.is_qv2ray_complex_node())
        ui.comboUpdateNodeGroup.addItems(self.group_names)

        ui.comboAutoImportGroup.addItems(self.group_names)

        picked_groups = deduplicate([node.group for node in self.nodes])
        if len(picked_groups) == 1:
            ui.editAutoImportName.setText( f'多入站 - {picked_groups[0]} - {len(self.nodes)}' )
        else:
            ui.editAutoImportName.setText( f'多入站 - (多个分组) - {len(self.nodes)}' )

    @property
    def ports(self):
        ui = self.ui
        ports = range(ui.spinPortStart.value(), ui.spinPortEnd.value() + 1) # range end + 1
        return ports

    def setHelpText(self, text :str):
        try:
            self.ui.labHelp.setText(text)
        except:
            pass

    def updateInstantHoverHelp(self):
        ui = self.ui
        helps = {
        }
        w = QApplication.widgetAt(QCursor.pos())
        if w:
            name = w.objectName()
            help_text = ''
            if name in helps:
                help_text = helps[name]
            else:
                if name == 'comboAutoImportGroup':
                    help_text = f'''<p>将生成的复杂配置（多端口节点）放在 <strong>{ui.comboAutoImportGroup.currentText()}</strong> 分组中。'''
                elif name == 'comboRouteScheme':
                    help_text = [
                        '''
                        <p>空白路由规则。每个端口的入站流量一定能到达对应的出站节点。</p>
                        ''',
                        '''
                        <p>自定义路由规则。即使用您填入的路由规则。</p>
                        <p>每个端口的入站流量，只有匹配您的规则的流量，才能到达对应的出站节点，否则被定向到默认出站节点 (所选节点列表中的第一个节点)。</p>
                        <p>路由规则的写法与Qv2ray全局路由设置的写法一样，参见示例。</p>
                        ''',
                        '''
                        <p>使用您在Qv2ray中设置的全局路由规则中<strong>直连</strong>部分的规则。</p>
                        <p>每个端口的入站流量，只有匹配直连规则的流量，才能到达对应的出站节点，否则被定向到默认出站节点 (所选节点列表中的第一个节点)。</p>
                        ''',
                        '''
                        <p>使用您在Qv2ray中设置的全局路由规则中<strong>代理</strong>部分的规则。</p>
                        <p>每个端口的入站流量，只有匹配代理规则的流量，才能到达对应的出站节点，否则被定向到默认出站节点 (所选节点列表中的第一个节点)。</p>
                        ''',
                        '''
                        <p>使用您在Qv2ray中设置的全局路由规则中<strong>阻断</strong>部分的规则。</p>
                        <p>每个端口的入站流量，只有匹配阻断规则的流量（“阻断”在这里有一点误导性，但它仅仅是指代您在Qv2ray全局路由设置中“阻断”部分的规则），才能到达对应的出站节点，否则被定向到默认出站节点 (所选节点列表中的第一个节点)。</p>
                        ''',
                    ][ui.comboRouteScheme.currentIndex()]
                elif name == 'comboBlockRuleScheme':
                    help_text = [
                        '''
                        <p>不使用任何阻断规则。</p>
                        ''',
                        '''
                        <p>自定义阻断规则。即使用您填入的规则。</p>
                        <p>任何匹配阻断规则的流量，都会被抛弃。</p>
                        ''',
                        '''
                        <p>使用您在Qv2ray中设置的全局路由规则中<strong>阻断</strong>部分的规则。</p>
                        <p>任何匹配阻断规则的流量，都会被抛弃。</p>
                        ''',
                    ][ui.comboBlockRuleScheme.currentIndex()]
            self.setHelpText(help_text)

    def event(self, a0: QEvent) -> bool:
        self.updateInstantHoverHelp()
        return super().event(a0)

    @pyqtSlot(bool)
    def on_groupBoxSw_toggled(self, b :bool):
        if b and not self.ui.editSwFile.text():
            self.on_btnBrowseSwFile_clicked()

    @pyqtSlot()
    def on_btnBrowseSwFile_clicked(self):
        ui = self.ui
        file_name = QFileDialog.getOpenFileName(self, '选择由 SwitchyOmega 插件导出的备份文件', '.', '.bak (*.bak);; 任何文件 (*.*)')[0]
        if file_name:
            file_name = relative_path(file_name)
            ui.editSwFile.setText(file_name)

    @pyqtSlot(int)
    def on_comboBlockRuleScheme_currentIndexChanged(self, i):
        ui = self.ui
        blockRulesDomain = ''
        blockRulesIp = ''
        if i == 1: # custom rules
            blockRulesDomain = dedent('''
                示例：
                geosite:category-ads-all
                domain:ads.dummysite.com
            ''')
            blockRulesIp = dedent('''
                示例：
                192.168.1.0/24
            ''')
        elif i == 2: # rules from Qv2ray
            rules = gen.qv2ray_conf['defaultRouteConfig']['routeConfig']
            blockRulesDomain = '\n'.join( rules['domains'].get('block', []) )
            blockRulesIp = '\n'.join( rules['ips'].get('block', []) )

        ui.txtRulesBlockDomain.setPlainText(blockRulesDomain.strip())
        ui.txtRulesBlockIp.setPlainText(blockRulesIp.strip())
        ui.groupBoxBlockRules.setEnabled(i != 0)

    @pyqtSlot(int)
    def on_comboRouteScheme_currentIndexChanged(self, i):
        ui = self.ui
        rulesDomain = ''
        rulesIp = ''
        if i == 1: # custom rules
            rulesDomain = dedent('''
                示例：
                geosite:geolocation-cn
                domain:baidu.com
            ''')
            rulesIp = dedent('''
                示例
                117.131.104.7
            ''')
        elif i >= 2: # rules from Qv2ray
            key = gen.outbound_tag_classes[i-2]
            rules = gen.qv2ray_conf['defaultRouteConfig']['routeConfig']
            rulesDomain = '\n'.join( rules['domains'].get(key, []) )
            rulesIp = '\n'.join( rules['ips'].get(key, []) )
            
        ui.txtRulesDomain.setPlainText(rulesDomain.strip())
        ui.txtRulesIp.setPlainText(rulesIp.strip())

    @pyqtSlot(int)
    def on_spinPortStart_valueChanged(self, value):
        total_nodes = len(self.nodes)
        self.ui.spinPortEnd.setValue(value + total_nodes - 1)
        self.ui.labHintPortCount.setText(f'共 {total_nodes} 个端口')

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

        # generate ports-nodes mapping report
        self.generateMappingReport()

        # generate SwitchyOmega file
        if ui.groupBoxSw.isChecked():
            ok = self.generateSwitchyomegaConfig()
            if not ok:
                return

        # generate Qv2ray complex config
        shouldClose = self.generateQv2rayMultiPortConfig()

        # finally, close the dialog
        if shouldClose:
            self.accept()


    def generateMappingReport(self):
        mapping_template = load_json(self.config['mapping_report_template_path'])
        nodes = self.nodes
        ports = self.ports

        result = None
        if isinstance(mapping_template, dict):
            result = {}
            for port, node in zip(ports, nodes):
                d = get_repr_mapping(node, port=port)
                result.update( format_json_obj(mapping_template, d) )
        elif isinstance(mapping_template, list):
            result = []
            for port, node in zip(ports, nodes):
                d = get_repr_mapping(node, port=port)
                result.extend( format_json_obj(mapping_template, d) )

        dump_json(result, self.config['mapping_report_result_path'])


    def generateSwitchyomegaConfig(self):
        bak_file = self.ui.editSwFile.text()
        if not bak_file or not path.exists(bak_file):
            QMessageBox.warning(self, "未选择 SwitchyOmega 文件", "请选择由 SwitchyOmega 插件导出的备份文件")
            return False

        proxy_template = load_json(self.config['switchyomega_proxy_template'])
        
        result = load_json(bak_file)
        for port, node in zip(self.ports, self.nodes):
            d = get_repr_mapping(node, port=port)
            switchyomega_item = format_json_obj(proxy_template, d)
            result.update(switchyomega_item)

        # dump result
        root, ext = path.splitext(bak_file)
        result_path = root + '.result' + ext
        dump_json(result, result_path)
        return True


    def generateQv2rayMultiPortConfig(self):
        ui = self.ui
        route_rules = {
            'domains': ui.txtRulesDomain.toPlainText().strip().splitlines(),
            'ips': ui.txtRulesIp.toPlainText().strip().splitlines()
        }
        block_rules = {
            'domains': ui.txtRulesBlockDomain.toPlainText().strip().splitlines(),
            'ips': ui.txtRulesBlockIp.toPlainText().strip().splitlines()
        }
        
        if self.config['default_port_type'] == 'HTTP':
            inbound_template = gen.inbound_http_template 
        else:
            inbound_template = gen.inbound_socks_template 
        
        qv2ray_result = gen.generate_qv2ray_multi_port_config(
            nodes=self.nodes,
            ports=self.ports,
            inbound_template=inbound_template,
            route_rules=route_rules,
            block_rules=block_rules,
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
        return shouldClose
