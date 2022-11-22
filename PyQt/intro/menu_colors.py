"""
33: Change Background Color With Menu
------------------------------------
https://www.youtube.com/watch?v=FgvZTJYITGg&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=33

https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/colors.py
https://github.com/flatplanet/pyqt5_youtube_playlist

02:00
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget
from PyQt5 import uic
import sys

#----------------------------------
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("menu_colors.ui", self)
 #-----------------------------------------------
        # <addaction name="actionWhite"/>
        #     <addaction name="actionBlack"/>
        #     <addaction name="actionRed"/>
        self.actionBlack.triggered.connect(lambda: self.change("black"))
        self.actionWhite.triggered.connect(lambda: self.change("white"))
        self.actionRed.triggered.connect(lambda: self.change("red"))
#-----------------------------------------------
        self.show()
#----------------------
    def change(self, color):
        # Change BG color
        self.setStyleSheet(f"background-color: {color};")
        # Change The Title
        self.setWindowTitle(f"You Changed The Color To {color}")
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
