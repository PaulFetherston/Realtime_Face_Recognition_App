from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

import image_import
import realtime_face_recognition


def button_pressed():
    print('Face Recognition')
    realtime_face_recognition.run_face()


def new_button_pressed():
    print('Add User')
    image_import.adduser()




app = QApplication([])
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
win.show()
app.exit(app.exec_())



