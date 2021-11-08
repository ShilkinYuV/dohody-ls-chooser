from MainWIndow import MainWindow
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication([])
application = MainWindow()
application.setWindowTitle("Проверщик")
application.show()

sys.exit(app.exec())