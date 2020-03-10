from main import RegisterDialog
from service import check_username_used, add_user
from utilities.text import encode
from utilities.initWindow import initLoginDialog


def onAccept(window: RegisterDialog):
    ui = window.ui
    mainWindow = window.mainWindow

    def alert(input, text, clearInput=False):
        mainWindow.showAlert(text)
        input.setFocus()
        if clearInput:
            input.setText('')

    def handleChange():
        username = ui.usernameInput.text()
        pwd = ui.pwdInput.text()
        pwd2 = ui.pwdInput2.text()
        if not username:
            alert(ui.usernameInput, 'Please fill in Username!')
            return
        if not pwd:
            alert(ui.pwdInput, 'Please fill in Password!')
            return
        if not pwd2:
            alert(ui.pwdInput2, 'Please confirm password!')
            return
        if pwd != pwd2:
            alert(ui.pwdInput2, 'Your password and confirmation password do not match.', True)
            return
        if check_username_used(username):
            alert(ui.usernameInput, 'Sorry, that username is already taken.\nPlease try another one.', True)
            return
        add_user(username, encode(pwd))
        window.close()
        initLoginDialog(mainWindow.loginDialog, username)


    return handleChange
