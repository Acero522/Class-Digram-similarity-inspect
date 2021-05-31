from PyQt5 import QtCore, QtGui, QtWidgets
 
from PyQt5.QtGui import QIcon
 
class Ui_mainWindow(object):
 
    def setupUi(self, mainWindow):
 
        mainWindow.setObjectName("mainWindow")
 
        mainWindow.setWindowModality(QtCore.Qt.WindowModal)
 
        mainWindow.resize(624, 511)
 
        self.centralWidget = QtWidgets.QWidget(mainWindow)
 
        self.centralWidget.setObjectName("centralWidget")
 
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
 
        self.pushButton.setGeometry(QtCore.QRect(240, 240,200, 53))
 
        self.pushButton.setObjectName("pushButton")
 
        self.pushButton.setText("一颗数据小白菜")
 
        # self.pushButton.setFlat(True)
 
        self.pushButton.setStyleSheet("background-color: rgb(164, 185, 255);"
 
"border-color: rgb(170, 150, 163);"
 
"font: 75 12pt \"Arial Narrow\";"
 
"color: rgb(126, 255, 46);")
 
        icon = QtGui.QIcon()
 
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
 
        self.pushButton.setIcon(icon)
 
        self.pushButton.setIconSize(QtCore.QSize(50, 80))
 
        self.pushButton.setAutoRepeatDelay(200)
 
        mainWindow.setCentralWidget(self.centralWidget)
 
        self.retranslateUi(mainWindow)
 
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
 
    def retranslateUi(self, mainWindow):
 
        _translate = QtCore.QCoreApplication.translate
 
        mainWindow.setWindowTitle('您好')
 
        mainWindow.setWindowIcon(QIcon('logo.png'))
 
if __name__ == "__main__":
 
    import sys
 
    app = QtWidgets.QApplication(sys.argv)
 
    mainWindow = QtWidgets.QMainWindow()
 
    ui = Ui_mainWindow()
 
    ui.setupUi(mainWindow)
 
    mainWindow.show()
 
    sys.exit(app.exec_())