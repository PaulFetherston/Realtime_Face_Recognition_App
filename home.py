# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QMainWindow, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QFont, QIcon
from test_user_form import Ui_user_form
import realtime_face_recognition


class Ui_MainWindow(QMainWindow):
    # TODO Comment Code

    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(self)
        self.face_recognition_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_user_btn = QtWidgets.QPushButton(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.center()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)

        self.centralwidget.setObjectName("centralwidget")

        self.face_recognition_btn.setGeometry(QtCore.QRect(250, 140, 261, 27))
        self.face_recognition_btn.setObjectName("face_recognition_btn")
        self.face_recognition_btn.clicked.connect(self.realtime_face_recognition)

        self.add_user_btn.setGeometry(QtCore.QRect(250, 170, 261, 27))
        self.add_user_btn.setObjectName("add_user_btn")
        self.add_user_btn.clicked.connect(self.user_form)

        self.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.face_recognition_btn.setText(_translate("MainWindow", "Face Recognition"))
        self.add_user_btn.setText(_translate("MainWindow", "Add User"))

    def user_form(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_user_form()
        self.ui.setupUi(self.window)
        self.window.show()

    def realtime_face_recognition(self):
        print('Face Recognition')
        realtime_face_recognition.run_face()

    # Confirm close window
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # Center App on the screen
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())