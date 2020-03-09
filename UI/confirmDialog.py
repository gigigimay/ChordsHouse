# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_confirmDialog(object):
    def setupUi(self, confirmDialog):
        confirmDialog.setObjectName("confirmDialog")
        confirmDialog.setWindowModality(QtCore.Qt.WindowModal)
        confirmDialog.setEnabled(True)
        confirmDialog.resize(305, 108)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(confirmDialog.sizePolicy().hasHeightForWidth())
        confirmDialog.setSizePolicy(sizePolicy)
        confirmDialog.setAcceptDrops(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(confirmDialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(32, 32, 32, 12)
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(confirmDialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(confirmDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(confirmDialog)
        QtCore.QMetaObject.connectSlotsByName(confirmDialog)

    def retranslateUi(self, confirmDialog):
        _translate = QtCore.QCoreApplication.translate
        confirmDialog.setWindowTitle(_translate("confirmDialog", "Delete"))
        self.label.setText(_translate("confirmDialog", "Confirm Delete?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirmDialog = QtWidgets.QWidget()
    ui = Ui_confirmDialog()
    ui.setupUi(confirmDialog)
    confirmDialog.show()
    sys.exit(app.exec_())
