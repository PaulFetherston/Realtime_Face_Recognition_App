# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_form_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QMainWindow, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget)
import image_import
import db_test_input_output
import pickle
import numpy as np
import cerberus
import datetime

face_encoding = np.array([1])

class Ui_user_form(object):

    def setupUi(self, MainWindow):
        # TODO Comment Code
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 10, 111, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(130, 50, 451, 200))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setContentsMargins(15, 0, 15, 0)
        self.formLayout.setVerticalSpacing(4)
        self.formLayout.setObjectName("formLayout")

        self.label_fname = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_fname.setObjectName("label_fname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_fname)
        self.fname_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.fname_lineEdit.setObjectName("fname_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fname_lineEdit)


        self.label_sname = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_sname.setObjectName("label_sname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_sname)
        self.sname_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sname_lineEdit.setObjectName("sname_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sname_lineEdit)

        self.dept_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.dept_lineEdit.setObjectName("dept_lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dept_lineEdit)
        self.label_dept = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_dept.setObjectName("label_dept")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_dept)

        self.authority_spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.authority_spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.authority_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.authority_spinBox.setMinimum(1)
        self.authority_spinBox.setMaximum(3)
        self.authority_spinBox.setObjectName("authority_spinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.authority_spinBox)
        self.label_authority = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_authority.setObjectName("label_authority")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_authority)

        self.dob_dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dob_dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dob_dateEdit.setObjectName("dob_dateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dob_dateEdit)
        self.label_dob = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_dob.setObjectName("label_dob")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_dob)

        self.face_capture_pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.face_capture_pushButton.setObjectName("face_capture_pushButton")
        self.face_capture_pushButton.clicked.connect(self.launch_webcam)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.face_capture_pushButton)

        self.label_face_captured = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_face_captured.setObjectName("label_face_captured")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_face_captured)
        # self.label_face_captured.hide()

        self.check_box = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.check_box.setObjectName("check_box")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.check_box)
        self.check_box.setChecked(False)
        self.check_box.setEnabled(False)
        self.check_box.hide()
        self.check_box.toggle()
        self.check_box.toggled.connect(self.prevent_toggle)

        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(130, 270, 260, 27))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.update_db)

        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(440, 270, 85, 27))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(self.cancel_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # TODO Comment Code
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Add a New User"))
        self.label_fname.setText(_translate("MainWindow", "First Name"))
        # self.fname_lineEdit.setText(_translate("MainWindow", ""))
        self.label_sname.setText(_translate("MainWindow", "Second Name"))
        # self.sname_lineEdit.setText(_translate("MainWindow", "Second_Name"))
        self.label_dept.setText(_translate("MainWindow", "Department"))
        self.label_authority.setText(_translate("MainWindow", "Access Level"))
        self.label_dob.setText(_translate("MainWindow", "Date of Birth"))
        self.face_capture_pushButton.setText(_translate("MainWindow", "Capture "))

        self.label_face_captured.setText(_translate("MainWindow", "No Image Captured"))

        self.btn_submit.setText(_translate("MainWindow", "Submit"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))

    # Launch camera to take a picture of a new person
    def launch_webcam(self):
        # TODO Comment Code
        global face_encoding

        face_encoding = image_import.add_user()

        if len(face_encoding) == 128:
            self.label_face_captured.setText(QtCore.QCoreApplication.translate("MainWindow", "Image Captured   "))
            self.check_box.show()
            self.check_box.setEnabled(True)
            self.check_box.setChecked(True)
        else:
            self.label_face_captured.setText(QtCore.QCoreApplication.translate("MainWindow", "No Image Captured"))
            self.check_box.hide()

    # Function to add new user to the database
    def update_db(self):
        # TODO form validation

        global face_encoding

        form_valid = self.form_validation()

        if form_valid:

            print('user form call db test')
            # Put user info into variables
            fname = self.fname_lineEdit.text()
            sname = self.sname_lineEdit.text()
            dob = self.dob_dateEdit.date().toPyDate()
            dept = self.dept_lineEdit.text()
            access = self.authority_spinBox.value()

            # Pass user info to script to insert into DB and return the new user's ID number
            user_id = db_test_input_output.db_update(fname, sname, dob, dept, access)
            # Create a dictionary with user ID and the face encoding
            ex_dict = {1: 'user_{}'.format(user_id), 2: face_encoding}
            # Pickle dictionary. Name it with the user id
            with open('/home/paul/sdp/pickle_folder/user_{}.pickle'.format(user_id), 'wb') as f:
                pickle.dump(ex_dict, f)

            f.close()
            self.form_reset()

        else:
            QtWidgets.QMessageBox.information(QtWidgets.QMainWindow(), 'Message', 'Form Not Complete',
                                              QMessageBox.Ok)

    def cancel_btn(self):
        # TODO Configure button effects on form
        print('cancel button pressed')
        # self.closeEvent(QtWidgets.QMainWindow().close())
        QMainWindow.close(QtWidgets.QMainWindow())

    # Function to prevent checkbox from being unchecked by a user
    def prevent_toggle(self):
        self.check_box.setChecked(QtCore.Qt.Checked)

    def form_validation(self):
        schema = {'fname': {'required': True, 'type': 'string', 'empty': False},
                  'lname': {'required': True, 'type': 'string', 'empty': False},
                  'dob': {'required': True, 'type': 'date', 'empty': False},
                  'dept': {'required': True, 'type': 'string', 'empty': False},
                  'access': {'required': True, 'type': 'integer', 'empty': False, 'min': 1, 'max': 3},
                  'face': {'required': True, 'type': 'integer', 'empty': False, 'min': 128, 'max': 128}}

        document = {'fname': self.fname_lineEdit.text(),
                    'lname': self.sname_lineEdit.text(),
                    'dob': self.dob_dateEdit.date().toPyDate(),
                    'dept': self.dept_lineEdit.text(),
                    'access': self.authority_spinBox.value(),
                    'face': len(face_encoding)}
        v = cerberus.Validator(schema)
        print('Cerberus : ', v.validate(document))
        print(v.errors)

        return v.validate(document)

    def form_reset(self):
        global face_encoding
        _translate = QtCore.QCoreApplication.translate
        self.fname_lineEdit.setText(_translate("MainWindow", ""))
        self.sname_lineEdit.setText(_translate("MainWindow", ""))
        self.dob_dateEdit.setDate(datetime.date.today())
        self.dept_lineEdit.setText(_translate("MainWindow", ""))
        self.authority_spinBox.setValue(1)
        face_encoding = np.array([1])
        self.label_face_captured.setText(_translate("MainWindow", "No Image Captured"))
        self.check_box.hide()

    # Confirm close window
    def closeEvent(self, event):

        reply = QMessageBox.question(QtWidgets.QMainWindow(), 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_user_form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
