from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,QTextEdit,QApplication,QLabel)
import sys
from PyQt5 import QtWidgets
import os

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.path1='123'
        self.path2='2134'
        self.initUI()


    def initUI(self):

        self.btn = QPushButton('calculate', self)
        self.btn.move(220, 130)
        self.btn.clicked.connect(self.calculate)

        self.btn2 = QPushButton('选择文件1', self)
        self.btn2.clicked.connect(self.msg)
        self.btn2.move(180,90)

        self.btn3 = QPushButton('选择文件2', self)
        self.btn3.clicked.connect(self.msg2)
        self.btn3.move(280, 90)

        self.le = QLineEdit('文件1',self)
        self.le.move(200, 20)

        self.le2=QLineEdit('文件2',self)
        self.le2.move(200,50)

        self.lb1 = QLabel("optimal distance", self)
        self.lb1.move(140,200)

        self.re1 = QLineEdit('optimal distance', self)
        self.re1.move(280, 200)

        self.lb2 = QLabel("possable path", self)
        self.lb2.move(140, 250)

        self.re2 = QTextEdit('possable path', self)
        self.re2.move(280, 250)

        self.setGeometry(1000, 400, 600, 500)
        self.setWindowTitle('calculate')
        self.show()

    def msg(self):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./GREC/data")  # 起始路径
        m = m[0]
        self.path1=m
        self.le.setText(m)


    def msg2(self):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./GREC/data")  # 起始路径
        m = m[0]
        self.path2=m
        self.le2.setText(m)

    def calculate(self):
        command='python GED.py --g1 '+self.path1+' --g2 '+self.path2
        r = os.popen(command)  # 执行该命令
        info = r.readlines()  # 读取命令行的输出到一个list
        print(info)
        opDistance=info[0].split(": ")[1]
        poPath=info[1].split(":  ")[1]
        self.re1.setText(opDistance)
        self.re2.setText(poPath)
        for line in info:  # 按行遍历
            print(line)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())