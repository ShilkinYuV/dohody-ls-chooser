# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 424)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/roskazna.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow, QMenuBar, QMenu, QAction, QStatusBar{\n"
"background-color: #003dad;\n"
"color: white;\n"
"}\n"
"\n"
"QMenu::selected{\n"
"background-color: #63b9ff;\n"
"color: white;\n"
"}\n"
"QMenuBar::item:selected{\n"
"background-color: #63b9ff;\n"
"color: white;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget\n"
"{\n"
"background-color: white\n"
"};")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbtn_add_report = QtWidgets.QPushButton(self.widget_2)
        self.pbtn_add_report.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pbtn_add_report.setStyleSheet(".QPushButton{\n"
"background-color: #3a66e0;\n"
"color: white;\n"
"border: 0;\n"
"height: 20px;\n"
"}\n"
"\n"
".QPushButton::hover{\n"
"    background-color: #63b9ff;\n"
"}")
        self.pbtn_add_report.setObjectName("pbtn_add_report")
        self.verticalLayout.addWidget(self.pbtn_add_report)
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget.setStyleSheet(".QTableWidget{\n"
"background-color: #3a66e0;\n"
"color: white;\n"
"border: 0;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_about_program = QtWidgets.QAction(MainWindow)
        self.action_about_program.setObjectName("action_about_program")
        self.action_save_to_excel = QtWidgets.QAction(MainWindow)
        self.action_save_to_excel.setObjectName("action_save_to_excel")
        self.menu.addAction(self.action_save_to_excel)
        self.menu_2.addAction(self.action_about_program)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbtn_add_report.setText(_translate("MainWindow", "Проверить отчет"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Помощь"))
        self.action_about_program.setText(_translate("MainWindow", "О программе"))
        self.action_save_to_excel.setText(_translate("MainWindow", "Сохранить в Excel"))
import resourses