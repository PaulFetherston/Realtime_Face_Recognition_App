# -*- coding: utf-8 -*-

# Paul Fetherston
#
# Student No: 2898842

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QWidget, QMainWindow, QPushButton, QMessageBox)
import add_user
import user_search
import live_system
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

        self.add_user_btn = QPushButton('Add User', self.centralwidget)
        self.add_user_btn.setGeometry(QtCore.QRect(250, 170, 261, 27))
        self.add_user_btn.setObjectName("add_user_btn")

        self.ser_user_btn = QPushButton('Search User', self.centralwidget)
        self.ser_user_btn.setGeometry(QtCore.QRect(250, 200, 261, 27))
        self.ser_user_btn.setObjectName("ser_user_btn")

        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiWindow = UIWindow()
        self.uiUserForm = add_user.UIUserForm()
        self.uiSearchUser = user_search.UISearchUser()
        self.uiLiveSystem = live_system.UILiveSystem()
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

    def startLiveSystem(self):
        self.uiLiveSystem.setupUI(self)
        self.uiLiveSystem.CPSBTN.clicked.connect(self.startUIWindow)
        self.showMaximized()

    def startUIWindow(self):
        self.uiWindow.setupUI(self)
        self.uiWindow.face_recognition_btn.clicked.connect(self.realtime_face_recognition)
        self.uiWindow.add_user_btn.clicked.connect(self.startNewUser)
        self.uiWindow.ser_user_btn.clicked.connect(self.startSearchUser)
        self.showMaximized()

    def realtime_face_recognition(self):
        print('Face Recognition')
        self.startLiveSystem()
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
