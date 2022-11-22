"""
35:LCD Clock
------------------------------------
https://www.youtube.com/watch?v=CcnsV4qlBGQ&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=35
https://github.com/flatplanet/pyqt5_youtube_playlist



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
        uic.loadUi("cb.ui", self)
 #-----------------------------------------------
        # Define our widgets


#-----------------------------------------------

        self.show()
#----------------------


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
