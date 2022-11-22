"""
34: Calendar Widget
------------------------------------
https://www.youtube.com/watch?v=dx_5UvjAJVQ&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=34
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/cal.py
https://github.com/flatplanet/pyqt5_youtube_playlist
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/cb.ui


"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,  QCalendarWidget,\
    QLabel, QWidget

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
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.label = self.findChild(QLabel, "label")

#-----------------------------------------------
        self.calendar.selectionChanged.connect(self.grab_date)
        self.show()
#----------------------
    def grab_date(self):
       dateSelected = self.calendar.selectedDate()

       # Put Date On Label
       #self.label.setText(str(dateSelected.toPyDate()))
       self.label.setText(str(dateSelected.toString()))

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
