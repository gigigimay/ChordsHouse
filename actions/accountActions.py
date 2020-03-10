from main import MainWindow
from utilities.initWindow import initLoginDialog, initRegisterDialog


def onActionLogin(window: MainWindow):
    ui = window.ui

    def handleChange():
        initLoginDialog(window.loginDialog)
        print('onActionLogin')

    return handleChange


def onActionLogout(window: MainWindow):
    ui = window.ui

    def handleChange():
        ui.userData = None
        print('onActionLogout')

    return handleChange


def onActionRegister(window: MainWindow):
    ui = window.ui

    def handleChange():
        initRegisterDialog(window.registerDialog)
        print('onActionRegister')

    return handleChange


def onActionProfile(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionProfile')

    return handleChange


def onActionClearFav(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionClearFav')

    return handleChange
