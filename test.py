# -*- coding: utf-8 -*-

import sys


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QMainWindow, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QFont, QIcon
from test_user_form import Ui_user_form
import user_in_test
import user_search
from test_user_form import Ui_user_form
import realtime_face_recognition


class UIWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle("Facial Recognition App")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)

        self.face_recognition_btn = QPushButton('Face Recognition', self.centralwidget)
        self.face_recognition_btn.setGeometry(QtCore.QRect(250, 140, 261, 27))
        self.face_recognition_btn.setObjectName("face_recognition_btn")
        # self.face_recognition_btn.move(50, 150)

        # MainWindow.setWindowIcon(QtGui.QIcon('beats.PGN'))
        self.add_user_btn = QPushButton('Add User', self.centralwidget)
        self.add_user_btn.setGeometry(QtCore.QRect(250, 170, 261, 27))
        self.add_user_btn.setObjectName("add_user_btn")
        # self.add_user_btn.move(50, 350)

        self.ser_user_btn = QPushButton('Search User', self.centralwidget)
        self.ser_user_btn.setGeometry(QtCore.QRect(250, 200, 261, 27))
        self.ser_user_btn.setObjectName("ser_user_btn")

        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiWindow = UIWindow()
        self.uiUserForm = user_in_test.UIUserForm()
        self.uiSearchUser = user_search.UISearchUser()
        self.startUIWindow()


    def startNewUser(self):
        self.uiUserForm.setupUI(self)
        self.uiUserForm.btn_cancel.clicked.connect(self.startUIWindow)
        self.showMaximized()

    def startSearchUser(self):
        self.uiSearchUser.setupUI(self)
        self.uiSearchUser.btn_cancel.clicked.connect(self.startUIWindow)
        self.uiSearchUser.btn_reset.clicked.connect(self.startSearchUser)
        self.showMaximized()

    def startUIWindow(self):
        self.uiWindow.setupUI(self)
        self.uiWindow.face_recognition_btn.clicked.connect(self.realtime_face_recognition)
        self.uiWindow.add_user_btn.clicked.connect(self.startNewUser)
        self.uiWindow.ser_user_btn.clicked.connect(self.startSearchUser)
        self.showMaximized()

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
