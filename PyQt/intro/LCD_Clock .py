"""
35:LCD Clock
------------------------------------
https://www.youtube.com/watch?v=CcnsV4qlBGQ&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=35
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/lcd.py
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/lcd.ui
https://github.com/flatplanet/pyqt5_youtube_playlist
6:30


"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel,\
    QWidget, QLCDNumber

# noinspection PyUnresolvedReferences
from PyQt5 import uic# Add the above line so uic is imported

import sys
from PyQt5.QtCore import QTime, QTimer
from datetime import datetime

#----------------------------------
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("lcd.ui", self)
 #-----------------------------------------------
        # Define our widgets
        self.lcd = self.findChild(QLCDNumber, "lcdNumber")


        # Create A Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_number)
        # Start the timer and update every second
        self.timer.start(1000)
        # Call the lcd function
        #self.lcd_number()
#-----------------------------------------------

        self.show()
#----------------------
    def lcd_number(self):
        time = datetime.now()
        formatted_time = time.strftime("%I:%M:%S %p")
        # Set number of LCD Digits
        self.lcd.setDigitCount(12)
        # Make Text Flat (no white outline)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)

        # Display The Time
        self.lcd.display(formatted_time)
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
