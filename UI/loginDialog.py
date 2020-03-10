# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName("loginDialog")
        loginDialog.resize(285, 110)
        self.formLayout = QtWidgets.QFormLayout(loginDialog)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(loginDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.usernameInput = QtWidgets.QLineEdit(loginDialog)
        self.usernameInput.setText("")
        self.usernameInput.setObjectName("usernameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameInput)
        self.label_2 = QtWidgets.QLabel(loginDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pwdInput = QtWidgets.QLineEdit(loginDialog)
        self.pwdInput.setText("")
        self.pwdInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdInput.setObjectName("pwdInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pwdInput)
        self.buttonBox = QtWidgets.QDialogButtonBox(loginDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.registerButton = QtWidgets.QPushButton(loginDialog)
        self.registerButton.setObjectName("registerButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.registerButton)

        self.retranslateUi(loginDialog)
        self.buttonBox.rejected.connect(loginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)

    def retranslateUi(self, loginDialog):
        _translate = QtCore.QCoreApplication.translate
        loginDialog.setWindowTitle(_translate("loginDialog", "Sign In"))
        self.label.setText(_translate("loginDialog", "Username*"))
        self.label_2.setText(_translate("loginDialog", "Password*"))
        self.registerButton.setText(_translate("loginDialog", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginDialog = QtWidgets.QDialog()
    ui = Ui_loginDialog()
    ui.setupUi(loginDialog)
    loginDialog.show()
    sys.exit(app.exec_())
