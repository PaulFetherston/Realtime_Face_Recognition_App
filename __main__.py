
from PyQt5.QtWidgets import QApplication
from home import Ui_MainWindow
import sys

app = QApplication([])
home = Ui_MainWindow()
sys.exit(app.exec_())