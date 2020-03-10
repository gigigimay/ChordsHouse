from main import MainWindow
from utilities.initWindow import initLoginDialog, initRegisterDialog
from utilities.ui import setCurrentUser, refreshSongList, setSongFav


def onActionLogin(window: MainWindow):
    def handleChange():
        initLoginDialog(window.loginDialog)

    return handleChange


def onActionLogout(window: MainWindow):
    ui = window.ui

    def handleChange():
        setCurrentUser(ui, None)
        refreshSongList(ui)
        window.showAlert('Logged out.', 'Message')

    return handleChange


def onActionRegister(window: MainWindow):
    def handleChange():
        initRegisterDialog(window.registerDialog)

    return handleChange


def onActionChangePassword(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionEditPassword')

    return handleChange


def onActionClearFav(window: MainWindow):
    ui = window.ui

    def handleChange():
        ui.favOnlyCheckbox.setChecked(False)
        setSongFav(ui, [])
        refreshSongList(ui)

    return handleChange
