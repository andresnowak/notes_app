# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notes-app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(440, 300)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 20, 421, 281))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalScrollBar = QtWidgets.QScrollBar(Form)
        self.verticalScrollBar.setGeometry(QtCore.QRect(420, 0, 21, 301))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def setupUiSave(self, Form):
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(0, 20, 75, 23))
        self.save.setObjectName("save")
        self.save_as = QtWidgets.QPushButton(Form)
        self.save_as.setGeometry(QtCore.QRect(0, 40, 75, 23))
        self.save_as.setObjectName("save_as")
        self.save_as_text = QtWidgets.QLineEdit(Form)
        self.save_as_text.setGeometry(QtCore.QRect(80, 40, 201, 21))
        self.save_as_text.setObjectName("save_as_text")

        self.retranslateUiSave(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUiSave(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.save.setText(_translate("Form", "Save"))
        self.save_as.setText(_translate("Form", "Save as"))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Options"))

