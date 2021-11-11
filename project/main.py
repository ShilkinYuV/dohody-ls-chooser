from MainWIndow import MainWindow
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication([])
application = MainWindow()
application.setWindowTitle("Проверка неисполненных поручений v1.0")
application.show()

sys.exit(app.exec())