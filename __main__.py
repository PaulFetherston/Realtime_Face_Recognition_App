
# Paul Fetherston
#
# Student No: 2898842
#
# BSCH 4th year development project
#
# 31/05/2019


from PyQt5.QtWidgets import QApplication
from home import MainWindow
from realtime_face_recognition import LiveVideo
from live_system import UILiveSystem
import sys

app = QApplication([])
lv = LiveVideo()
ui = UILiveSystem()
w = MainWindow()
lv.make_connection(w)
w.make_connection(lv)
sys.exit(app.exec_())