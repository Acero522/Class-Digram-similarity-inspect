from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)
import sys
from PyQt5 import QtCore, QtWidgets
import GED
import os
m1='123'
m2='123'
class Example(QWidget):

    def __init__(self):
        super().__init__()

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

    def msg(self, Filepath):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        m1=m
        print(m1)
        self.le.setText(m)

    def msg2(self, Filepath):
        print(m1)
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        m2=m
        print(m2)
        self.le2.setText(m)

    def calculate(self):
        print(m1,m2)
        os.system('python GED.py --g1 ./data/image1_1.gxl --g2 ./data/image1_2.gxl')

        text, ok = QInputDialog.getText(self, 'Input Dialog',
            '路径1:')
        text2,ok=QInputDialog.getText(self, 'Input Dialog',
            '路径2:')
        if ok:
            self.le.setText(m1)
            self.le2.setText(str(text2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())