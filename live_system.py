# -*- coding: utf-8 -*-

# Paul Fetherston
#
# Student No: 2898842
#
# BSCH 4th year development project
#
# 31/05/2019

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QTableWidget)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import db_interface
import datetime

row_count = 0
user_id = []
unauthorised_user = []
unknown_person = []


class UILiveSystem(object):

    changedValue = pyqtSignal(int)

    def setupUI(self, MainWindow):
        """setup the UI for the Live Systems page"""

        MainWindow.setWindowTitle("UIToolTab")
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.title = QtWidgets.QLabel()
        self.title.setObjectName("title")
        self.title2 = QtWidgets.QLabel()
        self.title2.setObjectName("title")

        self.groups = QHBoxLayout(self.centralwidget)

        self.tableWidget1 = QTableWidget()
        self.tableWidget1.setObjectName("tableWidget1")
        self.createTable1()
        self.tableWidget1.setHorizontalHeaderLabels(["Time", "Name", "Dept."])
        self.tableWidget1.resizeColumnsToContents()

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

        a_b_c_d = QVBoxLayout()
        a_b_c_d.setContentsMargins(5, 5, 5, 5)
        a_b_c_d.addWidget(self.close)

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
        # Create table 1
        self.tableWidget1.setWindowTitle("First Table")
        self.tableWidget1.setContentsMargins(10, 10, 10, 10)
        self.tableWidget1.setMaximumWidth(400)
        self.tableWidget1.setRowCount(0)
        self.tableWidget1.setColumnCount(3)
        self.tableWidget1.move(0, 0)

        # table selection change
        self.tableWidget1.doubleClicked.connect(self.on_click)

    def createTable2(self):
        # Create table 2
        self.tableWidget2 = QTableWidget()
        self.tableWidget2.setWindowTitle("Second Table")
        self.tableWidget2.setContentsMargins(10, 10, 10, 10)
        self.tableWidget2.setMaximumWidth(400)
        self.tableWidget2.setRowCount(0)
        self.tableWidget2.setColumnCount(3)
        self.tableWidget2.move(0, 0)

        # table selection change
        self.tableWidget2.doubleClicked.connect(self.on_click)

    def createTable3(self):
        # Create table 3
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
        """Method to handle information from clicked table cell
        -Future Work!!"""
        print("\n")
        for currentQTableWidgetItem in self.tableWidget1.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def insert_tb1(self, id_usr):
        """Method to insert data to table 1
        -Known people on the site seen in any area regardless of authority level"""

        # get the current time
        now = datetime.datetime.now()

        global user_id

        # If seen user is not already in the table insert into table 1
        if id_usr not in user_id:
            # Add user ID to user_id array
            user_id.append(id_usr)

            # Get user info from db
            user_record = db_interface.db_id_search(id_usr)

            # set variables
            name = 'Unknown'
            dept = 'unknown'

            # set variables based on db recors
            for row in user_record:
                name = '{} {}'.format(row[1], row[2])
                dept = row[3]

            # Create a empty row at bottom of table
            numRows = self.tableWidget1.rowCount()
            self.tableWidget1.insertRow(numRows)

            # Populate the relevant columns with the data
            self.tableWidget1.setItem(numRows, 0, QtWidgets.QTableWidgetItem(now.strftime("%Y-%m-%d %H:%M")))
            self.tableWidget1.setItem(numRows, 1, QtWidgets.QTableWidgetItem(name))
            self.tableWidget1.setItem(numRows, 2, QtWidgets.QTableWidgetItem(dept))
            self.tableWidget1.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.tableWidget1.resizeColumnsToContents()
            self.tableWidget1.item(numRows, 2).setTextAlignment(Qt.AlignCenter)

    def insert_tb2(self, unknown_name, loc):
        """Method to insert data to table 2
        -Unknown people seen in any area"""
        # get the time and date
        now = datetime.datetime.now()
        # create a name consisting of the user name and their location
        #This allows a person to be entered onto the table for each time
        # they are seen in an area without the correct aurthorisation
        name_loc = '{} - {}'.format(unknown_name, str(loc))

        global unknown_person
        # Update table if the person has not been seen in a location before
        if name_loc not in unknown_person:
            # Update the unknown_person array
            unknown_person.append(name_loc)


            # Create a empty row at bottom of table
            numRows = self.tableWidget2.rowCount()
            self.tableWidget2.insertRow(numRows)

            # Populate the relevant columns with the data
            self.tableWidget2.setItem(numRows, 0, QtWidgets.QTableWidgetItem(now.strftime("%Y-%m-%d %H:%M")))
            self.tableWidget2.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(loc)))
            self.tableWidget2.setItem(numRows, 2, QtWidgets.QTableWidgetItem(unknown_name))
            self.tableWidget2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.tableWidget2.resizeColumnsToContents()
            self.tableWidget2.item(numRows, 1).setTextAlignment(Qt.AlignCenter)

    def insert_tb3(self, id_usr, name):
        """Method to insert data to table 3
        - Known and Unknown people seen in any area without the correct authorisation"""
        # get the time and date
        now = datetime.datetime.now()

        global user_id
        global unauthorised_user
        # initialise some variables
        dept = '-'
        usr_id = '-'

        # Get user info from db
        user_record = db_interface.db_id_search(id_usr)
        # If the id of the person is in the database they are a known person
        if len(user_record) > 0:
            for row in user_record:
                # Set variables based on db record
                usr_id = row[0]
                name = '{} {}'.format(row[1], row[2])
                dept = row[3]

            if usr_id not in user_id:
                # If person is not already seen on they system - send Id to table 1 to record their presents on site
                self.insert_tb1(usr_id)
        # Check if the person has not already been added to table 3
        if name not in unauthorised_user:
            # If not add thir name to the unauthorised_user array
            unauthorised_user.append(name)

            # Create a empty row at bottom of table
            numRows = self.tableWidget3.rowCount()
            self.tableWidget3.insertRow(numRows)

            # Populate table 3 with user info
            self.tableWidget3.setItem(numRows, 0, QtWidgets.QTableWidgetItem(now.strftime("%Y-%m-%d %H:%M")))
            self.tableWidget3.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(usr_id)))
            self.tableWidget3.setItem(numRows, 2, QtWidgets.QTableWidgetItem(name))
            self.tableWidget3.setItem(numRows, 3, QtWidgets.QTableWidgetItem(dept))
            self.tableWidget3.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.tableWidget3.resizeColumnsToContents()
            self.tableWidget3.item(numRows, 1).setTextAlignment(Qt.AlignCenter)
            self.tableWidget3.item(numRows, 3).setTextAlignment(Qt.AlignCenter)

    @staticmethod
    def reset_tables():
        """Method to reset arrays"""
        global user_id
        global unauthorised_user
        global unknown_person

        user_id = []
        unauthorised_user = []
        unknown_person = []