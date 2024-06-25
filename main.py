from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from loginform import Ui_MainWindow  

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.login)  
        self.pushButton.clicked.connect(self.cancel) 

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username == "admin" and password == "admin":
            QMessageBox.information(self, "Login", "Selamat Anda berhasil login!")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
        else:
            QMessageBox.warning(self, "Login", "Username atau password salah!")

    def cancel(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        QMessageBox.information(self, "Cancel", "Kembali ke halaman utama.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
