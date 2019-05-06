#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon

# app = QApplication([])
# win = QMainWindow()
# central_widget = QWidget()
# button = QPushButton('Face Recognition')
# button.clicked.connect(button_pressed)
# button2 = QPushButton('Add User')
# button2.clicked.connect(new_button_pressed)
# layout = QVBoxLayout(central_widget)
# layout.addWidget(button)
# layout.addWidget(button2)
# win.setCentralWidget(central_widget)
# win.show()
# app.exit(app.exec_())

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
import image_import
import realtime_face_recognition


def button_pressed():
    print('Face Recognition')
    realtime_face_recognition.run_face()


def new_button_pressed(self):
    print('Add User')
    # image_import.adduser()


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    win = QMainWindow()

    central_widget = QWidget()
    button = QPushButton('Face Recognition')
    button.clicked.connect(button_pressed)
    button2 = QPushButton('Add User')
    button2.clicked.connect(new_button_pressed)
    layout = QVBoxLayout(central_widget)
    layout.addWidget(button)
    layout.addWidget(button2)
    win.setCentralWidget(central_widget)

    w.setWindowTitle('Simple')
    # w.show()
    win.show()

    sys.exit(app.exec_())


