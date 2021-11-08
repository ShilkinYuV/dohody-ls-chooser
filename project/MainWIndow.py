from MainForm import Ui_MainWindow
from PyQt5.QtWidgets import QAbstractItemView, QDesktopWidget, QDialog, QFileDialog, QLabel, QTableWidgetItem, QHeaderView, QMessageBox, QWidget
from PyQt5 import QtWidgets
import os

from classes.ReadExcel import ReadExcel

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pbtn_add_report.clicked.connect(self.open_file)

    def open_file(self):
        self.filename, _ = QFileDialog.getOpenFileName(
            None, 'Открыть', os.path.join(os.path.join(
                os.environ['USERPROFILE']), 'Desktop'),
            'Excel Files(*.xls);;Excel Files(*.xlsx)')

        self.my_thread = ReadExcel(my_window=self)
        self.my_thread.start()