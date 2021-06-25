
# PyQt5 imports
from genericpath import exists
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import qtawesome

from ui.mainwin import *
from ui.qv2ray_balancer import *
from ui.qv2ray_multi_port import *
from ui.settings import *

from components import RunOnce, Node, NodeListModel
from components.config import load_config
from components import generators as gen

from .qv2raybalancerform import *
from .qv2raymultiportform import *
from .settingsform import *
from .textcontentform import *

import time

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.config = load_config('config.json')
        Node.set_default_format(self.config['ui']['node_repr_format'])
        
        self.group_names = []
        self.model_left = NodeListModel(0, self)
        self.model_right = NodeListModel(0, self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.postSetupUi()


    def postSetupUi(self):
        ui = self.ui
        self.reloadStyleSheet()
        
        ui.editQvConfigFolder.setText(self.config['qv2ray']['config_folder'])

        icon_options = [{
            'scale_factor': 0.8,
            'color': 'black',
            'color_disabled': 'white'
        }]
        ui.btnAppendToRight.setIcon(qtawesome.icon('fa5s.plus', options=icon_options))
        ui.btnDeleteFromRight.setIcon(qtawesome.icon('fa5s.trash-alt', options=icon_options))
        ui.btnSettings.setIcon(qtawesome.icon('fa5s.cogs', options=icon_options))

        ui.listViewLeft.setModel(self.model_left)
        ui.listViewRight.setModel(self.model_right)

        self.selection_left = QItemSelectionModel(self.model_left, self)
        self.selection_right = QItemSelectionModel(self.model_right, self)

        ui.listViewLeft.setEditTriggers(QAbstractItemView.NoEditTriggers)
        ui.listViewRight.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        ui.listViewLeft.setSelectionMode(QAbstractItemView.MultiSelection)
        # ui.listViewRight.setSelectionMode(QAbstractItemView.MultiSelection)
        
        ui.listViewLeft.setSelectionModel(self.selection_left)
        ui.listViewRight.setSelectionModel(self.selection_right)

        ui.listViewLeft.setWordWrap(False)
        ui.listViewRight.setWordWrap(False)


    def reloadStyleSheet(self) -> None:
        styleSheet = open('ui/style.qss', 'rt', encoding='UTF-8').read()

        uiconfig = self.config['ui']
        for key in uiconfig:
            styleSheet = styleSheet.replace('<' + key +'>', str(uiconfig[key]))

        super().setStyleSheet(styleSheet)


    def saveConfig(self):
        dump_json(self.config, 'config.json')


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.saveConfig()
        return super().closeEvent(a0)


    def populateGroupNames(self):
        ui = self.ui
        
        self.group_names = []
        for group_id in gen.groups:
            group = gen.groups[group_id]
            self.group_names.append(group['displayName'])
        ui.comboGroups.clear()
        ui.comboGroups.addItems(self.group_names)


    def populateNodeListLeft(self):
        ui = self.ui
        if not ui.nodeSelectorPane.isEnabled():
            return
        
        group_name = ui.comboGroups.currentText()
        group_id = gen.get_group_id(group_name)
        connection_ids = gen.groups[group_id].get('connections', [])

        nodes = []
        for row, connection_id in enumerate(connection_ids):
            nodes.append(Node(
                id=connection_id,
                name=gen.get_display_name(connection_id),
                group=group_name,
                group_id=group_id,
            ))
        self.model_left.resetNodes(nodes)


    def updateNodeLists(self):
        Node.set_default_format(self.config['ui']['node_repr_format'])
        # left
        self.populateNodeListLeft()
        # right
        self.model_right.resetNodes(self.model_right.getNodes())


    def getUserPickedNodes(self):
        return self.model_right.getNodes()


    def checkQv2rayFolder(self, folder :str):
        valid = path.exists( path.join(folder, qv2ray_bin_name) )
        print(valid)
        return valid


    def checkQv2rayConfigFolder(self, folder :str):
        valid = path.exists(folder + '/groups.json')
        valid = valid and path.exists(folder + '/connections.json')
        valid = valid and path.isdir(folder + '/connections')
        return valid


    def checkQv2rayConfigFolderUi(self):
        ui = self.ui
        qv_config_folder = ui.editQvConfigFolder.text()
        valid = self.checkQv2rayConfigFolder(qv_config_folder)

        if valid:
            self.config['qv2ray']['config_folder'] = qv_config_folder
        ui.groupBoxBtns.setEnabled(valid)
        ui.comboGroups.setEnabled(valid)
        ui.nodeSelectorPane.setEnabled(valid)
        return valid
        

    def reloadQv2rayConfigs(self):
        folder = self.config['qv2ray']['config_folder']
        gen.groups = load_json( folder + '/groups.json' )
        gen.connections = load_json( folder + '/connections.json' )
        gen.qv2ray_multi_port_template = load_json( self.config['multi_port_forwarding']['qv2ray_template_path'] )
        gen.qv2ray_balancer_template = load_json( self.config['balancer']['qv2ray_template_path'] )
        gen.inbound_http_template = load_json( self.config["v2ray_object_templates"]["inbound_http"] )
        gen.inbound_socks_template = load_json( self.config["v2ray_object_templates"]["inbound_socks"] )
        gen.outbound_block_template = load_json( self.config["v2ray_object_templates"]["outbound_block"] )
        gen.outbound_direct_template = load_json( self.config["v2ray_object_templates"]["outbound_direct"] )
        self.qv2ray_conf = load_json( folder + '/Qv2ray.conf' )


    def isQv2rayComplexConfig(self, node_id :str):
        config_path = self.config['qv2ray']['config_folder'] + f'/connections/{node_id}.qv2ray.json'
        bExist = path.exists(config_path)
        config = {} if not bExist else load_json( config_path )
        bRule = ('routing' in config) and ('rules' in config['routing'])
        bRules = bRule and len(config['routing']['rules']) > 0
        bInboundCount  = ('inbounds' in config) and len(config['inbounds']) > 0
        bOutboundCount = ('outbounds' in config) and len(config['outbounds']) > 1
        return bRules or bInboundCount or bOutboundCount


    def jsonHightlightAsRichText(self, text :str):
        # prepare styles
        colors = self.config['ui']['json_highlight_colors']
        key_style = f'style="color: {colors["key"]};"'
        value_style1 = f'style="color: {colors["value1"]};"'
        value_style2 = f'style="color: {colors["value2"]};"'
        # format as HTML
        richText = '<pre>' + text + '</pre>'
        richText = re.sub(r'(".+"):\s+(".*")(,?)$', rf'<span {key_style}>\1</span>: <span {value_style1}>\2</span>\3', richText, flags=re.MULTILINE)
        richText = re.sub(r'(".+"):\s+([^\[\{"]+?)(,?)$', rf'<span {key_style}>\1</span>: <span {value_style2}>\2</span>\3', richText, flags=re.MULTILINE)
        richText = re.sub(r'(".+"):\s+(.*[\[\{\}\]].*)(,?)$', rf'<span {key_style}>\1</span>: \2\3', richText, flags=re.MULTILINE)
        richText = re.sub(r'^(\s+)("[^"]+")(,?)$', rf'\1<span {value_style1}>\2</span>\3', richText, flags=re.MULTILINE)
        return richText


    def showJsonContent(self, json :dict, title, description) -> bool:
        text = dump_jsons(json)
        
        w = TextContentForm(self, title)
        w.label.setText(description)
        if self.config['ui']['json_highlight']:
            # rich text
            w.textEdit.setHtml(self.jsonHightlightAsRichText(text))
            w.textEdit.setVisible(True)
        else:
            # plain text
            w.plainTextEdit.setPlainText(text)
            w.plainTextEdit.setVisible(True)
        return w.exec() == QDialog.Accepted


    def addNodeToQv2ray(self, node :'Node', qv2ray_node_file :str):
        group_id = gen.get_group_id(node.group) or gen.default_group_id
        gen.groups[group_id]['connections'].append(node.id)
        gen.connections.update({
            node.id: {
                "creationDate": int(time.time()),
                "displayName": node.name,
                "lastConnected": 0,
                "lastUpdatedDate": 0,
            }
        })
        qv2ray_config_folder = self.config['qv2ray']['config_folder']
        dump_json(gen.groups, qv2ray_config_folder + '/groups.json')
        dump_json(gen.connections, qv2ray_config_folder + '/connections.json')
        copy_file(qv2ray_node_file, qv2ray_config_folder + f'/connections/{node.id}.qv2ray.json')


    def addNodeToQv2rayUi(self, new_node :Node, qv2ray_node_file :str) -> bool:
        '''
        merge into Qv2ray connection config system, interactively.
        '''

        # check process
        while process_exists('qv2ray.exe'):
            msg = '请您退出 Qv2ray 程序。' if not self.config['qv2ray']['auto_start_qv2ray'] else '请您退出 Qv2ray 程序，节点导入后会自动重启 Qv2ray。'
            res = QMessageBox.information(self, '请退出 Qv2ray 程序', msg, buttons=QMessageBox.Ok | QMessageBox.Close)
            if res != QMessageBox.Ok:
                return False

        # reload Qv2ray configs after it exits.
        self.reloadQv2rayConfigs()

        # do merge
        self.addNodeToQv2ray(new_node, qv2ray_node_file)
        
        if self.config['qv2ray']['auto_start_qv2ray']:
            start_qv2ray_process(self.config['qv2ray']['folder'])
            time.sleep(0.5)

        if qv2ray_process_exists():
            res = QMessageBox.information(self, '完成', '新配置导入完成，Qv2ray已经启动。', buttons=QMessageBox.Ok | QMessageBox.Close)
        else:
            res = QMessageBox.information(self, '完成', '新配置导入完成，但Qv2ray尚未启动，您可以手动启动它。', buttons=QMessageBox.Ok | QMessageBox.Close)
        return res == QMessageBox.Ok


    @pyqtSlot(str)
    def on_editQvConfigFolder_textChanged(self, text):
        if self.checkQv2rayConfigFolderUi():
            self.reloadQv2rayConfigs()
            self.populateGroupNames()
        else:
            self.model_right.resetNodes()


    @pyqtSlot()
    def on_btnBrwsQvConfigFolder_clicked(self):
        ui = self.ui
        qv_config_folder = QFileDialog.getExistingDirectory(self, '选择 Qv2ray 配置文件夹', self.config['qv2ray']['config_folder'])
        if qv_config_folder:
            qv_config_folder = relative_path(qv_config_folder)
            ui.editQvConfigFolder.setText(qv_config_folder) # triggers on_editQvConfigFolder_textChanged
            if not self.checkQv2rayConfigFolder(qv_config_folder):
                QMessageBox.warning(self, '错误', f'您所选择的文件夹<br/>{qv_config_folder}<br/>看起来不像是 Qv2ray 的配置文件夹。')


    @pyqtSlot(str)
    def on_comboGroups_currentTextChanged(self, s :str):
        if s:
            print(s)
            self.populateNodeListLeft()


    @pyqtSlot()
    def on_btnAppendToRight_clicked(self):
        ui = self.ui
        nodes_right = self.model_right.getNodes()
        ignored_nodes = []

        for index in self.selection_left.selectedIndexes():
            node = self.model_left.getNode(index.row())
            # check if Qv2ray complex config
            if node and self.isQv2rayComplexConfig(node.id):
                ignored_nodes.append(node)
                continue
            if not node in nodes_right:
                self.model_right.appendNode(node)

        if ignored_nodes:
            nodes_str = '<br/>'.join([node.name for node in ignored_nodes])
            if len(ignored_nodes) > 1:
                msg = f'您选中的这些节点： <br/><br/><strong>{nodes_str}</strong><br/><br/> 本身是 Qv2ray 的复杂配置节点，已忽略！'
            else:
                msg = f'您选中的节点 <strong>{nodes_str}</strong> 本身是 Qv2ray 的复杂配置节点，已忽略！'
            QMessageBox.information(self, '选中了复杂配置节点', msg)


    @pyqtSlot()
    def on_btnDeleteFromRight_clicked(self):
        selectedRows = self.selection_right.selectedRows()
        selectedRows = sorted(selectedRows, key=lambda modelIndex :modelIndex.row(), reverse=True)
        for index in selectedRows:
            self.model_right.removeNode(index.row())


    @pyqtSlot()
    def on_listViewLeft_focusIn(self):
        ui = self.ui
        ui.btnAppendToRight.setEnabled(True)
        ui.btnDeleteFromRight.setEnabled(False)


    @pyqtSlot()
    def on_listViewRight_focusIn(self):
        ui = self.ui
        ui.btnAppendToRight.setEnabled(False)
        ui.btnDeleteFromRight.setEnabled(True)


    @pyqtSlot()
    def on_btnCheckAllLeft_clicked(self):
        selection = QItemSelection(self.model_left.index(0,0), self.model_left.index(self.model_left.rowCount()-1,0))
        self.selection_left.select(selection, QItemSelectionModel.Select)
        self.ui.btnAppendToRight.setEnabled(True)


    @pyqtSlot()
    def on_btnCheckAllRight_clicked(self):
        selection = QItemSelection(self.model_right.index(0,0), self.model_right.index(self.model_right.rowCount()-1,0))
        self.selection_right.select(selection, QItemSelectionModel.Select)
        self.ui.btnDeleteFromRight.setEnabled(True)


    @pyqtSlot()
    def on_btnUncheckAllLeft_clicked(self):
        self.selection_left.clear()


    @pyqtSlot()
    def on_btnUncheckAllRight_clicked(self):
        self.selection_right.clear()


    @pyqtSlot()
    def on_btnSettings_clicked(self):
        w = SettingsForm(self)
        if(w.exec() == QDialog.Accepted):
            self.config.update(w.config)
            self.saveConfig()
            self.reloadStyleSheet()
            self.updateNodeLists()


    @pyqtSlot()
    def on_btnQv2rayMultiPort_clicked(self):
        if len(self.getUserPickedNodes()) <= 0:
            QMessageBox.warning(self, '错误', '请至少选择一个节点。')
            return

        w = Qv2rayMultiPortForm(self)
        if(w.exec() == QDialog.Accepted):
            pass


    @pyqtSlot()
    def on_btnQv2rayBalancer_clicked(self):
        if len(self.getUserPickedNodes()) <= 0:
            QMessageBox.warning(self, '错误', '请至少选择一个节点。')
            return

        w = Qv2rayBalancerForm(self)
        if(w.exec() == QDialog.Accepted):
            pass
