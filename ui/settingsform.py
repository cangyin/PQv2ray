
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from .settings import Ui_Settings

from components import *

from pyqtconfig import config, ConfigManager

# hook pyqtconfig to support QRadioButton
config.HOOKS[QRadioButton] = (config._get_QCheckBox, config._set_QCheckBox, config._event_QPushButton)


class SettingsForm(QDialog):
        
    format_fields_help = '''<div style="color: #1e1e1e;">
            <p><strong>可用字段：</strong></p>
            <p><strong>port</strong>: 节点对应的本地端口号；</p>
            <p><strong>node.id</strong>: 节点的ID，由12个随机字母组成；</p>
            <p><strong>node.name</strong>: 节点名；</p>
            <p><strong>node.group</strong>: 节点所在分组名；</p>
            <p><strong>node.group_id</strong>: 节点所在分组的ID；</p>
        </div>'''

    def __init__(self, parent: Optional['QWidget'], flags: Union[Qt.WindowFlags, Qt.WindowType]=Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint) -> None:
        super().__init__(parent=parent, flags=flags)
        
        self.hover_help_current_widget = None

        self.ui = Ui_Settings()
        ui = self.ui
        ui.setupUi(self)

        self.config = deepcopy( g_config )

        # # tab UI
        self.config_mgr_ui = ConfigManager()
        self.config_mgr_ui.set_defaults(self.config['ui'])
        self.config_mgr_ui.add_handlers({
            'application_font_family': ui.fontComboAppFont,
            'application_font_size': ui.spinAppFontSize,
            'node_list_font_family': ui.fontComboListFont,
            'node_list_font_size': ui.spinListFontSize,
            'node_repr_format': ui.editNodeReprFormat,
            'json_highlight': ui.chkJsonHighlight
        })
        # # tab Qv2ray
        self.config_mgr_qv2ray = ConfigManager()
        self.config_mgr_qv2ray.set_defaults(self.config['qv2ray'])
        self.config_mgr_qv2ray.add_handlers({
            'folder': ui.editQvFolder,
            'auto_start_qv2ray': ui.chkAutoStartQv2ray,
        })
        # # tab v2ray
        self.config_mgr_v2ray = ConfigManager()
        self.config_mgr_v2ray.set_defaults(self.config['v2ray'])
        self.config_mgr_v2ray.add_handlers({
            'domainMatcher': ui.comboDomainMatcher,
            'balancer_strategy': ui.comboBalancerStrategy,
            'selector_use_prefixes': ui.chkSelectorPrefix,
            "domainStrategy": ui.comboDomainStrategy,
        })
        # # tab multi-port
        self.config_mgr_mp = ConfigManager()
        self.config_mgr_mp.set_defaults(self.config['multi_port'])
        self.config_mgr_mp.add_handlers({
            'default_port_start': ui.spinDefaultPortStart,
            'default_port_type': ui.comboPortType,
            'inbound_tag_format': ui.editInboundTagFmt,
            'rule_tag_format': ui.editRuleTagFmt,
            'outbound_tag_format': ui.editOutboundTagFmt,
            'mapping_report_template_path': ui.editMappingReportTemplatePath,
            'mapping_report_result_path': ui.editMappingReportResultPath,
            'qv2ray_result_path': ui.editQvComplexConfigResultPath,
            'config_level_v2ray': ui.rbtnProfileLevelV2
        })
        # # tab balancer
        self.config_mgr_bl = ConfigManager()
        self.config_mgr_bl.set_defaults(self.config['balancer'])
        self.config_mgr_bl.add_handlers({
            'outbound_tag_format': ui.editOutboundTagFmt2,
            'qv2ray_result_path': ui.editQvComplexConfigResultPath2,
            'config_level_v2ray': ui.rbtnProfileLevelV2_2
        })
        
        self.setHelpText('')
    
    def setHelpText(self, text):
        self.ui.txtHelp.setText(text)

    def updateInstantHoverHelp(self):
        helps = {
            # tab UI
            'editNodeReprFormat': '''<p>左右两个节点列表中，节点名的显示格式。</p>''' + self.format_fields_help,
            'chkJsonHighlight': '''<p>当选择手动导入Qv2ray节点配置时，输出的JSON结果可以增加语法高亮以增强可读性。</p>''',
            # tab Qv2ray
            'editQvFolder': '''<p>Qv2ray的安装目录。</p>''',
            'editQvconfigFolder': '''<p>如果您没有在Qv2ray中设置配置目录到其他位置，则不需要担心这里。</p>''',
            'chkAutoStartQv2ray': '<p>当您点击“确认生成”按钮且选择自动导入Qv2ray时，操作完成后是否自动启动Qv2ray。</p>',
            # tab v2ray
            'comboDomainMatcher': '''
                    <p><strong>linear</strong>：使用线性匹配算法，默认值；</p>
                    <p><strong>mph</strong>：使用最小完美散列（minimal perfect hash）算法。
                    测试数据约 17 万条，匹配速度提升约 30%，内存占用减少约 15% 。<strong>(v2ray 4.36.1+)</strong></p>
                    <p><a href="#">参见 https://www.v2fly.org/config/routing.html#routingobject</a></p>
                ''',
            'comboBalancerStrategy': '''
                    <p><strong>random</strong>： 从出站中随机选出一个作为最终的出站连接。</p>
                    <p><strong>leastPing</strong>： 根据观测记录选择 HTTPS GET 请求完成时间最快的一个出站连接。<strong>(v2ray 4.38.0+)</strong></p>
                    <p><a href="#">参见 https://www.v2fly.org/config/routing.html#strategyobject</a></p>
                ''',
            'chkSelectorPrefix': '''
                    <p><strong>精简前</strong>：<br/>香港1-V2Ray <br/>香港2-V2Ray <br/>香港3-V2Ray <br/>新加坡01 <br/>新加坡02 <br/>香港HGC01 <br/>香港HGC02 <br/>香港HGC03 </p>
                    <p><strong>精简后</strong>：<br/>香港 <br/>新加坡0 <br/>香港HGC0 </p>
                ''',
            # tab multi-port
            'editInboundTagFmt': '<p>入站标签(inbound tag)格式。</p>' + self.format_fields_help,
            'editOutboundTagFmt': '<p>出站标签(outbound tag)格式。</p>' + self.format_fields_help,
            'editRuleTagFmt': '<p>规则标签(rule tag)格式。</p>' + self.format_fields_help,
            'groupBoxMappingReport': '生成多端口节点配置后，会导出一份端口与对应出站节点的映射报告。',
            'editMappingReportTemplatePath': '这里选择生成报告的模板。',
            'editMappingReportResultPath': '这里选择生成报告的位置。',
            'editQvComplexConfigResultPath': '这里选择多端口节点配置文件的保存位置。',
            'rbtnProfileLevelQv': '生成的节点配置可导入Qv2ray，通过Qv2ray的GUI使用。',
            'rbtnProfileLevelV2': '生成的节点配置可直接提供给v2ray，命令行使用。节点配置文件的路径设置参见上方。',
            # tab balancer
            'editOutboundTagFmt2': '''
                    <p>出站标签(outbound tag)格式。</p>
                    <div style="color: #1e1e1e;">
                    <p><strong>可用字段：</strong></p>
                    <p><strong>node.id</strong>: 节点的ID，由12个随机字母组成；</p>
                    <p><strong>node.name</strong>: 节点名；</p>
                    <p><strong>node.group</strong>: 节点所在分组名；</p>
                    <p><strong>node.group_id</strong>: 节点所在分组的ID；</p>
                    </div>
                ''',
            'editQvComplexConfigResultPath2': '这里选择负载均衡节点配置文件的保存位置。',
            'rbtnProfileLevelQv_2': '生成的节点配置可导入Qv2ray，通过Qv2ray的GUI使用。',
            'rbtnProfileLevelV2_2': '生成的节点配置可直接提供给v2ray，命令行使用。节点配置文件的路径设置参见上方。',
            
        }
        w = QApplication.widgetAt(QCursor.pos())
        if w :
            if w == self.hover_help_current_widget:
                return
            else:
                self.hover_help_current_widget = w
            help_text = helps.get(w.objectName(), '')
            if help_text:
               self.setHelpText(help_text)

    def event(self, a0: QEvent) -> bool:
        self.updateInstantHoverHelp()
        return super().event(a0)

    @pyqtSlot()
    def on_btnSave_clicked(self):
        self.config['ui'] = self.config_mgr_ui.as_dict()
        self.config['qv2ray'] = self.config_mgr_qv2ray.as_dict()
        self.config['v2ray'] = self.config_mgr_v2ray.as_dict()
        self.config['multi_port'] = self.config_mgr_mp.as_dict()
        self.config['balancer'] = self.config_mgr_bl.as_dict()

        self.accept()

    @pyqtSlot()
    def on_btnCancel_clicked(self):
        self.reject()

    @pyqtSlot(int)
    def on_tabWidgetSettings_currentChanged(self, index):
        self.setHelpText('')
        # about
        self.ui.groupBoxHelp.setVisible(index != self.ui.tabWidgetSettings.count() - 1)

    # tab 2, Qv2ray

    @pyqtSlot(str)
    def on_editQvFolder_textChanged(self, text :str):
        valid = self.parent().checkQv2rayFolder(text)
        if not valid: # uncheck on invalid only
            self.ui.chkAutoStartQv2ray.setChecked(False)
        self.ui.chkAutoStartQv2ray.setEnabled(valid)            

    @pyqtSlot()
    def on_btnBrwsQvFolder_clicked(self):
        ui = self.ui
        qv2ray_folder = QFileDialog.getExistingDirectory(self, '选择 Qv2ray 文件夹', self.config['qv2ray']['folder'])
        if qv2ray_folder:
            qv2ray_folder = relative_path(qv2ray_folder)
            if self.parent().checkQv2rayFolder(qv2ray_folder):
                ui.editQvFolder.setText(qv2ray_folder)
            else:
                QMessageBox.warning(self, '错误', f'您所选择的文件夹 <br/>{qv2ray_folder}<br/> 看起来不像是 Qv2ray 的根目录。')

    # tab 3

    @pyqtSlot()
    def on_btnBrwsMappingReportTemplPath_clicked(self):
        file_name = QFileDialog.getOpenFileName(self, '选择用于导出端口映射信息的模板文件', 'templates', 'JSON 文件 (*.json);; 任何文件 (*.*)')[0]
        if file_name:
            file_name = relative_path(file_name)
            self.ui.editMappingReportTemplatePath.setText(file_name)

    @pyqtSlot()
    def on_btnBrwsMappingReportResultPath_clicked(self):
        file_name = QFileDialog.getSaveFileName(self, '选择端口映射信息的导出路径', 'results', 'JSON 文件 (*.json);; 任何文件 (*.*)')[0]
        if file_name:
            file_name = relative_path(file_name)
            self.ui.editMappingReportResultPath.setText(file_name)

    @pyqtSlot()
    def on_btnBrwsQvResultPath_clicked(self):
        file_name = QFileDialog.getSaveFileName(self, '选择生成 Qv2ray 复杂配置文件的路径', 'results', 'JSON 文件 (*.json);; 任何文件 (*.*)')[0]
        if file_name:
            file_name = relative_path(file_name)
            self.ui.editQvComplexConfigResultPath.setText(file_name)

    @pyqtSlot()
    def on_btnBrwsSoResultPath_clicked(self):
        file_name = QFileDialog.getSaveFileName(self, '选择生成 SwitchyOmega 配置文件的路径', 'results', 'BAK 后缀的文件 (*.bak);; 任何文件 (*.*)')[0]
        if file_name:
            file_name = relative_path(file_name)
            self.ui.editSoResultPath.setText(file_name)

    @pyqtSlot()
    def on_btnAboutQt_clicked(self):
        QMessageBox.aboutQt(self)
    