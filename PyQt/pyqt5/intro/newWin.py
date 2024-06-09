"""
36 Multiple Windows Inside Your App
------------------------------------
https://www.youtube.com/watch?v=CvWl-Rhy2wI&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=36
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/new_win.py
5:26
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, \
    QPushButton, QMdiArea, QLabel, QMdiSubWindow, QTextEdit

# noinspection PyUnresolvedReferences
from PyQt5 import uic# Add the above line so uic is imported

import sys


#----------------------------------
class UI(QMainWindow):
    count = 0
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("newWin.ui", self)
 #-----------------------------------------------
        # Define Our Widgets

        self.mdi = self.findChild(QMdiArea, "mdiArea")

        self.button = self.findChild(QPushButton, "pushButton")
        self.label = self.findChild(QLabel, "label")
        #-----------------------------------------------
        # Click Button
        self.button.clicked.connect(self.add_window)

#-----------------------------------------------

        self.show()
#----------------------
    def add_window(self):
        UI.count = UI.count + 1
        print("UI.count = ", UI.count)
        # Create Sub Windows
        sub = QMdiSubWindow()

        # Do stuff in the sub windows
        sub.setWidget(QTextEdit())
        # Set The Titlebar or the Sub Window
        sub.setWindowTitle("Subby Window " + str(UI.count))
        # Add The Sub Window Into Our MDI Widget
        self.mdi.addSubWindow(sub)
        # Show the new sub window
        sub.show()
        # Position the sub windows
        # tile them
        #self.mdi.tileSubWindows()
        # Cascade them
        self.mdi.cascadeSubWindows()
        # Do more fun stuff...
        # self.mdi.closeActiveSubWindow()
        # self.mdi.removeSubWindow()
        # self.mdi.subWindowList()

# Initialize The App


app = QApplication(sys.argv)


UIWindow = UI()
app.exec_()
