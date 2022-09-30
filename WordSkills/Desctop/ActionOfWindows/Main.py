import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon, QImage
from Desctop.UIDesxtop.Auto import Ui_Autor_MainWindow


class show_main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(show_main_window, self).__init__()
        self.ui = Ui_Autor_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.ui.btn_phone.setPlaceholderText("Ваш номер")
        self.ui.btn_password.setPlaceholderText("Ваш пароль")

    ''' self.setWindowIcon(QtGui.QIcon('Logo.png'))
     доработать лого
     Ошибка  не  появляется  лого

'''
app = QtWidgets.QApplication([])
application = show_main_window()
application.show()

sys.exit(app.exec())
