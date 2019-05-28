
from PyQt5.QtWidgets import QApplication
from home import Ui_MainWindow
from test import MainWindow
import sys

app = QApplication([])
# home = Ui_MainWindow()

w = MainWindow()

sys.exit(app.exec_())