from PyQt5.QtGui import QFont

from MainForm import Ui_MainWindow
from PyQt5.QtWidgets import QAbstractItemView, QDesktopWidget, QDialog, QFileDialog, QLabel, QTableWidgetItem, QHeaderView, QMessageBox, QWidget
from PyQt5 import QtWidgets, QtCore
import os

from classes.ReadExcel import ReadExcel

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pbtn_add_report.clicked.connect(self.open_file)

        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.horizontalHeader().setVisible(False)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPixelSize(14)
        self.font_t = QFont()
        self.font_t.setPixelSize(14)

        self.writeTBheader()

    def open_file(self):
        self.ui.statusbar.showMessage('')
        self.ui.tableWidget.clear()
        self.writeTBheader()
        self.filename, _ = QFileDialog.getOpenFileName(
            None, 'Открыть', os.path.join(os.path.join(
                os.environ['USERPROFILE']), 'Desktop'),
            'Excel Files(*.xls);;Excel Files(*.xlsx)')


        if self.filename in "('', '')":
            self.ui.statusbar.showMessage('Файл не выбран')

        else:
            self.ui.pbtn_add_report.setEnabled(False)
            self.my_thread = ReadExcel(my_window=self)
            self.my_thread.appendText.connect(self.appendText)
            self.my_thread.start()

    def writeTBheader(self):
        self.ui.tableWidget.setRowCount(1)
        newItem = QTableWidgetItem("Лицевой счет")
        newItem.setFont(self.font)
        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
        self.ui.tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("Возвраты")
        newItem.setFont(self.font)
        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
        self.ui.tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("Зачеты")
        newItem.setFont(self.font)
        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
        self.ui.tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem("Администратор доходов бюджета")
        newItem.setFont(self.font)
        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
        self.ui.tableWidget.setItem(0, 3, newItem)

        newItem = QTableWidgetItem("Наименование бюджета")
        newItem.setFont(self.font)
        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
        self.ui.tableWidget.setItem(0, 4, newItem)

    @QtCore.pyqtSlot(list,bool)
    def appendText(self, list, _bool):
        if _bool:
            self.ui.statusbar.showMessage('Отчет проверен! Есть неисполненные поручения!')
            self.ui.tableWidget.setRowCount(len(list)+1)
            i = 1
            for ls in list:
                newItem = QTableWidgetItem(ls.licevoy)
                newItem.setFont(self.font_t)
                self.ui.tableWidget.setItem(i, 0, newItem)

                newItem = QTableWidgetItem(ls.vozvraty)
                newItem.setFont(self.font_t)
                self.ui.tableWidget.setItem(i, 1, newItem)

                newItem = QTableWidgetItem(ls.zachety)
                newItem.setFont(self.font_t)
                self.ui.tableWidget.setItem(i, 2, newItem)

                newItem = QTableWidgetItem(ls.dohody_admin)
                newItem.setFont(self.font_t)
                self.ui.tableWidget.setItem(i, 3, newItem)

                newItem = QTableWidgetItem(ls.budget)
                newItem.setFont(self.font_t)
                self.ui.tableWidget.setItem(i, 4, newItem)
                i = i+1
        else:
            self.ui.statusbar.showMessage('Отчет проверен! Неисполненных поручений нет!')