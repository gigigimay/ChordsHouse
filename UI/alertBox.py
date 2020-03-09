# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alertBox.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_alertBox(object):
    def setupUi(self, alertBox):
        alertBox.setObjectName("alertBox")
        alertBox.resize(400, 203)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(alertBox.sizePolicy().hasHeightForWidth())
        alertBox.setSizePolicy(sizePolicy)
        alertBox.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(alertBox)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(32, 32, 32, 32)
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(alertBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(alertBox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(alertBox)
        self.buttonBox.accepted.connect(alertBox.accept)
        QtCore.QMetaObject.connectSlotsByName(alertBox)

    def retranslateUi(self, alertBox):
        _translate = QtCore.QCoreApplication.translate
        alertBox.setWindowTitle(_translate("alertBox", "Dialog"))
        self.label.setText(_translate("alertBox", "Alert!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    alertBox = QtWidgets.QDialog()
    ui = Ui_alertBox()
    ui.setupUi(alertBox)
    alertBox.show()
    sys.exit(app.exec_())
