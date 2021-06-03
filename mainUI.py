import webbrowser

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QTextEdit, QApplication, QLabel)
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import os
from PyQt5.QtCore import pyqtSlot, QFileInfo, pyqtSignal, QBuffer, QByteArray, QIODevice, QSize, Qt
from PyQt5.QtGui import QMovie, QPixmap, QIcon, QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.path1 = '123'
        self.path2 = '2134'
        self.initUI()

    def initUI(self):

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 680, 450))
        self.label.setPixmap(QtGui.QPixmap("./asset/hh.jpg"))
        self.setFont(QFont("黑体", 10, True))  #设置字体
        self.btn = QPushButton('calculate', self)
        self.btn.setIcon(QIcon(QPixmap('./asset/计算器.png')))
        self.btn.setStyleSheet(
             '''QPushButton{
                     color:black;
                     font-family:黑体;    
                 }
                 QPushButton:hover{
                     border: 1px solid Gray;
                     background:rgb(255, 255, 255, 90);
                 }
                 QPushButton:pressed{
                     border: 2px solid DarkGray;
                     background:rgb(255, 255, 255, 30);
                 }''')

        self.btn.move(240, 130)
        self.btn.clicked.connect(self.calculate)

        self.btn2 = QPushButton('选择文件1', self)
        self.btn2.setIcon(QIcon(QPixmap('./asset/file.png')))
        self.btn2.clicked.connect(self.msg)
        self.btn2.move(180, 90)

        self.btn3 = QPushButton('选择文件2', self)
        self.btn3.setIcon(QIcon(QPixmap('./asset/file.png')))
        self.btn3.clicked.connect(self.msg2)
        self.btn3.move(300, 90)

        self.btn4 = QPushButton('像素处理', self)
        self.btn4.setIcon(QIcon(QPixmap('./asset/大巴.png')))
        self.btn4.clicked.connect(self.msg3)
        self.btn4.move(100, 320)

        self.le = QLineEdit('文件1', self)
        self.le.move(200, 20)

        self.le2=QLineEdit('文件2', self)
        self.le2.move(200, 50)

        self.lb1 = QLabel("optimal distance", self)
        self.lb1.move(140, 200)
        self.lb1.setStyleSheet(
            '''QLabel{         
                color:white;
                font-family:黑体; }''')

        self.re1 = QLineEdit('计算距离', self)
        self.re1.move(300, 200)
        self.re1.setStyleSheet(
            '''QLineEdit{         
                border:1px solid gray;         
                width:250px;         
                border-radius:10px;         
                padding:2px 4px; }''')

        self.lb2 = QLabel("possable path", self)
        self.lb2.move(140, 250)
        self.lb2.setStyleSheet(
            '''QLabel{         
                color:white;
                font-family:黑体; }''')

        self.re2 = QTextEdit('路径列表', self)
        self.re2.move(300, 250)

        self.setGeometry(1000, 400, 600, 500)
        self.setWindowTitle('哦吼哦吼')
        self.show()

    def msg(self):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./GREC/data")  # 起始路径
        m = m[0]
        self.path1 = m
        self.le.setText(m)

    def msg2(self):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./GREC/data")  # 起始路径
        m = m[0]
        self.path2 = m
        self.le2.setText(m)

    def msg3(self):
        current_path = os.path.abspath("./canvasFilter/index.html")
        webbrowser.open('file:///' + current_path)

    # def msg3(self):
    #     m = QtWidgets.QFileDialog.getOpenFileName(None, "走你", "./canvasFilter/index.html")  # 起始路径
    #     m = m[0]
    #     self.path2 = m
    #     self.le2.setText(m)

    def calculate(self):
        command = 'python GED.py --g1 '+self.path1+' --g2 '+self.path2
        r = os.popen(command)  # 执行该命令
        info = r.readlines()  # 读取命令行的输出到一个list
        print(info)
        opDistance = info[0].split(": ")[1]
        poPath = info[1].split(":  ")[1]
        self.re1.setText(opDistance)
        self.re2.setText(poPath)
        for line in info:  # 按行遍历
            print(line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())