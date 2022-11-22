"""
 Basic initial pyqt 
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget

# noinspection PyUnresolvedReferences
from PyQt5 import uic# Add the above line so uic is imported


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

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
