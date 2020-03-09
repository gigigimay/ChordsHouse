from main import MainWindow


def onActionLogin(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionLogin')

    return handleChange


def onActionLogout(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionLogout')

    return handleChange


def onActionRegister(window: MainWindow):
    ui = window.ui

    def handleChange():
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
