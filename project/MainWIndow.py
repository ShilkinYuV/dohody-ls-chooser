from MainForm import Ui_MainWindow
# from PyQt5.QtWidgets import QAbstractItemView, QDesktopWidget, QDialog, QFileDialog, QLabel, QTableWidgetItem, QHeaderView, QMessageBox, QWidget
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)