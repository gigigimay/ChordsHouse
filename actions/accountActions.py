from main import MainWindow
from utilities.initWindow import initLoginDialog, initRegisterDialog
from utilities.ui import setCurrentUser


def onActionLogin(window: MainWindow):
    ui = window.ui

    def handleChange():
        initLoginDialog(window.loginDialog)
        print('onActionLogin')

    return handleChange


def onActionLogout(window: MainWindow):
    ui = window.ui

    def handleChange():
        setCurrentUser(ui, None)
        window.showAlert('Logged out.', 'Message')

    return handleChange


def onActionRegister(window: MainWindow):
    ui = window.ui

    def handleChange():
        initRegisterDialog(window.registerDialog)
        print('onActionRegister')

    return handleChange


def onActionChangePassword(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionEditPassword')

    return handleChange


def onActionClearFav(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionClearFav')

    return handleChange
