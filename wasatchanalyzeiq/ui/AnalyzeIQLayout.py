# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wasatchanalyzeiq/ui/AnalyzeIQLayout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(496, 302)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.toolButton_acquire = QtGui.QToolButton(self.tab)
        self.toolButton_acquire.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_acquire.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_acquire.setObjectName(_fromUtf8("toolButton_acquire"))
        self.gridLayout.addWidget(self.toolButton_acquire, 4, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.checkBox_laser_enable = QtGui.QCheckBox(self.tab)
        self.checkBox_laser_enable.setObjectName(_fromUtf8("checkBox_laser_enable"))
        self.gridLayout.addWidget(self.checkBox_laser_enable, 1, 1, 1, 1)
        self.spinBox_integration_time = QtGui.QSpinBox(self.tab)
        self.spinBox_integration_time.setMaximum(60000)
        self.spinBox_integration_time.setProperty("value", 100)
        self.spinBox_integration_time.setObjectName(_fromUtf8("spinBox_integration_time"))
        self.gridLayout.addWidget(self.spinBox_integration_time, 2, 1, 1, 1)
        self.label_device_text = QtGui.QLabel(self.tab)
        self.label_device_text.setMinimumSize(QtCore.QSize(0, 0))
        self.label_device_text.setObjectName(_fromUtf8("label_device_text"))
        self.gridLayout.addWidget(self.label_device_text, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("imagery/wasatch_name.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.toolButton_cancel = QtGui.QToolButton(self.tab)
        self.toolButton_cancel.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButton_cancel.setObjectName(_fromUtf8("toolButton_cancel"))
        self.gridLayout.addWidget(self.toolButton_cancel, 4, 3, 1, 1)
        self.lcdNumber_countdown = QtGui.QLCDNumber(self.tab)
        self.lcdNumber_countdown.setProperty("value", 60000.0)
        self.lcdNumber_countdown.setObjectName(_fromUtf8("lcdNumber_countdown"))
        self.gridLayout.addWidget(self.lcdNumber_countdown, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget = QtGui.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 161))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_coeff0 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_coeff0.setObjectName(_fromUtf8("lineEdit_coeff0"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_coeff0)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_coeff1 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_coeff1.setObjectName(_fromUtf8("lineEdit_coeff1"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_coeff1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_coeff2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_coeff2.setObjectName(_fromUtf8("lineEdit_coeff2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_coeff2)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_coeff3 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_coeff3.setObjectName(_fromUtf8("lineEdit_coeff3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_coeff3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.toolButton_acquire.setText(_translate("MainWindow", "Acquire", None))
        self.checkBox_laser_enable.setText(_translate("MainWindow", "Laser Enable", None))
        self.spinBox_integration_time.setSuffix(_translate("MainWindow", " ms", None))
        self.spinBox_integration_time.setPrefix(_translate("MainWindow", "Integration time: ", None))
        self.label_device_text.setText(_translate("MainWindow", "Searching for device...", None))
        self.toolButton_cancel.setText(_translate("MainWindow", "Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main Settings", None))
        self.label_2.setText(_translate("MainWindow", "Coefficient C0:", None))
        self.lineEdit_coeff0.setText(_translate("MainWindow", "778.267", None))
        self.label_3.setText(_translate("MainWindow", "Coefficient C1:", None))
        self.lineEdit_coeff1.setText(_translate("MainWindow", "0.189334", None))
        self.label_4.setText(_translate("MainWindow", "Coefficient C2:", None))
        self.lineEdit_coeff2.setText(_translate("MainWindow", "1.24617e-05", None))
        self.label_5.setText(_translate("MainWindow", "Coefficient C3:", None))
        self.lineEdit_coeff3.setText(_translate("MainWindow", "-3.17627e-08", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Calibration", None))

