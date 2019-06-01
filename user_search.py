# -*- coding: utf-8 -*-

# Paul Fetherston
#
# Student No: 2898842
#
# BSCH 4th year development project
#
# 31/05/2019

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QPushButton, QMessageBox, QFrame)
import image_import
import db_interface
import validator
import pickle
import numpy as np
import os

face_encoding = np.array([1])
new_capture = False
user_id = 0


class UISearchUser(object):
    """MainWindow display that encompases the search, display Db info and Edit db info"""
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle("Search User")
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 10, 111, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.title.setObjectName("title")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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

        self.label_lname = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_lname.setObjectName("label_lname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_lname)
        self.lname_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lname_lineEdit.setObjectName("lname_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lname_lineEdit)

        self.label_sname = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_sname.setObjectName("label_sname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_sname)
        self.sname_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sname_lineEdit.setObjectName("sname_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sname_lineEdit)
        self.label_sname.hide()
        self.sname_lineEdit.hide()

        self.dob_dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dob_dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dob_dateEdit.setObjectName("dob_dateEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dob_dateEdit)
        self.label_dob = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_dob.setObjectName("label_dob")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_dob)
        self.dob_dateEdit.hide()
        self.label_dob.hide()

        self.dept_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.dept_lineEdit.setObjectName("dept_lineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dept_lineEdit)
        self.label_dept = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_dept.setObjectName("label_dept")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_dept)
        self.dept_lineEdit.hide()
        self.label_dept.hide()

        self.label_authority = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_authority.setObjectName("label_authority")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_authority)
        self.label_authority.hide()

        self.authority_spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.authority_spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.authority_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.authority_spinBox.setMinimum(1)
        self.authority_spinBox.setMaximum(3)
        self.authority_spinBox.setObjectName("authority_spinBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.authority_spinBox)
        self.authority_spinBox.hide()

        self.face_capture_pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.face_capture_pushButton.setObjectName("face_capture_pushButton")
        self.face_capture_pushButton.clicked.connect(self.launch_webcam)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.face_capture_pushButton)
        self.face_capture_pushButton.hide()

        self.label_face_captured = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_face_captured.setObjectName("label_face_captured")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_face_captured)
        self.check_box = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.check_box.setObjectName("check_box")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.check_box)
        self.check_box.setChecked(False)
        self.check_box.setEnabled(False)
        self.label_face_captured.hide()
        self.check_box.hide()
        self.check_box.toggle()
        self.check_box.toggled.connect(self.prevent_toggle)

        self.label_no_result = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_no_result.setGeometry(QtCore.QRect(145, 56, 111, 31))
        self.label_no_result.setObjectName("label_no_result")
        self.label_no_result.setFrameShape(QFrame.Panel)
        self.label_no_result.hide()

        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(145, 140, 275, 27))
        self.btn_search.setObjectName("btn_search")
        self.btn_search.clicked.connect(self.search_db)

        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(440, 140, 125, 27))
        self.btn_cancel.setObjectName("btn_cancel")

        self.btn_edit_user = QPushButton('Edit User', self.centralwidget)
        self.btn_edit_user.setGeometry(QtCore.QRect(145, 270, 275, 27))
        self.btn_edit_user.setObjectName("btn_edit_user")
        self.btn_edit_user.clicked.connect(self.user_edit)
        self.btn_edit_user.hide()

        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(440, 270, 125, 27))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_reset.hide()

        self.btn_save_user = QPushButton('Save User', self.centralwidget)
        self.btn_save_user.setGeometry(QtCore.QRect(145, 270, 275, 27))
        self.btn_save_user.setObjectName("btn_save_user")
        self.btn_save_user.clicked.connect(self.user_save)
        self.btn_save_user.hide()

        self.label_user_updated = QtWidgets.QLabel(self.centralwidget)
        self.label_user_updated.setGeometry(QtCore.QRect(250, 300, 220, 27))
        self.label_user_updated.setObjectName("label_no_result")
        self.label_user_updated.setFrameShape(QFrame.Panel)
        self.label_user_updated.hide()

        self.btn_delete_user = QPushButton('Delete User', self.centralwidget)
        self.btn_delete_user.setGeometry(QtCore.QRect(145, 300, 125, 27))
        self.btn_delete_user.setObjectName("btn_delete_user")
        self.btn_delete_user.clicked.connect(self.user_del)
        self.btn_delete_user.hide()

        self.label_user_deleted = QtWidgets.QLabel(self.centralwidget)
        self.label_user_deleted.setGeometry(QtCore.QRect(145, 270, 275, 27))
        self.label_user_deleted.setObjectName("label_no_result")
        self.label_user_deleted.setFrameShape(QFrame.Panel)
        self.label_user_deleted.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mw = MainWindow

    def retranslateUi(self, MainWindow):
        """Method to name all labels and buttons"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User Search"))
        self.title.setText(_translate("MainWindow", "Search User"))
        self.label_fname.setText(_translate("MainWindow", "First Name : "))
        self.label_lname.setText(_translate("MainWindow", "Last Name : "))
        self.label_no_result.setText(_translate("MainWindow", "No User Found !!"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.btn_reset.setText((_translate("MainWindow", "Reset")))
        self.label_sname.setText(_translate("MainWindow", "Second Name : "))
        self.label_dob.setText(_translate("MainWindow", "Date of Birth : "))
        self.label_dept.setText(_translate("MainWindow", "Department : "))
        self.label_authority.setText(_translate("MainWindow", "Access Level"))
        self.face_capture_pushButton.setText(_translate("MainWindow", "Capture "))
        self.label_face_captured.setText(_translate("MainWindow", "Image Captured : "))
        self.btn_delete_user.setText(_translate("MainWindow", "Delete User"))
        self.label_user_updated.setText(_translate("MainWindow", "User Info Successfully Updated"))
        self.label_user_deleted.setText(_translate("MainWindow", "User Successfully Deleted"))

    def search_db(self):
        """Method to search the db for a user and display the results"""
        global user_id

        # Call the db_search method in the db_interface page. Pass in the first and second names
        db_record = db_interface.db_search(self.fname_lineEdit.text(), self.lname_lineEdit.text())

        # no record found display label to inform user
        if len(db_record) < 1:
            self.label_sname.hide()
            self.sname_lineEdit.hide()
            self.label_no_result.show()

            self.label_fname.setText("First Name : ")
            self.fname_lineEdit.setText(self.fname_lineEdit.text())
            self.label_lname.setText("Last Name : ")
            self.lname_lineEdit.setText(self.lname_lineEdit.text())
            self.fname_lineEdit.setReadOnly(False)
            self.lname_lineEdit.setReadOnly(False)
        # If record found set up display for user information
        # and display information about the user
        else:
            self.label_no_result.hide()
            self.label_fname.setText("User Id : ")
            self.label_lname.setText("First Name : ")
            self.label_sname.show()
            self.sname_lineEdit.show()
            self.label_dob.show()
            self.dob_dateEdit.show()

            self.label_dept.show()
            self.dept_lineEdit.show()

            self.label_authority.show()
            self.authority_spinBox.show()

            self.user_info()

            for row in db_record:
                user_id = row[0]
                self.fname_lineEdit.setText(str(row[0]))
                self.lname_lineEdit.setText(row[1])
                self.sname_lineEdit.setText(row[2])
                self.dob_dateEdit.setDate(row[3])
                self.dept_lineEdit.setText(row[4])
                self.authority_spinBox.setValue(row[5])

    # Function to prevent checkbox from being unchecked by a user
    def prevent_toggle(self):
        self.check_box.setChecked(QtCore.Qt.Checked)

    def user_edit(self):
        """Method called from the edit user button when user db info is displayed
        - Make all fields editable except the user id as this is unique to the user
        - Option to capture a new image of the users face is given"""
        self.title.setText("Edit User")
        self.lname_lineEdit.setReadOnly(False)
        self.sname_lineEdit.setReadOnly(False)
        self.dob_dateEdit.setReadOnly(False)
        self.dept_lineEdit.setReadOnly(False)
        self.authority_spinBox.setReadOnly(False)
        self.face_capture_pushButton.show()
        self.btn_edit_user.hide()
        self.btn_save_user.show()
        self.label_user_updated.hide()
        self.btn_delete_user.show()

        global face_encoding
        global user_id

        # Temporarily store the users face encodings in a temp face_encodings variable
        # by pulling the users .pickle file from the pickle folder
        directory_in_str = "/home/paul/sdp/pickle_folder/user_{}.pickle".format(user_id)
        pickle_in = open(directory_in_str, "rb")
        loaded_person = pickle.load(pickle_in)
        face_encoding = (loaded_person[2])

    # Launch camera to take a picture of a new person
    def launch_webcam(self):
        """Method to launch the camera to capture a new image of a user"""
        global face_encoding
        global new_capture

        # Call the image_import.add_user method which launches the camera and
        # returns the face encodings if a new picture is taken
        new_face_encoding = image_import.add_user()

        # Check if a new image was returned from the add_user method
        if len(new_face_encoding) == 128:
            # If new image - set the temp face_encodings variable with the new image
            # - set new_capture to True and update the on screen lable to confirm a new image has been taken
            face_encoding = new_face_encoding
            new_capture = True
            self.label_face_captured.setText("New Image Captured :")

    def user_save(self):
        """Method to save user info in the db after editing information
        - Also update the pickle folder with a new image encodings if a new image was captured"""
        global user_id
        global new_capture

        # Call the validator function which returns true if the user information is valid for uploading to the db
        form_valid = validator.form_validation(self.fname_lineEdit.text(), self.sname_lineEdit.text(),
                                               self.dob_dateEdit.date().toPyDate(), self.dept_lineEdit.text(),
                                               self.authority_spinBox.value(), len(face_encoding))

        # Do the following if the form passes validation
        if form_valid:
            # Put user info into variables
            fname = self.lname_lineEdit.text()
            sname = self.sname_lineEdit.text()
            dob = self.dob_dateEdit.date().toPyDate()
            dept = self.dept_lineEdit.text()
            access = self.authority_spinBox.value()

            # Pass user info to db_interface to update the DB
            db_interface.db_update(user_id, fname, sname, dob, dept, access)

            if new_capture:
                # If a new image of the user is captured remove the old .pickle file from the pickle folder
                os.remove('/home/paul/sdp/pickle_folder/user_{}.pickle'.format(user_id))
                # Create a dictionary with user ID and the new face encoding
                ex_dict = {1: 'user_{}'.format(user_id), 2: face_encoding}
                # Pickle dictionary. Name it with the user id and put it in the pickle folder
                with open('/home/paul/sdp/pickle_folder/user_{}.pickle'.format(user_id), 'wb') as f:
                    pickle.dump(ex_dict, f)

                f.close()
                # Reset the capture so a new image can be taken if necessarily
                new_capture = False

            # Returns to the edit window to display the newly edited user info and
            # shows the user updated label to confirm the users info has successfully been updated
            self.user_info()
            self.label_user_updated.show()
        # Do the following if the form doesn't pass validation
        else:
            # Display Message box to inform the user the form is incomplete
            QtWidgets.QMessageBox.information(QtWidgets.QMainWindow(), 'Message', 'Form Not Complete',
                                              QMessageBox.Ok)

    def user_del(self):
        """Method to confirm if the user is to be deleted from the db
        - Display a messagebox to confirm deletion or cancel deletion"""
        reply = QMessageBox.question(self.mw, 'Delete User',
                                     "Are you sure you wish to delete this user?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Confirmed deletion calls the confirm_user_del
            self.confirm_user_del()

    def confirm_user_del(self):
        """Method to delete all db and pickle folder information about the user"""

        # Remove .pickle file from pickle folder
        os.remove('/home/paul/sdp/pickle_folder/user_{}.pickle'.format(user_id))
        # Call user delete method in the db_interface file. Pass the user id to be deleted
        db_interface.db_user_delete(user_id)

        # Disable all filds from being editable and hide the required buttons and labels from view
        # Show label confirming user deletion
        self.fname_lineEdit.setReadOnly(True)
        self.lname_lineEdit.setReadOnly(True)
        self.sname_lineEdit.setReadOnly(True)
        self.dob_dateEdit.setReadOnly(True)
        self.dept_lineEdit.setReadOnly(True)
        self.authority_spinBox.setReadOnly(True)

        self.face_capture_pushButton.hide()
        self.label_face_captured.hide()
        self.check_box.hide()

        self.label_user_deleted.show()
        self.btn_save_user.hide()
        self.btn_delete_user.hide()

    def user_info(self):
        """Method to set up the display for the user information passed
        - No field can be edited as it is only displayed info at the point"""
        self.title.setText("User Info")
        self.fname_lineEdit.setReadOnly(True)
        self.lname_lineEdit.setReadOnly(True)
        self.sname_lineEdit.setReadOnly(True)
        self.dob_dateEdit.setReadOnly(True)
        self.dept_lineEdit.setReadOnly(True)
        self.authority_spinBox.setReadOnly(True)

        self.label_face_captured.show()
        self.check_box.show()
        self.check_box.setEnabled(True)
        self.check_box.setChecked(True)

        self.face_capture_pushButton.hide()
        self.btn_save_user.hide()
        self.btn_edit_user.show()

        self.btn_search.hide()
        self.btn_cancel.hide()
        self.btn_reset.show()
        self.btn_delete_user.hide()