import os
from PyQt5 import QtCore
import openpyxl
from PyQt5.QtCore import QThread, pyqtSignal
from openpyxl import Workbook
import re

import pyexcel
# from pojo import LS
import re

from .ReportByLS import ReportByLS


class ReadExcel(QThread):

    appendText = QtCore.pyqtSignal(list,bool)

    def __init__(self, my_window, parent=None):
        super(ReadExcel, self).__init__()
        self.my_window = my_window

        self.filename = ''
        self.dict_LS = []
        self.delete_file = True

    def run(self):
        self.filename = self.my_window.filename
        if self.filename.__contains__('.xlsx'):
            self.delete_file = False
        else:
            pyexcel.save_book_as(file_name=self.filename, dest_file_name=self.filename.replace('.xls', '_temp.xlsx'))
            self.filename = self.filename.replace('.xls', '_temp.xlsx')

        wb = openpyxl.load_workbook(self.filename)
        sheet_one = wb.get_sheet_names()[0]
        this_sheet = wb[sheet_one]

        if self.delete_file:
            os.remove(self.filename)

        i = 0

        isWeFindNeispPoruch = False
        templsvalue = None
        for cell in this_sheet['A']:
            i = i + 1

            if str(this_sheet['X' + str(i)].value) is not None and str(this_sheet['X' + str(i)].value) != '█' and len(
                    str(this_sheet['X' + str(i)].value).strip()) == 11 and str(
                this_sheet['X' + str(i)].value).__contains__(",") is not True:
                templsvalue = ReportByLS(licevoy=str(this_sheet['X' + str(i)].value))
                j = i

                while not str(this_sheet['A' + str(j)].value).lower().__contains__('администратор доходов бюджета'):
                    j = j + 1

                while ((str(this_sheet['A' + str(j)].value).lower().__contains__('администратор доходов бюджета') or
                        this_sheet['A' + str(j)].value is None)
                       and not str(this_sheet['A' + str(j)].value).lower().__contains__(
                            'главный администратор доходов бюджета')):
                    templsvalue.dohody_admin = templsvalue.dohody_admin + str(this_sheet['L' + str(j)].value)
                    j = j + 1

                while not str(this_sheet['A' + str(j)].value).lower().__contains__('наименование бюджета'):
                    j = j + 1

                while str(this_sheet['A' + str(j)].value).lower().__contains__('наименование бюджета') \
                        or this_sheet['A' + str(j)].value is None:
                    templsvalue.budget = templsvalue.budget + str(this_sheet['L' + str(j)].value)
                    j = j + 1

            if cell.value is not None and cell.value != '█' and str(cell.value).lower().__contains__(
                    "неисполненные поручения администратора доходов") and templsvalue is not None:
                isWeFindNeispPoruch = True

            if cell.value is not None and cell.value != '█' and str(cell.value).__contains__("Итого") \
                    and isWeFindNeispPoruch:
                templsvalue.vozvraty = str(this_sheet['S' + str(i)].value)
                templsvalue.zachety = str(this_sheet['AB' + str(i)].value)
                self.dict_LS.append(templsvalue)
                isWeFindNeispPoruch = False
                templsvalue = None

        if len(self.dict_LS) > 0:
            self._bool = True
        else:
            self._bool = False

        self.appendText.emit(self.dict_LS,self._bool)

        # for v in self.dict_LS:
        #     print('LS: ', v.licevoy, ' vozvraty: ', v.vozvraty, ' zachety: ', v.zachety)
        #     print('budget: ', v.budget)
        #     print('dohody_admin', v.dohody_admin)

        self.my_window.ui.pbtn_add_report.setEnabled(True)