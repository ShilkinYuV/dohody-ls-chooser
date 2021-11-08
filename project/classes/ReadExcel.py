import os
from PyQt5 import QtCore
import openpyxl
from PyQt5.QtCore import QThread, pyqtSignal
from openpyxl import Workbook
import re

import pyexcel
# from pojo import LS
import re

class ReadExcel(QThread):
    def __init__(self, my_window, parent=None):
        super(ReadExcel, self).__init__()
        self.my_window = my_window
        
        self.filename = ''
        self.dict_lic_scheta = {}
        self.dict_summ = {}
        self.dict_vozvraty = {}
        self.dict_zachety = {}
        self.dict_LS = []
        self.delete_file = True

    def run(self):
        self.filename = self.my_window.filename
        if self.filename.__contains__('.xlsx'):
            self.delete_file = False
        else:
            pyexcel.save_book_as(file_name=self.filename,dest_file_name=self.filename.replace('.xls','_temp.xlsx'))
            self.filename = self.filename.replace('.xls','_temp.xlsx')

        wb = openpyxl.load_workbook(self.filename)
        sheet_one = wb.get_sheet_names()[0]
        this_sheet = wb[sheet_one]

        if self.delete_file:
                os.remove(self.filename)

        i = 0
        
        for cell in this_sheet['X']:
            i = i + 1
            if cell.value != None and cell.value != '█' and len(str(cell.value).strip()) == 11 and str(cell.value).__contains__(",") != True:
                self.dict_lic_scheta[i] = str(cell.value)

        i = 0
        
        isWeFindNeispPoruch = False

        for cell in this_sheet['A']:
            i = i + 1
            if cell.value != None and cell.value != '█' and str(cell.value).lower().__contains__("неисполненные поручения администратора доходов"):
                isWeFindNeispPoruch = True

            if cell.value != None and cell.value != '█' and str(cell.value).__contains__("Итого") and isWeFindNeispPoruch:
                self.dict_summ[i] = str(cell.value)
                isWeFindNeispPoruch = False

        print(len(self.dict_lic_scheta))
        print(len(self.dict_summ))