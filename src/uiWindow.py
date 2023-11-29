# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(693, 487)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.labelPath = QLabel(self.centralwidget)
        self.labelPath.setObjectName(u"labelPath")

        self.horizontalLayout_4.addWidget(self.labelPath)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBoxPath = QGroupBox(self.centralwidget)
        self.groupBoxPath.setObjectName(u"groupBoxPath")
        self.verticalLayout_5 = QVBoxLayout(self.groupBoxPath)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 5, 2, -1)
        self.tabWidget = QTabWidget(self.groupBoxPath)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnChooseFile = QPushButton(self.frame_2)
        self.btnChooseFile.setObjectName(u"btnChooseFile")

        self.horizontalLayout_2.addWidget(self.btnChooseFile)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnChooseFolder = QPushButton(self.frame_3)
        self.btnChooseFolder.setObjectName(u"btnChooseFolder")

        self.horizontalLayout_3.addWidget(self.btnChooseFolder)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cbTxtFile = QCheckBox(self.groupBox)
        self.cbTxtFile.setObjectName(u"cbTxtFile")

        self.gridLayout_3.addWidget(self.cbTxtFile, 1, 1, 1, 1)

        self.cbJavaFile = QCheckBox(self.groupBox)
        self.cbJavaFile.setObjectName(u"cbJavaFile")

        self.gridLayout_3.addWidget(self.cbJavaFile, 1, 3, 1, 1)

        self.cbCppFile = QCheckBox(self.groupBox)
        self.cbCppFile.setObjectName(u"cbCppFile")
        self.cbCppFile.setChecked(True)

        self.gridLayout_3.addWidget(self.cbCppFile, 0, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_3, 8, 0, 1, 4)

        self.cbCFile = QCheckBox(self.groupBox)
        self.cbCFile.setObjectName(u"cbCFile")
        self.cbCFile.setChecked(True)

        self.gridLayout_3.addWidget(self.cbCFile, 0, 0, 1, 1)

        self.cbBatFile = QCheckBox(self.groupBox)
        self.cbBatFile.setObjectName(u"cbBatFile")

        self.gridLayout_3.addWidget(self.cbBatFile, 1, 0, 1, 1)

        self.cbPyFile = QCheckBox(self.groupBox)
        self.cbPyFile.setObjectName(u"cbPyFile")

        self.gridLayout_3.addWidget(self.cbPyFile, 1, 2, 1, 1)

        self.cbMFile = QCheckBox(self.groupBox)
        self.cbMFile.setObjectName(u"cbMFile")

        self.gridLayout_3.addWidget(self.cbMFile, 2, 0, 1, 1)

        self.cbHFile = QCheckBox(self.groupBox)
        self.cbHFile.setObjectName(u"cbHFile")
        self.cbHFile.setChecked(True)

        self.gridLayout_3.addWidget(self.cbHFile, 0, 1, 1, 1)

        self.cbHppFile = QCheckBox(self.groupBox)
        self.cbHppFile.setObjectName(u"cbHppFile")
        self.cbHppFile.setChecked(True)

        self.gridLayout_3.addWidget(self.cbHppFile, 0, 3, 1, 1)

        self.leditCustomEncode = QLineEdit(self.groupBox)
        self.leditCustomEncode.setObjectName(u"leditCustomEncode")

        self.gridLayout_3.addWidget(self.leditCustomEncode, 6, 0, 1, 2)

        self.btnCustomCheck = QPushButton(self.groupBox)
        self.btnCustomCheck.setObjectName(u"btnCustomCheck")

        self.gridLayout_3.addWidget(self.btnCustomCheck, 6, 2, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 5, 0, 1, 4)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_5.addWidget(self.tabWidget)


        self.verticalLayout_9.addWidget(self.groupBoxPath)

        self.groupBoxEncode = QGroupBox(self.centralwidget)
        self.groupBoxEncode.setObjectName(u"groupBoxEncode")
        self.verticalLayout_6 = QVBoxLayout(self.groupBoxEncode)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBoxEncode)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")
        self.label_4.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.comboBox = QComboBox(self.groupBoxEncode)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_5.addWidget(self.comboBox)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_9.addWidget(self.groupBoxEncode)


        self.horizontalLayout.addLayout(self.verticalLayout_9)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnTransmit = QPushButton(self.centralwidget)
        self.btnTransmit.setObjectName(u"btnTransmit")

        self.horizontalLayout_6.addWidget(self.btnTransmit)

        self.btnClear = QPushButton(self.centralwidget)
        self.btnClear.setObjectName(u"btnClear")

        self.horizontalLayout_6.addWidget(self.btnClear)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.verticalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u8f6c\u6362\u5de5\u5177V1.0.0(2020.03.16)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8def\u5f84:", None))
        self.labelPath.setText("")
        self.groupBoxPath.setTitle(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u8bbe\u7f6e", None))
        self.btnChooseFile.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.btnChooseFolder.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u9012\u5f52\u5904\u7406\u6587\u4ef6\u5939\u4e2d\u4ee5\u4e0b\u7c7b\u578b", None))
        self.cbTxtFile.setText(QCoreApplication.translate("MainWindow", u".txt", None))
        self.cbJavaFile.setText(QCoreApplication.translate("MainWindow", u".java", None))
        self.cbCppFile.setText(QCoreApplication.translate("MainWindow", u".cpp", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5982\u679c\u81ea\u5b9a\u4e49\u591a\u79cd\u6587\u4ef6\u7c7b\u578b\uff0c\u4e0d\u540c\u7c7b\u578b\u4e4b\u95f4\u7528\u7a7a\u683c\u5206\u5f00\uff0c\u5982\uff1a.html .xml", None))
        self.cbCFile.setText(QCoreApplication.translate("MainWindow", u".c", None))
        self.cbBatFile.setText(QCoreApplication.translate("MainWindow", u".bat", None))
        self.cbPyFile.setText(QCoreApplication.translate("MainWindow", u".py", None))
        self.cbMFile.setText(QCoreApplication.translate("MainWindow", u".m", None))
        self.cbHFile.setText(QCoreApplication.translate("MainWindow", u".h", None))
        self.cbHppFile.setText(QCoreApplication.translate("MainWindow", u".hpp", None))
        self.btnCustomCheck.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u7528", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u7c7b\u578b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.groupBoxEncode.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u8bbe\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362\u540e\u7684\u7f16\u7801:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"UTF-8 BOM", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"UTF-8", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"GB2312", None))

        self.btnTransmit.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u5c4f", None))
    # retranslateUi

