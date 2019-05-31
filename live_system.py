# -*- coding: utf-8 -*-

# Paul Fetherston
#
# Student No: 2898842

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem)

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import image_import
import db_interface
import datetime
import validator
import pickle
import numpy as np
import os

row_count = 0
user_id = []
unauthorised_user = []
unknown_person = []


class UILiveSystem(object):

    changedValue = pyqtSignal(int)

    def setupUI(self, MainWindow):

        MainWindow.setWindowTitle("UIToolTab")
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255); margin:5px; border:1px solid rgb(255, 0, 0); ")
        # # self.verticalLayoutWidget.setStyleSheet("background-color: rgb(255, 255, 255); margin:5px; border:1px solid rgb(0, 255, 0); ")


        self.title = QtWidgets.QLabel()
        self.title.setObjectName("title")
        self.title2 = QtWidgets.QLabel()
        self.title2.setObjectName("title")

        # self.wid = QtWidgets.QWidget()
        # self.setCentralWidget(self.wid)

        self.groups = QHBoxLayout(self.centralwidget)
        self.tableWidget1 = QTableWidget()
        self.tableWidget1.setObjectName("tableWidget1")
        self.createTable1()
        self.tableWidget1.setHorizontalHeaderLabels(["Time", "Name", "Dept."])
        self.tableWidget1.resizeColumnsToContents()

        # numRows = self.tableWidget1.rowCount()
        # print("WWWWWWWWWWWWWWDDDDDDDDDDDDDDDDDDDDD : ", numRows)

        self.createTable2()
        self.tableWidget2.setHorizontalHeaderLabels(["Time", "Location", "Unknown Person"])
        self.tableWidget2.resizeColumnsToContents()

        self.createTable3()
        self.tableWidget3.setHorizontalHeaderLabels(["Time", "User ID", "Name", "Dept."])
        self.tableWidget3.resizeColumnsToContents()

        l_a1 = QtWidgets.QLabel('People on site')
        a = QVBoxLayout()
        a.setContentsMargins(5, 5, 5, 5)
        a.addWidget(l_a1)
        a.addWidget(self.tableWidget1)

        l_a2 = QtWidgets.QLabel('Unknown People Alerts')
        a_b = QVBoxLayout()
        a_b.setContentsMargins(5, 5, 5, 5)
        a_b.addWidget(l_a2)
        a_b.addWidget(self.tableWidget2)

        l_a3 = QtWidgets.QLabel('Unauthorised Access')
        a_b_c = QVBoxLayout()
        a_b_c.setContentsMargins(5, 5, 5, 5)
        a_b_c.addWidget(l_a3)
        a_b_c.addWidget(self.tableWidget3)

        self.close = QtWidgets.QPushButton('close')
        self.close.setObjectName("close")

        self.test = QPushButton('test')
        self.test.setObjectName("test")
        self.test.clicked.connect(self.insert_tb1)

        a_b_c_d = QVBoxLayout()
        a_b_c_d.setContentsMargins(5, 5, 5, 5)
        a_b_c_d.addWidget(self.close)
        a_b_c_d.addWidget(self.test)

        a.setAlignment(Qt.AlignTop)
        a_b.setAlignment(Qt.AlignTop)
        a_b_c.setAlignment(Qt.AlignTop)
        a_b_c_d.setAlignment(Qt.AlignTop)

        self.groups.addLayout(a)
        self.groups.addLayout(a_b)
        self.groups.addLayout(a_b_c)
        self.groups.addLayout(a_b_c_d)
        self.groups.setAlignment(Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        # TODO Comment Code
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Live System"))
        self.title.setText(_translate("MainWindow", "Live System View"))
        self.title2.setText(_translate("MainWindow", "Live System View 2"))

    def createTable1(self):
        # Create table
        # self.tableWidget1 = QTableWidget()
        self.tableWidget1.setWindowTitle("First Table")
        self.tableWidget1.setContentsMargins(10, 10, 10, 10)
        self.tableWidget1.setMaximumWidth(400)
        self.tableWidget1.setRowCount(0)
        self.tableWidget1.setColumnCount(3)
        self.tableWidget1.move(0, 0)

        # table selection change
        self.tableWidget1.doubleClicked.connect(self.on_click)

    def createTable2(self):
        # Create table
        self.tableWidget2 = QTableWidget()
        self.tableWidget2.setWindowTitle("Second Table")
        self.tableWidget2.setContentsMargins(10, 10, 10, 10)
        self.tableWidget2.setMaximumWidth(400)
        self.tableWidget2.setRowCount(0)
        self.tableWidget2.setColumnCount(3)
        self.tableWidget2.move(0, 0)

        # table selection change
        #self.tableWidget2.doubleClicked.connect(self.on_click)

    def createTable3(self):
        # Create table
        self.tableWidget3 = QTableWidget()
        self.tableWidget3.setWindowTitle("Third Table")
        self.tableWidget3.setContentsMargins(10, 10, 10, 10)
        self.tableWidget3.setMaximumWidth(400)
        self.tableWidget3.setRowCount(0)
        self.tableWidget3.setColumnCount(4)
        self.tableWidget3.move(0, 0)

        # table selection change
        self.tableWidget3.doubleClicked.connect(self.on_click)

    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget1.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def insert_tb1(self, id_usr):
        print("Inserting into Table 1 user id = ", id_usr)
        now = datetime.datetime.now()

        global user_id

        if id_usr not in user_id:
            print("User id = ", id_usr)
            print("TimeDate = ", now)
            user_id.append(id_usr)

            print(user_id)

            # Get user info from db
            user_record = db_interface.db_id_search(id_usr)

            name = 'Unknown'
            dept = 'unknown'

            for row in user_record:
                name = '{} {}'.format(row[1], row[2])
                dept = row[3]

            # Create a empty row at bottom of table
            numRows = self.tableWidget1.rowCount()
            self.tableWidget1.insertRow(numRows)

            # Add text to the row
            self.tableWidget1.setItem(numRows, 0, QtWidgets.QTableWidgetItem(now.strftime("%Y-%m-%d %H:%M")))
            self.tableWidget1.setItem(numRows, 1, QtWidgets.QTableWidgetItem(name))
            self.tableWidget1.setItem(numRows, 2, QtWidgets.QTableWidgetItem(dept))
            self.tableWidget1.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.tableWidget1.resizeColumnsToContents()

    def insert_tb2(self, unknown_name, loc):
        print("Inserting into Table 1 user id = ", unknown_name)
        now = datetime.datetime.now()

        name_loc = '{} - {}'.format(unknown_name, loc)

        global unknown_person

        if name_loc not in unknown_person:

            # Create a empty row at bottom of table
            numRows = self.tableWidget2.rowCount()
            self.tableWidget2.insertRow(numRows)

            # Add text to the row
            self.tableWidget2.setItem(numRows, 0, QtWidgets.QTableWidgetItem(now.strftime("%Y-%m-%d %H:%M")))
            self.tableWidget2.setItem(numRows, 1, QtWidgets.QTableWidgetItem(loc))
            self.tableWidget2.setItem(numRows, 2, QtWidgets.QTableWidgetItem(unknown_name))
            self.tableWidget2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.tableWidget2.resizeColumnsToContents()

    def insert_tb3(self, id_usr):
        print("Inserting into Table 3 user id = ", id_usr)
        now = datetime.datetime.now()

        global user_id
        global unauthorised_user

        if id_usr not in unauthorised_user:
            print("User id = ", id_usr)
            print("TimeDate = ", now)
            unauthorised_user.append(id_usr)

            if id_usr not in user_id:
                self.insert_tb1(id_usr)

            print(user_id)

            # Get user info from db
            user_record = db_interface.db_id_search(id_usr)

            name = 'Unknown'
            dept = 'unknown'
            usr_id = 'Unknown'

            for row in user_record:
                usr_id = str(row[0])
                name = '{} {}'.format(row[1], row[2])
                dept = row[3]

            # Create a empty row at bottom of table
            numRows = self.tableWidget3.rowCount()
            self.tableWidget3.insertRow(numRows)

            # Add text to the row
            self.tableWidget3.setItem(numRows, 0, QtWidgets.QTableWidgetItem(now.strftime("%Y-%m-%d %H:%M")))
            self.tableWidget3.setItem(numRows, 1, QtWidgets.QTableWidgetItem(usr_id))
            self.tableWidget3.setItem(numRows, 2, QtWidgets.QTableWidgetItem(name))
            self.tableWidget3.setItem(numRows, 3, QtWidgets.QTableWidgetItem(dept))
            self.tableWidget3.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.tableWidget3.resizeColumnsToContents()


    def make_connection(self, slider_object):
        print("Live_System 55555555555555 make_connection : ", slider_object)
        self.get_slider_value(slider_object)
        # slider.changedValue.connect(self.get_slider_value)


    @pyqtSlot(int)
    def get_slider_value(self, val):
        print("HERE IS THE VALUE 55555555555555 = ", val)

    def reset_tables(self):
        global user_id
        global unauthorised_user
        global unknown_person

        user_id = []
        unauthorised_user = []
        unknown_person = []