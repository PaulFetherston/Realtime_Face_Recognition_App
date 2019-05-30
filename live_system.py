# -*- coding: utf-8 -*-

# Paul Fetherston
#
# Student No: 2898842

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem)

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from onsite import Onsite
import image_import
import db_interface
import validator
import pickle
import numpy as np
import os


class UILiveSystem(object):

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

        self.createTable1()
        self.tableWidget1.setHorizontalHeaderLabels(["Time", "Name", "Dept."])
        self.tableWidget1.resizeColumnsToContents()

        self.createTable2()
        self.tableWidget2.setHorizontalHeaderLabels(["Time", "Name", "Dept."])
        self.tableWidget2.resizeColumnsToContents()

        self.createTable3()
        self.tableWidget3.setHorizontalHeaderLabels(["Time", "Name", "Dept."])
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

        l_a3 = QtWidgets.QLabel('A')
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
        # Create table
        self.tableWidget1 = QTableWidget()
        self.tableWidget1.setWindowTitle("First Table")
        self.tableWidget1.setContentsMargins(10, 10, 10, 10)
        self.tableWidget1.setMaximumWidth(400)
        self.tableWidget1.setRowCount(4)
        self.tableWidget1.setColumnCount(3)
        self.tableWidget1.setItem(0, 0, QTableWidgetItem("5555555  Cell (1,1)"))
        self.tableWidget1.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget1.setItem(0, 2, QTableWidgetItem("Cell (1,3)"))
        self.tableWidget1.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget1.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget1.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget1.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget1.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget1.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget1.move(0, 0)

        # table selection change
        self.tableWidget1.doubleClicked.connect(self.on_click)

    def createTable2(self):
        # Create table
        self.tableWidget2 = QTableWidget()
        self.tableWidget2.setWindowTitle("First Table")
        self.tableWidget2.setContentsMargins(10, 10, 10, 10)
        self.tableWidget2.setMaximumWidth(400)
        self.tableWidget2.setRowCount(4)
        self.tableWidget2.setColumnCount(3)
        self.tableWidget2.setItem(0, 0, QTableWidgetItem("kkkk (1,1)"))
        self.tableWidget2.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget2.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget2.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget2.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget2.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget2.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget2.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget2.move(0, 0)

        # table selection change
        self.tableWidget2.doubleClicked.connect(self.on_click)

    def createTable3(self):
        # Create table
        self.tableWidget3 = QTableWidget()
        self.tableWidget3.setWindowTitle("First Table")
        self.tableWidget3.setContentsMargins(10, 10, 10, 10)
        self.tableWidget3.setMaximumWidth(400)
        self.tableWidget3.setRowCount(4)
        self.tableWidget3.setColumnCount(3)
        self.tableWidget3.setItem(0, 0, QTableWidgetItem("kkkk (1,1)"))
        self.tableWidget3.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget3.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget3.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget3.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget3.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget3.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget3.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget3.move(0, 0)

        # table selection change
        self.tableWidget3.doubleClicked.connect(self.on_click)

    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
