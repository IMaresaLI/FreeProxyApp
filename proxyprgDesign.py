# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Batuhan Olgaç\Desktop\proxy Programı\proxyprgDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.proxyLogo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxyLogo.sizePolicy().hasHeightForWidth())
        self.proxyLogo.setSizePolicy(sizePolicy)
        self.proxyLogo.setMinimumSize(QtCore.QSize(0, 50))
        self.proxyLogo.setText("")
        self.proxyLogo.setObjectName("proxyLogo")
        self.verticalLayout.addWidget(self.proxyLogo)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 1, 3, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.http_rdb = QtWidgets.QRadioButton(self.groupBox_2)
        self.http_rdb.setChecked(True)
        self.http_rdb.setObjectName("http_rdb")
        self.horizontalLayout.addWidget(self.http_rdb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.https_rdb = QtWidgets.QRadioButton(self.groupBox_2)
        self.https_rdb.setObjectName("https_rdb")
        self.horizontalLayout.addWidget(self.https_rdb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.socks4_rdb = QtWidgets.QRadioButton(self.groupBox_2)
        self.socks4_rdb.setObjectName("socks4_rdb")
        self.horizontalLayout.addWidget(self.socks4_rdb)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.socks5_rdb = QtWidgets.QRadioButton(self.groupBox_2)
        self.socks5_rdb.setObjectName("socks5_rdb")
        self.horizontalLayout.addWidget(self.socks5_rdb)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 2)
        self.proxy_btn = QtWidgets.QPushButton(self.page)
        self.proxy_btn.setObjectName("proxy_btn")
        self.gridLayout_2.addWidget(self.proxy_btn, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setItalic(True)
        self.statusbar.setFont(font)
        self.statusbar.setToolTip("")
        self.statusbar.setStatusTip("")
        self.statusbar.setWhatsThis("")
        self.statusbar.setAccessibleDescription("")
        self.statusbar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusbar.setStyleSheet("color: rgb(147, 147, 147);")
        self.statusbar.showMessage("Copyright © Maresal PRM".rjust(128))        
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Free Proxy | Maresal PRM"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Protokol Güncelleme"))
        self.http_rdb.setText(_translate("MainWindow", "HTTP"))
        self.https_rdb.setText(_translate("MainWindow", "HTTPS"))
        self.socks4_rdb.setText(_translate("MainWindow", "Socks4"))
        self.socks5_rdb.setText(_translate("MainWindow", "Socks5"))
        self.proxy_btn.setText(_translate("MainWindow", "Güncelle"))
