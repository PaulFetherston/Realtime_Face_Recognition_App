# -*- coding: utf-8 -*-

import sys


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QMainWindow, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QFont, QIcon
from test_user_form import Ui_user_form
import user_in_test


class UIWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(900, 950)
        MainWindow.setWindowTitle("UIWindow")
        self.centralwidget = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.ToolsBTN = QPushButton('text', self.centralwidget)
        self.ToolsBTN.move(50, 350)
        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiWindow = UIWindow()
        self.uiToolTab = user_in_test.UIToolTab()
        self.startUIWindow()

    def startUIToolTab(self):
        self.uiToolTab.setupUI(self)
        self.uiToolTab.btn_cancel.clicked.connect(self.startUIWindow)
        # self.uiToolTab.btn_submit.clicked.connect(user_in_test.random)
        self.show()

    def startUIWindow(self):
        self.uiWindow.setupUI(self)
        self.uiWindow.ToolsBTN.clicked.connect(self.startUIToolTab)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())