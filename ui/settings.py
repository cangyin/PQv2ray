# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\PQv2ray\ui\settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(908, 686)
        self.gridLayout_8 = QtWidgets.QGridLayout(Settings)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSave = QtWidgets.QPushButton(Settings)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnCancel = QtWidgets.QPushButton(Settings)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.gridLayout_8.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.groupBoxHelp = QtWidgets.QGroupBox(Settings)
        self.groupBoxHelp.setObjectName("groupBoxHelp")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxHelp)
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtHelp = QtWidgets.QTextEdit(self.groupBoxHelp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtHelp.sizePolicy().hasHeightForWidth())
        self.txtHelp.setSizePolicy(sizePolicy)
        self.txtHelp.setReadOnly(True)
        self.txtHelp.setObjectName("txtHelp")
        self.verticalLayout.addWidget(self.txtHelp)
        self.gridLayout_8.addWidget(self.groupBoxHelp, 0, 1, 1, 1)
        self.tabWidgetSettings = QtWidgets.QTabWidget(Settings)
        self.tabWidgetSettings.setObjectName("tabWidgetSettings")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_2.setVerticalSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fontComboAppFont = QtWidgets.QFontComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.fontComboAppFont.setCurrentFont(font)
        self.fontComboAppFont.setObjectName("fontComboAppFont")
        self.gridLayout_2.addWidget(self.fontComboAppFont, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.spinAppFontSize = QtWidgets.QSpinBox(self.groupBox)
        self.spinAppFontSize.setMinimum(5)
        self.spinAppFontSize.setMaximum(50)
        self.spinAppFontSize.setSingleStep(2)
        self.spinAppFontSize.setProperty("value", 10)
        self.spinAppFontSize.setObjectName("spinAppFontSize")
        self.gridLayout_2.addWidget(self.spinAppFontSize, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.fontComboListFont = QtWidgets.QFontComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.fontComboListFont.setCurrentFont(font)
        self.fontComboListFont.setObjectName("fontComboListFont")
        self.gridLayout.addWidget(self.fontComboListFont, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.spinListFontSize = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinListFontSize.setMinimum(5)
        self.spinListFontSize.setMaximum(50)
        self.spinListFontSize.setSingleStep(2)
        self.spinListFontSize.setProperty("value", 10)
        self.spinListFontSize.setObjectName("spinListFontSize")
        self.gridLayout.addWidget(self.spinListFontSize, 1, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.editNodeReprFormat = QtWidgets.QLineEdit(self.groupBox_2)
        self.editNodeReprFormat.setObjectName("editNodeReprFormat")
        self.horizontalLayout_9.addWidget(self.editNodeReprFormat)
        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 0, 1, 3)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.chkJsonHighlight = QtWidgets.QCheckBox(self.groupBox_7)
        self.chkJsonHighlight.setObjectName("chkJsonHighlight")
        self.verticalLayout_9.addWidget(self.chkJsonHighlight)
        self.verticalLayout_2.addWidget(self.groupBox_7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.tabWidgetSettings.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.chkAutoStartQv2ray = QtWidgets.QCheckBox(self.tab_2)
        self.chkAutoStartQv2ray.setEnabled(False)
        self.chkAutoStartQv2ray.setGeometry(QtCore.QRect(20, 100, 241, 19))
        self.chkAutoStartQv2ray.setObjectName("chkAutoStartQv2ray")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 551, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.editQvFolder = QtWidgets.QLineEdit(self.layoutWidget)
        self.editQvFolder.setObjectName("editQvFolder")
        self.horizontalLayout_8.addWidget(self.editQvFolder)
        self.btnBrwsQvFolder = QtWidgets.QPushButton(self.layoutWidget)
        self.btnBrwsQvFolder.setObjectName("btnBrwsQvFolder")
        self.horizontalLayout_8.addWidget(self.btnBrwsQvFolder)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.tabWidgetSettings.addTab(self.tab_2, "")
        self.tabV2ray = QtWidgets.QWidget()
        self.tabV2ray.setObjectName("tabV2ray")
        self.groupBoxV2rayAdvanced = QtWidgets.QGroupBox(self.tabV2ray)
        self.groupBoxV2rayAdvanced.setGeometry(QtCore.QRect(20, 40, 541, 261))
        self.groupBoxV2rayAdvanced.setObjectName("groupBoxV2rayAdvanced")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBoxV2rayAdvanced)
        self.gridLayout_6.setSpacing(12)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_11 = QtWidgets.QLabel(self.groupBoxV2rayAdvanced)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1)
        self.comboDomainStrategy = QtWidgets.QComboBox(self.groupBoxV2rayAdvanced)
        self.comboDomainStrategy.setObjectName("comboDomainStrategy")
        self.comboDomainStrategy.addItem("")
        self.comboDomainStrategy.addItem("")
        self.comboDomainStrategy.addItem("")
        self.gridLayout_6.addWidget(self.comboDomainStrategy, 2, 1, 1, 1)
        self.comboBalancerStrategy = QtWidgets.QComboBox(self.groupBoxV2rayAdvanced)
        self.comboBalancerStrategy.setObjectName("comboBalancerStrategy")
        self.comboBalancerStrategy.addItem("")
        self.comboBalancerStrategy.addItem("")
        self.gridLayout_6.addWidget(self.comboBalancerStrategy, 1, 1, 1, 1)
        self.comboDomainMatcher = QtWidgets.QComboBox(self.groupBoxV2rayAdvanced)
        self.comboDomainMatcher.setObjectName("comboDomainMatcher")
        self.comboDomainMatcher.addItem("")
        self.comboDomainMatcher.addItem("")
        self.gridLayout_6.addWidget(self.comboDomainMatcher, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBoxV2rayAdvanced)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBoxV2rayAdvanced)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 2, 2, 1, 1)
        self.chkSelectorPrefix = QtWidgets.QCheckBox(self.groupBoxV2rayAdvanced)
        self.chkSelectorPrefix.setObjectName("chkSelectorPrefix")
        self.gridLayout_6.addWidget(self.chkSelectorPrefix, 1, 2, 1, 1)
        self.tabWidgetSettings.addTab(self.tabV2ray, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_9.setContentsMargins(-1, 18, -1, -1)
        self.gridLayout_9.setHorizontalSpacing(8)
        self.gridLayout_9.setVerticalSpacing(12)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.spinDefaultPortStart = QtWidgets.QSpinBox(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinDefaultPortStart.sizePolicy().hasHeightForWidth())
        self.spinDefaultPortStart.setSizePolicy(sizePolicy)
        self.spinDefaultPortStart.setMinimum(1024)
        self.spinDefaultPortStart.setMaximum(65535)
        self.spinDefaultPortStart.setObjectName("spinDefaultPortStart")
        self.gridLayout_9.addWidget(self.spinDefaultPortStart, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_8)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_9.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_8)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_9.addWidget(self.label_14, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem5, 0, 2, 1, 1)
        self.comboPortType = QtWidgets.QComboBox(self.groupBox_8)
        self.comboPortType.setObjectName("comboPortType")
        self.comboPortType.addItem("")
        self.comboPortType.addItem("")
        self.gridLayout_9.addWidget(self.comboPortType, 1, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_8)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setContentsMargins(-1, 16, -1, -1)
        self.gridLayout_3.setHorizontalSpacing(12)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.editInboundTagFmt = QtWidgets.QLineEdit(self.groupBox_4)
        self.editInboundTagFmt.setObjectName("editInboundTagFmt")
        self.gridLayout_3.addWidget(self.editInboundTagFmt, 0, 1, 1, 1)
        self.editRuleTagFmt = QtWidgets.QLineEdit(self.groupBox_4)
        self.editRuleTagFmt.setObjectName("editRuleTagFmt")
        self.gridLayout_3.addWidget(self.editRuleTagFmt, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.editOutboundTagFmt = QtWidgets.QLineEdit(self.groupBox_4)
        self.editOutboundTagFmt.setObjectName("editOutboundTagFmt")
        self.gridLayout_3.addWidget(self.editOutboundTagFmt, 3, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.groupBoxMappingReport = QtWidgets.QGroupBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxMappingReport.sizePolicy().hasHeightForWidth())
        self.groupBoxMappingReport.setSizePolicy(sizePolicy)
        self.groupBoxMappingReport.setObjectName("groupBoxMappingReport")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxMappingReport)
        self.gridLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_4.setVerticalSpacing(12)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.groupBoxMappingReport)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.editMappingReportTemplatePath = QtWidgets.QLineEdit(self.groupBoxMappingReport)
        self.editMappingReportTemplatePath.setObjectName("editMappingReportTemplatePath")
        self.gridLayout_4.addWidget(self.editMappingReportTemplatePath, 0, 1, 1, 1)
        self.btnBrwsMappingReportTemplPath = QtWidgets.QPushButton(self.groupBoxMappingReport)
        self.btnBrwsMappingReportTemplPath.setObjectName("btnBrwsMappingReportTemplPath")
        self.gridLayout_4.addWidget(self.btnBrwsMappingReportTemplPath, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBoxMappingReport)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.editMappingReportResultPath = QtWidgets.QLineEdit(self.groupBoxMappingReport)
        self.editMappingReportResultPath.setObjectName("editMappingReportResultPath")
        self.gridLayout_4.addWidget(self.editMappingReportResultPath, 1, 1, 1, 1)
        self.btnBrwsMappingReportResultPath = QtWidgets.QPushButton(self.groupBoxMappingReport)
        self.btnBrwsMappingReportResultPath.setObjectName("btnBrwsMappingReportResultPath")
        self.gridLayout_4.addWidget(self.btnBrwsMappingReportResultPath, 1, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBoxMappingReport)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setContentsMargins(-1, 16, -1, -1)
        self.gridLayout_7.setVerticalSpacing(14)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.editQvComplexConfigResultPath = QtWidgets.QLineEdit(self.groupBox_6)
        self.editQvComplexConfigResultPath.setObjectName("editQvComplexConfigResultPath")
        self.horizontalLayout_6.addWidget(self.editQvComplexConfigResultPath)
        self.btnBrwsQvResultPath = QtWidgets.QPushButton(self.groupBox_6)
        self.btnBrwsQvResultPath.setObjectName("btnBrwsQvResultPath")
        self.horizontalLayout_6.addWidget(self.btnBrwsQvResultPath)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.gridLayout_7.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_6)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.rbtnProfileLevelQv = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtnProfileLevelQv.setChecked(True)
        self.rbtnProfileLevelQv.setObjectName("rbtnProfileLevelQv")
        self.horizontalLayout_2.addWidget(self.rbtnProfileLevelQv)
        self.rbtnProfileLevelV2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtnProfileLevelV2.setObjectName("rbtnProfileLevelV2")
        self.horizontalLayout_2.addWidget(self.rbtnProfileLevelV2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.tabWidgetSettings.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 30, 541, 101))
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_20 = QtWidgets.QLabel(self.groupBox_10)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_11.addWidget(self.label_20, 0, 0, 1, 1)
        self.editOutboundTagFmt2 = QtWidgets.QLineEdit(self.groupBox_10)
        self.editOutboundTagFmt2.setObjectName("editOutboundTagFmt2")
        self.gridLayout_11.addWidget(self.editOutboundTagFmt2, 0, 1, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_11.setGeometry(QtCore.QRect(20, 170, 541, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_10.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_19 = QtWidgets.QLabel(self.groupBox_11)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_11.addWidget(self.label_19)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.editQvComplexConfigResultPath2 = QtWidgets.QLineEdit(self.groupBox_11)
        self.editQvComplexConfigResultPath2.setObjectName("editQvComplexConfigResultPath2")
        self.horizontalLayout_11.addWidget(self.editQvComplexConfigResultPath2)
        self.btnBrwsQvResultPath2 = QtWidgets.QPushButton(self.groupBox_11)
        self.btnBrwsQvResultPath2.setObjectName("btnBrwsQvResultPath2")
        self.horizontalLayout_11.addWidget(self.btnBrwsQvResultPath2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 310, 541, 51))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_3.addWidget(self.label_21)
        self.rbtnProfileLevelQv_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.rbtnProfileLevelQv_2.setChecked(True)
        self.rbtnProfileLevelQv_2.setObjectName("rbtnProfileLevelQv_2")
        self.horizontalLayout_3.addWidget(self.rbtnProfileLevelQv_2)
        self.rbtnProfileLevelV2_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.rbtnProfileLevelV2_2.setObjectName("rbtnProfileLevelV2_2")
        self.horizontalLayout_3.addWidget(self.rbtnProfileLevelV2_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.tabWidgetSettings.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.labQv2rayIcon = QtWidgets.QLabel(self.tab_5)
        self.labQv2rayIcon.setText("")
        self.labQv2rayIcon.setPixmap(QtGui.QPixmap(":/3.ico"))
        self.labQv2rayIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.labQv2rayIcon.setObjectName("labQv2rayIcon")
        self.verticalLayout_12.addWidget(self.labQv2rayIcon)
        self.labThanksQv2ray = QtWidgets.QLabel(self.tab_5)
        self.labThanksQv2ray.setAlignment(QtCore.Qt.AlignCenter)
        self.labThanksQv2ray.setObjectName("labThanksQv2ray")
        self.verticalLayout_12.addWidget(self.labThanksQv2ray)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem8)
        self.btnAboutQt = QtWidgets.QPushButton(self.tab_5)
        self.btnAboutQt.setObjectName("btnAboutQt")
        self.verticalLayout_12.addWidget(self.btnAboutQt)
        self.tabWidgetSettings.addTab(self.tab_5, "")
        self.gridLayout_8.addWidget(self.tabWidgetSettings, 0, 0, 1, 1)

        self.retranslateUi(Settings)
        self.tabWidgetSettings.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "设置"))
        self.btnSave.setText(_translate("Settings", "保存"))
        self.btnCancel.setText(_translate("Settings", "取消"))
        self.groupBoxHelp.setTitle(_translate("Settings", "说明"))
        self.groupBox.setTitle(_translate("Settings", "界面"))
        self.label_4.setText(_translate("Settings", "字号"))
        self.label_3.setText(_translate("Settings", "字体"))
        self.groupBox_2.setTitle(_translate("Settings", "节点列表"))
        self.label_6.setText(_translate("Settings", "字号"))
        self.label_5.setText(_translate("Settings", "字体"))
        self.label_10.setText(_translate("Settings", "节点显示格式"))
        self.groupBox_7.setTitle(_translate("Settings", "其他"))
        self.chkJsonHighlight.setText(_translate("Settings", "JSON 语法高亮"))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tab), _translate("Settings", "外观"))
        self.chkAutoStartQv2ray.setText(_translate("Settings", "自动导入配置后启动Qv2ray"))
        self.label_16.setText(_translate("Settings", "Qv2ray 目录"))
        self.btnBrwsQvFolder.setText(_translate("Settings", "浏览"))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tab_2), _translate("Settings", "Qv2ray"))
        self.groupBoxV2rayAdvanced.setTitle(_translate("Settings", "Advanced"))
        self.label_11.setText(_translate("Settings", "域名匹配算法"))
        self.comboDomainStrategy.setItemText(0, _translate("Settings", "AsIs"))
        self.comboDomainStrategy.setItemText(1, _translate("Settings", "IPIfNonMatch"))
        self.comboDomainStrategy.setItemText(2, _translate("Settings", "IPOnDemand"))
        self.comboBalancerStrategy.setItemText(0, _translate("Settings", "random"))
        self.comboBalancerStrategy.setItemText(1, _translate("Settings", "leastPing"))
        self.comboDomainMatcher.setItemText(0, _translate("Settings", "linear"))
        self.comboDomainMatcher.setItemText(1, _translate("Settings", "mph"))
        self.label_15.setText(_translate("Settings", "负载均衡策略"))
        self.label_17.setText(_translate("Settings", "域名策略"))
        self.chkSelectorPrefix.setText(_translate("Settings", "负载均衡选择器列表精简"))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tabV2ray), _translate("Settings", "v2ray"))
        self.groupBox_8.setTitle(_translate("Settings", "入站端口"))
        self.label_18.setText(_translate("Settings", "类型"))
        self.label_14.setText(_translate("Settings", "默认起始端口"))
        self.comboPortType.setItemText(0, _translate("Settings", "SOCKS5"))
        self.comboPortType.setItemText(1, _translate("Settings", "HTTP"))
        self.groupBox_4.setTitle(_translate("Settings", "标签格式"))
        self.label_7.setText(_translate("Settings", "路由规则标签"))
        self.label_2.setText(_translate("Settings", "入站标签"))
        self.label_8.setText(_translate("Settings", "出站标签"))
        self.groupBoxMappingReport.setTitle(_translate("Settings", "端口映射报告"))
        self.label.setText(_translate("Settings", "模板"))
        self.btnBrwsMappingReportTemplPath.setText(_translate("Settings", "浏览"))
        self.label_9.setText(_translate("Settings", "导出路径"))
        self.btnBrwsMappingReportResultPath.setText(_translate("Settings", "浏览"))
        self.groupBox_6.setTitle(_translate("Settings", "输出路径"))
        self.label_12.setText(_translate("Settings", "为 Qv2ray 生成的复杂配置文件"))
        self.btnBrwsQvResultPath.setText(_translate("Settings", "浏览"))
        self.label_13.setText(_translate("Settings", "配置完整度"))
        self.rbtnProfileLevelQv.setText(_translate("Settings", "Qv2ray"))
        self.rbtnProfileLevelV2.setText(_translate("Settings", "v2ray"))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tab_3), _translate("Settings", "多端口"))
        self.groupBox_10.setTitle(_translate("Settings", "标签格式"))
        self.label_20.setText(_translate("Settings", "出站标签"))
        self.groupBox_11.setTitle(_translate("Settings", "输出路径"))
        self.label_19.setText(_translate("Settings", "为 Qv2ray 生成的复杂配置文件"))
        self.btnBrwsQvResultPath2.setText(_translate("Settings", "浏览"))
        self.label_21.setText(_translate("Settings", "配置完整度"))
        self.rbtnProfileLevelQv_2.setText(_translate("Settings", "Qv2ray"))
        self.rbtnProfileLevelV2_2.setText(_translate("Settings", "v2ray"))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tab_4), _translate("Settings", "负载均衡"))
        self.labThanksQv2ray.setText(_translate("Settings", "Thanks To Qv2ray"))
        self.btnAboutQt.setText(_translate("Settings", "关于 Qt"))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tab_5), _translate("Settings", "关于"))
