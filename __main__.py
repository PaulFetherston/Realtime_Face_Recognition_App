
# Paul Fetherston
#
# Student No: 2898842


from PyQt5.QtWidgets import QApplication
from home import MainWindow
from realtime_face_recognition import LiveVideo
from live_system import UILiveSystem
import sys

app = QApplication([])

lv = LiveVideo()

ui = UILiveSystem()

w = MainWindow()

ui.make_connection(lv)

# lv.make_connection(ui)

lv.make_connection(w)



sys.exit(app.exec_())