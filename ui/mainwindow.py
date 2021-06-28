from components.node import NodeComplexityType
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from .mainwin import Ui_MainWindow

from .qv2raybalancerform import *
from .qv2raymultiportform import *
from .settingsform import *
from .textcontentform import *

import qtawesome

from components import *

import time

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # TODO promote config to global
        Node.set_default_format(g_config['ui']['node_repr_format'])
        
        self.model_left = NodeListModel(0, self)
        self.model_right = NodeListModel(0, self)
        self.group_names = []
        self.node_selector = None
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.postSetupUi()


    def postSetupUi(self):
        ui = self.ui
        self.reloadStyleSheet()
        
        ui.editQvConfigFolder.setText(g_config['qv2ray']['config_folder'])

        icon_options = [{
            'scale_factor': 0.8,
            'color': 'black',
            'color_disabled': 'white'
        }]
        ui.btnAppendToRight.setIcon(qtawesome.icon('fa5s.plus', options=icon_options))
        ui.btnDeleteFromRight.setIcon(qtawesome.icon('fa5s.trash-alt', options=icon_options))
        ui.btnSettings.setIcon(qtawesome.icon('fa5s.cogs', options=icon_options))
        ui.btnRefreshList.setIcon(qtawesome.icon('fa5s.sync-alt', options=icon_options))
        fm = ui.labFilter.fontMetrics()
        icon_size = QSize(fm.height(), fm.height())
        ui.labFilter.setPixmap(qtawesome.icon('fa5s.filter', options=[{'color': '#1b8c90'}]).pixmap(icon_size))

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

        self.model_right.rowsInserted.connect(self.on_model_right_rowsChanged)
        self.model_right.rowsRemoved.connect(self.on_model_right_rowsChanged)


    def reloadStyleSheet(self) -> None:
        styleSheet = open(g_config['ui']['stylesheet'], 'rt', encoding='UTF-8').read()

        uiconfig = g_config['ui']
        for key in uiconfig:
            styleSheet = styleSheet.replace('<' + key +'>', str(uiconfig[key]))

        super().setStyleSheet(styleSheet)


    def saveConfig(self):
        dump_json(g_config, 'config.json')


    def closeEvent(self, a0: QCloseEvent) -> None:
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
        ui.comboGroups.insertSeparator(ui.comboGroups.count())
        ui.comboGroups.addItem('（全部）')


    def populateNodeListLeft(self):
        ui = self.ui
        if not ui.nodeSelectorPane.isEnabled():
            return
        
        if ui.comboGroups.currentIndex() == ui.comboGroups.count() - 1:
            # all nodes in all groups
            nodes = []
            for i in range(ui.comboGroups.count() - 2):
                group_name = ui.comboGroups.itemText(i)
                nodes.extend( gen.get_nodes_in_group(gen.get_group_id(group_name)) )
        else:
            group_name = ui.comboGroups.currentText()
            nodes = gen.get_nodes_in_group(gen.get_group_id(group_name))

        if self.node_selector:
            nodes = [node for node in nodes if self.node_selector(node)]
        self.model_left.resetNodes(nodes)


    def updateNodeLists(self):
        Node.set_default_format(g_config['ui']['node_repr_format'])
        # left
        self.populateNodeListLeft()
        # right
        self.model_right.resetNodes(self.model_right.getNodes())


    def getUserPickedNodes(self):
        return self.model_right.getNodes()


    def checkQv2rayFolder(self, folder :str):
        valid = path.exists( path.join(folder, qv2ray_bin_name) )
        logger.info(f'Qv2ray folder {folder} is ' + ('invalid', 'valid')[valid])
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
            g_config['qv2ray']['config_folder'] = qv_config_folder

        for widget in (
            ui.groupBoxBtns,
            ui.comboGroups,
            ui.btnRefreshList,
            ui.nodeSelectorPane
        ):
            widget.setEnabled(valid)
        return valid
        

    def jsonHightlightAsRichText(self, text :str):
        # prepare styles
        colors = g_config['ui']['json_highlight_colors']
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
        if g_config['ui']['json_highlight']:
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
        gen.groups[group_id]['connections'] = gen.groups[group_id].get('connections', []) + [node.id]
        gen.connections.update({
            node.id: {
                "creationDate": int(time.time()),
                "displayName": node.name,
                "lastConnected": 0,
                "lastUpdatedDate": 0,
            }
        })
        qv2ray_config_folder = g_config['qv2ray']['config_folder']
        dump_json(gen.groups, qv2ray_config_folder + '/groups.json')
        dump_json(gen.connections, qv2ray_config_folder + '/connections.json')
        copy_file(qv2ray_node_file, qv2ray_config_folder + f'/connections/{node.id}.qv2ray.json')


    def addNodeToQv2rayUi(self, new_node :Node, qv2ray_node_file :str) -> bool:
        '''
        merge into Qv2ray connection config system, interactively.
        '''

        # check process
        while process_exists('qv2ray.exe'):
            msg = '请您退出 Qv2ray 程序。' if not g_config['qv2ray']['auto_start_qv2ray'] else '请您退出 Qv2ray 程序，节点导入后会自动重启 Qv2ray。'
            res = QMessageBox.information(self, '请退出 Qv2ray 程序', msg, buttons=QMessageBox.Ok | QMessageBox.Close)
            if res != QMessageBox.Ok:
                return False

        # reload low level configs after Qv2ray exits.
        gen.load()

        # do merge
        self.addNodeToQv2ray(new_node, qv2ray_node_file)
        
        if g_config['qv2ray']['auto_start_qv2ray']:
            start_qv2ray_process(g_config['qv2ray']['folder'])
            time.sleep(0.5)

        if qv2ray_process_exists():
            msg = '新配置导入完成，Qv2ray已经启动。'
        else:
            msg = '新配置导入完成，但Qv2ray尚未启动，您可以手动启动它。'
        res = QMessageBox.information(self, '完成', msg, buttons=QMessageBox.Ok | QMessageBox.Close)
        return res == QMessageBox.Ok


    def replaceNodeInQv2rayUi(self, node_id :str, node_json :dict):
        dump_json(node_json, g_config['qv2ray']['config_folder'] + f'/connections/{node_id}.qv2ray.json')
        if not qv2ray_process_exists():
            if g_config['qv2ray']['auto_start_qv2ray']:
                start_qv2ray_process(g_config['qv2ray']['folder'])
                time.sleep(0.5)
            msg = '配置更新完成，Qv2ray已经启动。'
        else:
            msg = '配置更新完成，您需要重启Qv2ray。'
        res = QMessageBox.information(self, '完成', msg, buttons=QMessageBox.Ok | QMessageBox.Close)
        return res == QMessageBox.Ok


    @pyqtSlot(str)
    def on_editQvConfigFolder_textChanged(self, text):
        if self.checkQv2rayConfigFolderUi():
            gen.load()
            self.populateGroupNames()
        else:
            self.model_right.resetNodes()


    @pyqtSlot()
    def on_btnBrwsQvConfigFolder_clicked(self):
        ui = self.ui
        qv_config_folder = QFileDialog.getExistingDirectory(self, '选择 Qv2ray 配置文件夹', g_config['qv2ray']['config_folder'])
        if qv_config_folder:
            qv_config_folder = relative_path(qv_config_folder)
            ui.editQvConfigFolder.setText(qv_config_folder) # triggers on_editQvConfigFolder_textChanged
            if not self.checkQv2rayConfigFolder(qv_config_folder):
                QMessageBox.warning(self, '错误', f'您所选择的文件夹<br/>{qv_config_folder}<br/>看起来不像是 Qv2ray 的配置文件夹。')


    @pyqtSlot(str)
    def on_comboGroups_currentTextChanged(self, s :str):
        if s:
            logger.info(s)
            self.populateNodeListLeft()


    @pyqtSlot()
    def on_btnAppendToRight_clicked(self):
        nodes_right = self.model_right.getNodes()
        ignored_nodes = []

        selectedRows = self.selection_left.selectedRows()
        selectedRows = sorted(selectedRows, key=lambda modelIndex: modelIndex.row())
        for index in selectedRows:
            node = self.model_left.getNode(index.row())

            logger.debug(str(node.complexity_type))
            if node.complexity_type in (NodeComplexityType.General, NodeComplexityType.MultiPort):
                ignored_nodes.append(node)
                continue

            if not node in nodes_right:
                self.model_right.appendNode(node)

        if ignored_nodes:
            nodes_str = '<br/>'.join([node.name for node in ignored_nodes])
            QMessageBox.information(self, '无法处理的节点', f'您选中的这些节点： <br/><br/><strong>{nodes_str}</strong><br/><br/> 无法处理，已被忽略！')


    @pyqtSlot()
    def on_btnDeleteFromRight_clicked(self):
        selectedRows = self.selection_right.selectedRows()
        selectedRows = sorted(selectedRows, key=lambda modelIndex: modelIndex.row(), reverse=True)
        for index in selectedRows:
            self.model_right.removeNode(index.row())

    
    @pyqtSlot(QModelIndex, int, int)
    def on_model_right_rowsChanged(self, parent, first, last) -> None:
        has_balancer = False
        for node in self.model_right.getNodes():
            if node.complexity_type == NodeComplexityType.Balancer:
                has_balancer = True
                break
        # self.ui.btnQv2rayMultiPort.setEnabled(True) # always enabled (for Balancer or Simple)
        self.ui.btnQv2rayBalancer.setEnabled(not has_balancer)


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


    @pyqtSlot(QModelIndex)
    def on_listViewLeft_doubleClicked(self, index :QModelIndex):
        self.selection_left.select(index, QItemSelectionModel.ClearAndSelect)
        self.on_btnAppendToRight_clicked()
        

    @pyqtSlot(QModelIndex)
    def on_listViewRight_doubleClicked(self, index :QModelIndex):
        self.selection_right.select(index, QItemSelectionModel.ClearAndSelect)
        self.on_btnDeleteFromRight_clicked()


    @pyqtSlot(QKeyEvent)
    def on_listViewRight_keyPress(self, e :QKeyEvent):
        if e.key() == Qt.Key_Delete:
            self.on_btnDeleteFromRight_clicked()


    @pyqtSlot(str)
    def on_editFilter_textChanged(self, text):
        ui = self.ui
        r =  ui.editFilter.text()
        try:
            re.compile(r)
            ui.editFilter.setStyleSheet('color: #1b8c90;')
        except re.error:
            # invalid regular expression
            r = re.escape(r)
            ui.editFilter.setStyleSheet('color: #1e1e1e;')
            return
            
        if r.lower() == r: # case insensitive
            self.node_selector = lambda node : re.search(r, repr(node).lower()) != None
        else: # case sensitive
            self.node_selector = lambda node : re.search(r, repr(node)) != None

        self.populateNodeListLeft()
        if r != '':
            self.on_btnCheckAllLeft_clicked()


    @pyqtSlot()
    def on_editFilter_returnPressed(self):
        self.on_btnAppendToRight_clicked()


    @pyqtSlot()
    def on_btnCheckAllLeft_clicked(self):
        selection = QItemSelection(self.model_left.index(0,0), self.model_left.index(self.model_left.count()-1,0))
        self.selection_left.select(selection, QItemSelectionModel.Select)
        self.ui.btnAppendToRight.setEnabled(True)


    @pyqtSlot()
    def on_btnCheckAllRight_clicked(self):
        selection = QItemSelection(self.model_right.index(0,0), self.model_right.index(self.model_right.count()-1,0))
        self.selection_right.select(selection, QItemSelectionModel.Select)
        self.ui.btnDeleteFromRight.setEnabled(True)


    @pyqtSlot()
    def on_btnUncheckAllLeft_clicked(self):
        self.selection_left.clear()


    @pyqtSlot()
    def on_btnUncheckAllRight_clicked(self):
        self.selection_right.clear()


    @pyqtSlot()
    def on_btnRefreshList_clicked(self):
        gen.load()
        self.model_right.resetNodes()
        current = self.ui.comboGroups.currentIndex()
        self.populateGroupNames()
        if self.ui.comboGroups.count() > current:
            self.ui.comboGroups.setCurrentIndex(current)


    @pyqtSlot()
    def on_btnSettings_clicked(self):
        w = SettingsForm(self)
        if(w.exec() == QDialog.Accepted):
            g_config.update(w.config)
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

        self.on_btnRefreshList_clicked()


    @pyqtSlot()
    def on_btnQv2rayBalancer_clicked(self):
        if len(self.getUserPickedNodes()) <= 0:
            QMessageBox.warning(self, '错误', '请至少选择一个节点。')
            return

        w = Qv2rayBalancerForm(self)
        if(w.exec() == QDialog.Accepted):
            pass
        
        self.on_btnRefreshList_clicked()
