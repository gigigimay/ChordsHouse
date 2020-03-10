from main import LoginDialog
from utilities.text import encode
from service import login, check_username_exist
from utilities.ui import setCurrentUser


def onRegister(window: LoginDialog):
    mainWindow = window.mainWindow
    mainUi = mainWindow.ui

    def handleChange():
        window.close()
        mainUi.actionSign_Up.trigger()

    return handleChange


def onAccept(window: LoginDialog):
    ui = window.ui
    mainWindow = window.mainWindow

    def alert(input, text, clearInput=False):
        mainWindow.showAlert(text)
        input.setFocus()
        if clearInput:
            input.setText('')


    def handleChange():
        username = ui.usernameInput.text()
        password = ui.pwdInput.text()
        if not username:
            alert(ui.usernameInput, 'Please fill in username!')
            return
        if not password:
            alert(ui.pwdInput, 'Please fill in password!')
            return
        if not check_username_exist(username):
            alert(ui.usernameInput, 'Username does not exist.', True)
            ui.pwdInput.setText('')
            return
        user = login(username, encode(password))
        if not user:
            alert(ui.pwdInput, 'Incorrect Password!', True)
            return
        mainWindow.showAlert(f'Hello, {username}.\n\nPlease enjoy smashing the favorite button!', 'Message')
        window.close()
        setCurrentUser(mainWindow.ui, user)

    return handleChange