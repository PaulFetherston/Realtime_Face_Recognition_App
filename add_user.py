# -*- coding: utf-8 -*-

# Paul Fetherston
#
# Student No: 2898842
#
# BSCH 4th year development project
#
# 31/05/2019

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QFrame, QMessageBox)
import image_import
import validator
import db_interface
import pickle
import numpy as np
import datetime

face_encoding = np.array([1])


class UIUserForm(object):
    """Set up the add user form"""
    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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

        self.dob_dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dob_dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dob_dateEdit.setObjectName("dob_dateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dob_dateEdit)
        self.label_dob = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_dob.setObjectName("label_dob")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_dob)

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

        self.face_capture_pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.face_capture_pushButton.setObjectName("face_capture_pushButton")
        self.face_capture_pushButton.clicked.connect(self.launch_webcam)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.face_capture_pushButton)

        self.label_face_captured = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_face_captured.setObjectName("label_face_captured")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_face_captured)
        self.check_box = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.check_box.setObjectName("check_box")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.check_box)
        self.check_box.setChecked(False)
        self.check_box.setEnabled(False)
        self.check_box.hide()
        self.check_box.toggle()
        self.check_box.toggled.connect(self.prevent_toggle)

        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(145, 270, 275, 27))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.update_db)

        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(440, 270, 125, 27))
        self.btn_cancel.setObjectName("btn_cancel")

        self.label_user_added = QtWidgets.QLabel(self.centralwidget)
        self.label_user_added.setGeometry(QtCore.QRect(145, 300, 275, 27))
        self.label_user_added.setObjectName("label_user_added")
        self.label_user_added.setFrameShape(QFrame.Panel)
        self.label_user_added.hide()

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
        """Method to name all labels and buttons"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add New User"))
        self.title.setText(_translate("MainWindow", "Add a New User"))
        self.label_fname.setText(_translate("MainWindow", "First Name"))
        self.label_sname.setText(_translate("MainWindow", "Second Name"))
        self.label_dept.setText(_translate("MainWindow", "Department"))
        self.label_authority.setText(_translate("MainWindow", "Access Level"))
        self.label_dob.setText(_translate("MainWindow", "Date of Birth"))
        self.face_capture_pushButton.setText(_translate("MainWindow", "Capture "))

        self.label_face_captured.setText(_translate("MainWindow", "No Image Captured"))

        self.btn_submit.setText(_translate("MainWindow", "Submit"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.label_user_added.setText(_translate("MainWindow", "Successfully added a new user"))

    def launch_webcam(self):
        """Method to launch the camera to capture a new users image"""
        global face_encoding

        # Call the image_import.add_user method which launches the camera and
        # returns the face encodings if a new picture is taken
        face_encoding = image_import.add_user()

        # Check if a new image was returned from the add_user method
        if len(face_encoding) == 128:
            # Confirm if a new image has been captured
            self.label_face_captured.setText(QtCore.QCoreApplication.translate("MainWindow", "Image Captured   "))
            self.check_box.show()
            self.check_box.setEnabled(True)
            self.check_box.setChecked(True)
        else:
            # Notify if a new image is not captured
            self.label_face_captured.setText(QtCore.QCoreApplication.translate("MainWindow", "No Image Captured"))
            self.check_box.hide()

    # Function to add new user to the database
    def update_db(self):
        """Method to update the database with a new user"""

        global face_encoding

        # Call the validator function which returns true if the user information is valid for uploading to the db
        form_valid = validator.form_validation(self.fname_lineEdit.text(), self.sname_lineEdit.text(),
                                               self.dob_dateEdit.date().toPyDate(), self.dept_lineEdit.text(),
                                               self.authority_spinBox.value(), len(face_encoding))

        if form_valid:
            # If validation passes
            # Put user info into variables
            fname = self.fname_lineEdit.text()
            sname = self.sname_lineEdit.text()
            dob = self.dob_dateEdit.date().toPyDate()
            dept = self.dept_lineEdit.text()
            access = self.authority_spinBox.value()

            # Pass user info to db_interface to insert into DB and return the new user's ID number
            user_id = db_interface.db_insert(fname, sname, dob, dept, access)
            # Create a dictionary with user ID and the face encoding
            ex_dict = {1: 'user_{}'.format(user_id), 2: face_encoding, 3: access, 4: user_id}
            # Pickle dictionary. Name it with the user id
            with open('/home/paul/sdp/pickle_folder/user_{}.pickle'.format(user_id), 'wb') as f:
                pickle.dump(ex_dict, f)

            f.close()
            # Display to notify of successfully adding a new user to the system
            self.label_user_added.show()
            # call reset to reset the form
            self.form_reset()
        # Do the following if the form doesn't pass validation
        else:
            # Display Message box to inform the user the form is incomplete
            QtWidgets.QMessageBox.information(QtWidgets.QMainWindow(), 'Message', 'Form Not Complete',
                                              QMessageBox.Ok)
            # Hides the added label incase it was shown from a previously added user
            self.label_user_added.hide()

    # Function to prevent checkbox from being unchecked by a user
    def prevent_toggle(self):
        self.check_box.setChecked(QtCore.Qt.Checked)

    def form_reset(self):
        """Method to reset the form to allow a new user to be added to the system"""
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