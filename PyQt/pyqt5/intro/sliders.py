"""
40 Horizontal Sliders
------------------------

https://www.youtube.com/watch?v=lQ4KVj-EVOk&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=40
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/slide.py

3:00

"""
from PyQt5.QtWidgets import QMainWindow, QApplication,\
                            QSlider, QLabel
from PyQt5 import QtCore
import sys
# noinspection PyUnresolvedReferences
from PyQt5 import uic  # Add the above line so uic is imported


class UI(QMainWindow):
 def __init__(self):
    super(UI, self).__init__()

    # Load the ui file
    uic.loadUi("slide.ui", self)
    self.setWindowTitle("Slider!")

    # Define our widgets
    self.slider = self.findChild(QSlider, "horizontalSlider")
    self.label = self.findChild(QLabel, "label")
    self.slider01 = self.findChild(QSlider, "verticalSlider")
    self.label02 = self.findChild(QLabel, "label_2")
    # center the label
    self.label.setAlignment(QtCore.Qt.AlignCenter)

    # Set horoz Slider Properties
    self.slider.setMinimum(0)
    self.slider.setMaximum(50)
    self.slider.setValue(0)
    self.slider.setTickPosition(QSlider.TicksAbove)
    self.slider.setTickInterval(5)
    self.slider.setSingleStep(5)
    # Set vertical  Slider Properties
    self.slider01.setMinimum(0)
    self.slider01.setMaximum(50)
    self.slider01.setValue(0)
    self.slider.setTickPosition(QSlider.TicksLeft)


    self.slider.valueChanged.connect(self.slide_it)
    self.slider01.valueChanged.connect(self.slide01_it)
    self.show()
 def slide_it(self, value):
       self.label.setText(str(value))
 def slide01_it(self, value):
    self.label02.setText(str(value))

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()