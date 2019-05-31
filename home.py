# -*- coding: utf-8 -*-

# Paul Fetherston
#
# Student No: 2898842
#
# BSCH 4th year development project
#
# 31/05/2019

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QMessageBox)
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import add_user
import user_search
import live_system


class UIWindow(object):
    def setupUI(self, MainWindow):
        """setup the UI for the default front page"""

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
    """MainWindow class"""

    # A signal
    changedValue = pyqtSignal(int)

    def __init__(self, parent=None):
        """Initialise the MainWindow -
        - get instances of the alternative views"""

        super(MainWindow, self).__init__(parent)
        self.uiWindow = UIWindow()
        self.uiUserForm = add_user.UIUserForm()
        self.uiSearchUser = user_search.UISearchUser()
        self.uiLiveSystem = live_system.UILiveSystem()
        self.startUIWindow()

    def startNewUser(self):
        """Function to change the MainWindow display to show the new user form
        - The cancel button changes the MainWindow display to show the default display"""
        self.uiUserForm.setupUI(self)
        self.uiUserForm.btn_cancel.clicked.connect(self.startUIWindow)
        self.showMaximized()

    def startSearchUser(self):
        """Function to change the MainWindow display to show the Search User Window
        - The cancel button changes the MainWindow display to show the default display
        - The reset button resets the Search User Window"""
        self.uiSearchUser.setupUI(self)
        self.uiSearchUser.btn_cancel.clicked.connect(self.startUIWindow)
        self.uiSearchUser.btn_reset.clicked.connect(self.startSearchUser)
        self.showMaximized()

    def startLiveSystem(self):
        """Function to change the MainWindow display to show the live System page and
        launch the live video face recognition
        - The close button calls a function to change the MainWindow display to show the default display and
        end the live video feed"""
        self.uiLiveSystem.setupUI(self)
        self.uiLiveSystem.close.clicked.connect(self.end_realtime_face_recognition)
        self.showMaximized()

    def startUIWindow(self):
        """Main default Function to change the MainWindow display to show the default window
        - The face_recognition_btn button calls a function to launch the live video feed and
        change the display to show the live systems window
        - The add_user_btn button changes the MainWindow display the add new user window
        - The ser_user_btn button changes the MainWindow display the search user window"""
        self.uiWindow.setupUI(self)
        self.uiWindow.face_recognition_btn.clicked.connect(self.realtime_face_recognition)
        self.uiWindow.add_user_btn.clicked.connect(self.startNewUser)
        self.uiWindow.ser_user_btn.clicked.connect(self.startSearchUser)
        self.showMaximized()

    def realtime_face_recognition(self):
        """Function to change the MainWindow display to show the live System page and
        call a function to emit a signal to launch the live video face recognition feed"""
        self.startLiveSystem()
        self.on_changed_value(1)

    def end_realtime_face_recognition(self):
        """Function to change the MainWindow display to show the live System page and"""
        self.startUIWindow()
        self.on_changed_value(2)
        self.uiLiveSystem.reset_tables()

    def make_connection(self, slider_object):
        print("Realtime_face +++++++++++++ Make_connection : ", slider_object)
        slider_object.newValue.connect(self.get_slider_value)

    @pyqtSlot(int, int, int, str)
    def get_slider_value(self, flag, usr_id, loc, name):
        print("Realtime_face ++++++++++++++++ HOME get_slider_value : ", name)
        if flag == 1:
            self.uiLiveSystem.insert_tb1(usr_id)
        if flag == 2:
            self.uiLiveSystem.insert_tb2(name, loc)
        if flag == 3:
            self.uiLiveSystem.insert_tb3(usr_id)


    def on_changed_value(self, value):
        print('Home ********** on_changed_value : ', value)
        self.changedValue.emit(value)

    # Confirm close window
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.end_realtime_face_recognition()
            event.accept()
        else:
            event.ignore()
