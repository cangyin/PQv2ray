# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\PQv2ray\ui\qv2ray_balancer.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Qv2rayBalancerForm(object):
    def setupUi(self, Qv2rayBalancerForm):
        Qv2rayBalancerForm.setObjectName("Qv2rayBalancerForm")
        Qv2rayBalancerForm.resize(871, 557)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Qv2rayBalancerForm.sizePolicy().hasHeightForWidth())
        Qv2rayBalancerForm.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(Qv2rayBalancerForm)
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.inputGroup = QtWidgets.QGroupBox(Qv2rayBalancerForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputGroup.sizePolicy().hasHeightForWidth())
        self.inputGroup.setSizePolicy(sizePolicy)
        self.inputGroup.setObjectName("inputGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.inputGroup)
        self.gridLayout.setContentsMargins(-1, 20, -1, 12)
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.inputGroup)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.inputGroup)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chkHttpPort = QtWidgets.QCheckBox(self.inputGroup)
        self.chkHttpPort.setObjectName("chkHttpPort")
        self.horizontalLayout_4.addWidget(self.chkHttpPort)
        self.spinHttpPort = QtWidgets.QSpinBox(self.inputGroup)
        self.spinHttpPort.setEnabled(False)
        self.spinHttpPort.setMinimum(1024)
        self.spinHttpPort.setMaximum(65535)
        self.spinHttpPort.setProperty("value", 1081)
        self.spinHttpPort.setObjectName("spinHttpPort")
        self.horizontalLayout_4.addWidget(self.spinHttpPort)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.chkSocksPort = QtWidgets.QCheckBox(self.inputGroup)
        self.chkSocksPort.setObjectName("chkSocksPort")
        self.horizontalLayout_5.addWidget(self.chkSocksPort)
        self.spinSocksPort = QtWidgets.QSpinBox(self.inputGroup)
        self.spinSocksPort.setEnabled(False)
        self.spinSocksPort.setMinimum(1024)
        self.spinSocksPort.setMaximum(65535)
        self.spinSocksPort.setObjectName("spinSocksPort")
        self.horizontalLayout_5.addWidget(self.spinSocksPort)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.editListenIp = QtWidgets.QLineEdit(self.inputGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editListenIp.sizePolicy().hasHeightForWidth())
        self.editListenIp.setSizePolicy(sizePolicy)
        self.editListenIp.setObjectName("editListenIp")
        self.gridLayout.addWidget(self.editListenIp, 0, 1, 1, 2)
        self.gridLayout_2.addWidget(self.inputGroup, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Qv2rayBalancerForm)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(16)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6, 0, QtCore.Qt.AlignLeft)
        self.comboFallbackOutboundGroup = QtWidgets.QComboBox(self.groupBox_2)
        self.comboFallbackOutboundGroup.setMinimumSize(QtCore.QSize(150, 0))
        self.comboFallbackOutboundGroup.setObjectName("comboFallbackOutboundGroup")
        self.horizontalLayout_6.addWidget(self.comboFallbackOutboundGroup, 0, QtCore.Qt.AlignLeft)
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widgetFallBackNode = QtWidgets.QWidget(self.widget)
        self.widgetFallBackNode.setObjectName("widgetFallBackNode")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widgetFallBackNode)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.widgetFallBackNode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.comboFallbackOutboundNode = QLinkedNodeComboBox(self.widgetFallBackNode)
        self.comboFallbackOutboundNode.setObjectName("comboFallbackOutboundNode")
        self.horizontalLayout_9.addWidget(self.comboFallbackOutboundNode)
        self.verticalLayout_6.addWidget(self.widgetFallBackNode)
        spacerItem1 = QtWidgets.QSpacerItem(337, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_6.addWidget(self.widget)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 4, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chkBypassCN = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkBypassCN.setObjectName("chkBypassCN")
        self.horizontalLayout_2.addWidget(self.chkBypassCN)
        self.chkBypassLAN = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkBypassLAN.setObjectName("chkBypassLAN")
        self.horizontalLayout_2.addWidget(self.chkBypassLAN)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rbtnNoRouteSettings = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbtnNoRouteSettings.setChecked(False)
        self.rbtnNoRouteSettings.setObjectName("rbtnNoRouteSettings")
        self.verticalLayout_4.addWidget(self.rbtnNoRouteSettings)
        self.rbtnUseQvRouteSettings = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbtnUseQvRouteSettings.setChecked(True)
        self.rbtnUseQvRouteSettings.setObjectName("rbtnUseQvRouteSettings")
        self.verticalLayout_4.addWidget(self.rbtnUseQvRouteSettings)
        self.rbtnImportQvRouteSettings = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbtnImportQvRouteSettings.setObjectName("rbtnImportQvRouteSettings")
        self.verticalLayout_4.addWidget(self.rbtnImportQvRouteSettings)
        self.widgetQvExportedRouteBrwsPane = QtWidgets.QWidget(self.groupBox_2)
        self.widgetQvExportedRouteBrwsPane.setEnabled(False)
        self.widgetQvExportedRouteBrwsPane.setObjectName("widgetQvExportedRouteBrwsPane")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetQvExportedRouteBrwsPane)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 8)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editQvExportedRouteSettings = QtWidgets.QLineEdit(self.widgetQvExportedRouteBrwsPane)
        self.editQvExportedRouteSettings.setObjectName("editQvExportedRouteSettings")
        self.horizontalLayout.addWidget(self.editQvExportedRouteSettings)
        self.btnBrwsQvExportedRouteSettings = QtWidgets.QPushButton(self.widgetQvExportedRouteBrwsPane)
        self.btnBrwsQvExportedRouteSettings.setObjectName("btnBrwsQvExportedRouteSettings")
        self.horizontalLayout.addWidget(self.btnBrwsQvExportedRouteSettings)
        self.verticalLayout_4.addWidget(self.widgetQvExportedRouteBrwsPane)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.groupBoxRouteTypeOrder = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxRouteTypeOrder.sizePolicy().hasHeightForWidth())
        self.groupBoxRouteTypeOrder.setSizePolicy(sizePolicy)
        self.groupBoxRouteTypeOrder.setTitle("")
        self.groupBoxRouteTypeOrder.setObjectName("groupBoxRouteTypeOrder")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxRouteTypeOrder)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labHintDragRules = QtWidgets.QLabel(self.groupBoxRouteTypeOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labHintDragRules.sizePolicy().hasHeightForWidth())
        self.labHintDragRules.setSizePolicy(sizePolicy)
        self.labHintDragRules.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labHintDragRules.setObjectName("labHintDragRules")
        self.verticalLayout_3.addWidget(self.labHintDragRules)
        self.listRouteTypes = QtWidgets.QListWidget(self.groupBoxRouteTypeOrder)
        self.listRouteTypes.setMaximumSize(QtCore.QSize(120, 100))
        self.listRouteTypes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listRouteTypes.setDragEnabled(True)
        self.listRouteTypes.setDragDropOverwriteMode(False)
        self.listRouteTypes.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listRouteTypes.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listRouteTypes.setObjectName("listRouteTypes")
        self.verticalLayout_3.addWidget(self.listRouteTypes)
        self.gridLayout_3.addWidget(self.groupBoxRouteTypeOrder, 0, 1, 3, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.btnCommit = QtWidgets.QPushButton(Qv2rayBalancerForm)
        self.btnCommit.setObjectName("btnCommit")
        self.gridLayout_2.addWidget(self.btnCommit, 2, 1, 1, 1)
        self.groupBoxImport = QtWidgets.QGroupBox(Qv2rayBalancerForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxImport.sizePolicy().hasHeightForWidth())
        self.groupBoxImport.setSizePolicy(sizePolicy)
        self.groupBoxImport.setObjectName("groupBoxImport")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBoxImport)
        self.gridLayout_5.setContentsMargins(-1, 25, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.rbtnUpdateNode = QtWidgets.QRadioButton(self.groupBoxImport)
        self.rbtnUpdateNode.setObjectName("rbtnUpdateNode")
        self.gridLayout_5.addWidget(self.rbtnUpdateNode, 1, 0, 1, 1)
        self.rbtnAutoImport = QtWidgets.QRadioButton(self.groupBoxImport)
        self.rbtnAutoImport.setObjectName("rbtnAutoImport")
        self.gridLayout_5.addWidget(self.rbtnAutoImport, 0, 0, 1, 1)
        self.rbtnManualImport = QtWidgets.QRadioButton(self.groupBoxImport)
        self.rbtnManualImport.setChecked(True)
        self.rbtnManualImport.setObjectName("rbtnManualImport")
        self.gridLayout_5.addWidget(self.rbtnManualImport, 2, 0, 1, 1)
        self.importSettingStack = QtWidgets.QStackedWidget(self.groupBoxImport)
        self.importSettingStack.setEnabled(False)
        self.importSettingStack.setObjectName("importSettingStack")
        self.autoImportSettingPane = QtWidgets.QWidget()
        self.autoImportSettingPane.setObjectName("autoImportSettingPane")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.autoImportSettingPane)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboAutoImportGroup = QtWidgets.QComboBox(self.autoImportSettingPane)
        self.comboAutoImportGroup.setMinimumSize(QtCore.QSize(150, 0))
        self.comboAutoImportGroup.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboAutoImportGroup.setObjectName("comboAutoImportGroup")
        self.horizontalLayout_7.addWidget(self.comboAutoImportGroup)
        self.label_21 = QtWidgets.QLabel(self.autoImportSettingPane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_7.addWidget(self.label_21)
        self.editAutoImportName = QtWidgets.QLineEdit(self.autoImportSettingPane)
        self.editAutoImportName.setMinimumSize(QtCore.QSize(200, 0))
        self.editAutoImportName.setObjectName("editAutoImportName")
        self.horizontalLayout_7.addWidget(self.editAutoImportName)
        self.importSettingStack.addWidget(self.autoImportSettingPane)
        self.updateImportSettingPane = QtWidgets.QWidget()
        self.updateImportSettingPane.setObjectName("updateImportSettingPane")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.updateImportSettingPane)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboUpdateNodeGroup = QtWidgets.QComboBox(self.updateImportSettingPane)
        self.comboUpdateNodeGroup.setMinimumSize(QtCore.QSize(150, 0))
        self.comboUpdateNodeGroup.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboUpdateNodeGroup.setObjectName("comboUpdateNodeGroup")
        self.horizontalLayout_3.addWidget(self.comboUpdateNodeGroup)
        self.label_22 = QtWidgets.QLabel(self.updateImportSettingPane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_3.addWidget(self.label_22)
        self.comboUpdateNodeName = QLinkedNodeComboBox(self.updateImportSettingPane)
        self.comboUpdateNodeName.setMinimumSize(QtCore.QSize(200, 0))
        self.comboUpdateNodeName.setObjectName("comboUpdateNodeName")
        self.horizontalLayout_3.addWidget(self.comboUpdateNodeName)
        self.importSettingStack.addWidget(self.updateImportSettingPane)
        self.gridLayout_5.addWidget(self.importSettingStack, 0, 1, 2, 1)
        self.gridLayout_2.addWidget(self.groupBoxImport, 2, 0, 1, 1)

        self.retranslateUi(Qv2rayBalancerForm)
        self.importSettingStack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Qv2rayBalancerForm)

    def retranslateUi(self, Qv2rayBalancerForm):
        _translate = QtCore.QCoreApplication.translate
        Qv2rayBalancerForm.setWindowTitle(_translate("Qv2rayBalancerForm", "Qv2ray 多节点负载均衡配置"))
        self.inputGroup.setTitle(_translate("Qv2rayBalancerForm", "入站设置"))
        self.label.setText(_translate("Qv2rayBalancerForm", "监听地址"))
        self.label_3.setText(_translate("Qv2rayBalancerForm", "端口类型"))
        self.chkHttpPort.setText(_translate("Qv2rayBalancerForm", "HTTP端口"))
        self.chkSocksPort.setText(_translate("Qv2rayBalancerForm", "SOCKS5端口"))
        self.groupBox_2.setTitle(_translate("Qv2rayBalancerForm", "路由"))
        self.label_6.setText(_translate("Qv2rayBalancerForm", "默认出站节点"))
        self.label_9.setText(_translate("Qv2rayBalancerForm", "-"))
        self.chkBypassCN.setText(_translate("Qv2rayBalancerForm", "绕过大陆"))
        self.chkBypassLAN.setText(_translate("Qv2rayBalancerForm", "绕过私有地址"))
        self.rbtnNoRouteSettings.setText(_translate("Qv2rayBalancerForm", "空"))
        self.rbtnUseQvRouteSettings.setText(_translate("Qv2rayBalancerForm", "使用Qv2ray全局路由"))
        self.rbtnImportQvRouteSettings.setText(_translate("Qv2rayBalancerForm", "使用Qv2ray导出的路由方案"))
        self.btnBrwsQvExportedRouteSettings.setText(_translate("Qv2rayBalancerForm", "浏览"))
        self.labHintDragRules.setText(_translate("Qv2rayBalancerForm", "<html><head/><body><p>拖放以调整<br/>规则顺序</p></body></html>"))
        self.btnCommit.setText(_translate("Qv2rayBalancerForm", "确认生成"))
        self.groupBoxImport.setTitle(_translate("Qv2rayBalancerForm", "导入Qv2ray"))
        self.rbtnUpdateNode.setText(_translate("Qv2rayBalancerForm", "更新已有节点"))
        self.rbtnAutoImport.setText(_translate("Qv2rayBalancerForm", "导入为新节点"))
        self.rbtnManualImport.setText(_translate("Qv2rayBalancerForm", "手动"))
        self.label_21.setText(_translate("Qv2rayBalancerForm", "-"))
        self.label_22.setText(_translate("Qv2rayBalancerForm", "-"))
from ui.qlinkednodecombobox import QLinkedNodeComboBox
