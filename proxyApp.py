################################################
################################################
################################################
#########*******###*******####**********########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**********########
########**#####**#**#####**###**################
########**#####**#**#####**###**################
########**######***######**###**################
########**###############**###**################
########**###############**###**################
################################################
########Copyright © Maresal Programming#########
################################################

from PyQt5 import QtWidgets
import sys,os
from proxyprgDesign import Ui_MainWindow
import urllib.request


class ProxyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ProxyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.AllDataGeting()
        self.getProxySetting()
        self.lbl()

        self.ui.http_rdb.toggled.connect(self.getProxySetting)
        self.ui.https_rdb.toggled.connect(self.getProxySetting)
        self.ui.socks5_rdb.toggled.connect(self.getProxySetting)
        self.ui.socks4_rdb.toggled.connect(self.getProxySetting)

        self.ui.proxy_btn.clicked.connect(self.updateBtn)

    def getProxySetting(self):
        global protokol
        items = self.ui.groupBox_2.findChildren(QtWidgets.QRadioButton)
        for i in items :
            if i.isChecked():
                protokol = i.text().lower()
                self.getData(i.text().lower())


    def openProxy(self,protocol):
        try :
            list = []
            with open(f"proxys/{protocol.lower()}.txt","r") as file :
                a = file.readlines()
                for i in a :
                    list.append(i.split(":"))
            return list
        except Exception :
            pass
        

    def getData(self,protocol):
        try:
            data = self.openProxy(protocol)
            self.ui.tableWidget.setRowCount(len(data))
            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ("Ip", "Port", "Protokol"))

            rowIndex = 0
            for re in data:
                self.ui.tableWidget.setItem(
                        rowIndex, 0, QtWidgets.QTableWidgetItem(re[0]))
                self.ui.tableWidget.setItem(
                        rowIndex, 1, QtWidgets.QTableWidgetItem(re[1]))
                self.ui.tableWidget.setItem(
                        rowIndex, 2, QtWidgets.QTableWidgetItem(protocol))
                rowIndex += 1
        except Exception :
            pass

    def updateBtn(self):
        self.updateProxy(protokol)

    def updateProxy(self,protokol):
        url = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol="+protokol+"&timeout=10000&country=all"
        urllib.request.urlretrieve(url, f"./proxys/{protokol}.txt")
        QtWidgets.QMessageBox.information(self,"Güncelleme Bildirimi",f"{protokol} proxy listesi güncellendi.")

    def lbl(self):
        self.ui.proxyLogo.setStyleSheet("background-color: transparent; image:url('logo.png');")


    def AllDataGeting(self):
        protokol = ["http","https","socks4","socks5"]
        for i in protokol:
            if os.path.exists(path=f"./proxys/{i}.txt"):
                pass
            else :
                url = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol="+i+"&timeout=10000&country=all"
                urllib.request.urlretrieve(url, f"./proxys/{i}.txt")
                if len(os.listdir("./proxys")) == len(protokol) :            
                    QtWidgets.QMessageBox.information(self,"Bilgilendirme","Eksik dosyalar tespit edildi ve yeniden indirildi.")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    main = ProxyApp()
    main.show()
    app.exit(app.exec_())