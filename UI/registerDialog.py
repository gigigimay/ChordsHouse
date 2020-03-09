# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registerDialog(object):
    def setupUi(self, registerDialog):
        registerDialog.setObjectName("registerDialog")
        registerDialog.resize(324, 147)
        self.formLayout = QtWidgets.QFormLayout(registerDialog)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(registerDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.usernameInput = QtWidgets.QLineEdit(registerDialog)
        self.usernameInput.setText("")
        self.usernameInput.setObjectName("usernameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameInput)
        self.label_2 = QtWidgets.QLabel(registerDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pwdInput = QtWidgets.QLineEdit(registerDialog)
        self.pwdInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdInput.setObjectName("pwdInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pwdInput)
        self.label_3 = QtWidgets.QLabel(registerDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pwdInput2 = QtWidgets.QLineEdit(registerDialog)
        self.pwdInput2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdInput2.setObjectName("pwdInput2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pwdInput2)
        self.buttonBox = QtWidgets.QDialogButtonBox(registerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(registerDialog)
        self.buttonBox.accepted.connect(registerDialog.accept)
        self.buttonBox.rejected.connect(registerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(registerDialog)

    def retranslateUi(self, registerDialog):
        _translate = QtCore.QCoreApplication.translate
        registerDialog.setWindowTitle(_translate("registerDialog", "Sign Up"))
        self.label.setText(_translate("registerDialog", "Username"))
        self.label_2.setText(_translate("registerDialog", "Password"))
        self.label_3.setText(_translate("registerDialog", "Confirm Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerDialog = QtWidgets.QDialog()
    ui = Ui_registerDialog()
    ui.setupUi(registerDialog)
    registerDialog.show()
    sys.exit(app.exec_())
