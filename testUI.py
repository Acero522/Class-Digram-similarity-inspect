from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)
import sys
from PyQt5 import QtCore, QtWidgets
import GED
import os

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.path1='123'
        self.path2='2134'
        self.initUI()


    def initUI(self):

        self.btn = QPushButton('calculate', self)
        self.btn.move(150, 130)
        self.btn.clicked.connect(self.calculate)

        self.btn2 = QPushButton('选择文件1', self)
        self.btn2.clicked.connect(self.msg)
        self.btn2.move(100,90)

        self.btn3 = QPushButton('选择文件2', self)
        self.btn3.clicked.connect(self.msg2)
        self.btn3.move(200, 90)

        self.le = QLineEdit('文件1',self)
        self.le.move(130, 20)

        self.le2=QLineEdit('文件2',self)
        self.le2.move(130,50)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('calculate')
        self.show()

    def msg(self):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./")  # 起始路径
        m = m[0]
        self.path1=m
        self.le.setText(m)


    def msg2(self):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./")  # 起始路径
        m = m[0]
        self.path2=m
        self.le2.setText(m)

    def calculate(self):
        #print(self.path1,self.path2)
        command='python GED.py --g1 '+self.path1+' --g2 '+self.path2
        r = os.popen(command)  # 执行该命令
        info = r.readlines()  # 读取命令行的输出到一个list
        for line in info:  # 按行遍历
            print(line)


if __name__ == '__main__':
    m1 = '123'
    m2 = '123'
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())