from main import RegisterDialog
from service import check_username_exist, add_user, edit_password
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
        value1 = ui.usernameInput.text()
        value2 = ui.pwdInput.text()
        value3 = ui.pwdInput2.text()
        if ui.mode == 'register':
            if not value1:
                alert(ui.usernameInput, 'Please fill in username!')
                return
            if not value2:
                alert(ui.pwdInput, 'Please fill in password!')
                return
            if not value3:
                alert(ui.pwdInput2, 'Please confirm password!')
                return
            if value2 != value3:
                alert(ui.pwdInput2, 'Your password and confirmation password do not match.', True)
                return
            if check_username_exist(value1):
                alert(ui.usernameInput, 'Sorry, that username is already taken.\nPlease try another one.', True)
                return
            add_user(value1, encode(value2))
            window.close()
            initLoginDialog(mainWindow.loginDialog, value1)
        elif ui.mode == 'changePassword':
            user = mainWindow.ui.userData
            if not value1:
                alert(ui.usernameInput, 'Please fill in old password!')
                return
            if not value2:
                alert(ui.pwdInput, 'Please fill in old password!')
                return
            if not value3:
                alert(ui.pwdInput2, 'Please confirm password!')
                return
            if value2 != value3:
                alert(ui.pwdInput2, 'Your new password and confirmation password do not match.', True)
                return
            if encode(value1) != user['password']:
                alert(ui.usernameInput, 'Incorrect old password!', True)
                return
            edit_password(user, encode(value2))
            window.close()
            mainWindow.showAlert('Password edited.', 'Message')

    return handleChange
