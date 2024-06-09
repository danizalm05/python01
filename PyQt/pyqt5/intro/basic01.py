"""
Basic skelton
------------------------------------
https://www.youtube.com/watch?v=5yyD-dQojC4&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=31
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/toe.py
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/toe.ui
https://github.com/flatplanet/pyqt5_youtube_playlist

4:20
"""
 
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("tictac.ui", self)

        self.show()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
