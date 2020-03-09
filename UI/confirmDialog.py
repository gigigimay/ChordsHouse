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
        confirmDialog.resize(305, 218)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(confirmDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.deleteButton = QtWidgets.QPushButton(confirmDialog)
        self.deleteButton.setAutoDefault(True)
        self.deleteButton.setDefault(True)
        self.deleteButton.setFlat(False)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(confirmDialog)
        QtCore.QMetaObject.connectSlotsByName(confirmDialog)

    def retranslateUi(self, confirmDialog):
        _translate = QtCore.QCoreApplication.translate
        confirmDialog.setWindowTitle(_translate("confirmDialog", "Delete"))
        self.label.setText(_translate("confirmDialog", "Confirm Delete?"))
        self.cancelButton.setText(_translate("confirmDialog", "Cancel"))
        self.deleteButton.setText(_translate("confirmDialog", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirmDialog = QtWidgets.QWidget()
    ui = Ui_confirmDialog()
    ui.setupUi(confirmDialog)
    confirmDialog.show()
    sys.exit(app.exec_())
