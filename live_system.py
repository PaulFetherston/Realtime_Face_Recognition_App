# -*- coding: utf-8 -*-

# Paul Fetherston
#
# Student No: 2898842

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QPushButton, QMessageBox, QFrame)
import image_import
import db_interface
import validator
import pickle
import numpy as np
import os


class UILiveSystem(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(400, 450)
        MainWindow.setWindowTitle("UIToolTab")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.CPSBTN = QPushButton("text2", self.centralwidget)
        self.CPSBTN.move(100, 350)
        MainWindow.setCentralWidget(self.centralwidget)