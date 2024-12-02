from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('intro_window.ui', self)
        self.initUI()

    def initUI(self):
        self.tableWidget .setRowCount(10)
        self.tableWidget .setColumnCount(5)