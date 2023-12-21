import sys
from screen import *
from PyQt5.QtWidgets import *
from daemon import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.parent = parent
        self.ui = Ui_LinuxAgentUI()
        self.ui.setupUi(self)
        self.myDaemon = MyDaemon()

        self.ui.startBtn.clicked.connect(self.startSlot)
        self.ui.stopBtn.clicked.connect(self.stopSlot)

        self.ui.getPasswordSettingBtn.clicked.connect(self.showPaswordSetting)
        self.ui.getPasswordInfoBtn.clicked.connect(self.showPaswordInfo)
        self.ui.getSerialNumberBtn.clicked.connect(self.showSerialNumber)


    def showPaswordSetting(self):
        username = 'dev'
        password_settings = self.myDaemon.get_linux_password_settings(username)
        formatted_settings = "\n".join(f"{key}: {value}" for key, value in password_settings.items())

        # Create a QMessageBox
        message_box = QMessageBox()
        message_box.setWindowTitle('Information')
        message_box.setText(formatted_settings)
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)

         # Show the message box
        message_box.exec_()

    def showPaswordInfo(self):
        username = 'dev'
        password_settings = self.myDaemon.get_linux_password_info(username)
        
        # Create a QMessageBox
        message_box = QMessageBox()
        message_box.setWindowTitle('Information')
        message_box.setText(password_settings)
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)

        # Show the message box
        message_box.exec_()

    def showSerialNumber(self):
        password_settings = self.myDaemon.get_linux_hard_drive_serial_numbers()
        
        # Create a QMessageBox
        message_box = QMessageBox()
        message_box.setWindowTitle('Information')
        message_box.setText(password_settings)
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)

        # Show the message box
        message_box.exec_()

    def startSlot(self):
        self.myDaemon.start()
    def stopSlot(self):
        self.myDaemon.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())