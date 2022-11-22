'''
Grabe a frame from a video  file
https://www.youtube.com/watch?v=p6Q2-m9i4Fg&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=28
How To Load PYQT5 Designer UI File
9:42
 PyShine
menu actions
https://www.youtube.com/watch?v=Vz0s-w4hksY&list=PLjPKPFvkBtZqKg8ugYihcxkWfnIDcwR4K&index=2

Control GUI Widgets: PyQt5 tutorial - Part 03
https://www.youtube.com/watch?v=co4ymeb3FRc&list=PLjPKPFvkBtZqKg8ugYihcxkWfnIDcwR4K&index=3
4:40 Edit Signalss  slots
'''
import os

import numpy as np



from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, \
    QSpinBox, QStatusBar,QSlider
from PyQt5.QtGui import QPixmap,  QFont
from PyQt5.QtCore import Qt

# noinspection PyUnresolvedReferences
from PyQt5 import uic
import sys
import getpass
import cv2





vid_name = "m.mkv" #"5.mkv"#"dog.mp4" #"4.mp4"


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        video_file = self.readImagePath() + vid_name#Create path to the video
        print(video_file)

        self.cap = cv2.VideoCapture(video_file)
        self.intVideo()
        self.currentFrame= np.zeros((3, 3, 3), np.uint8)
        self.frameNum =15
        self.fps = 1
        self.disply_width = 2040
        self.display_height = 980

        # Load the ui file framegrab.ui
        uic.loadUi("framegrab.ui", self)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)


        # Define Our Widgets

        self.imageLabel = self.findChild(QLabel, "imageLabel")
        self.imageLabel.resize(self.disply_width, self.display_height)
        self.upButton = self.findChild(QPushButton, "upButton")
        self.downButton = self.findChild(QPushButton, "downButton")
        self.up100 = self.findChild(QPushButton, "up100Button")
        self.down100 = self.findChild(QPushButton, "down100Button")

        self.scanSlider = self.findChild(QSlider, "scan_Slider")
        self.frameScanLabel = self.findChild(QLabel, "frame_scan_label")


        self.loadFrame = self.findChild(QPushButton, "loadFrameButton")
        self.saveFrame = self.findChild(QPushButton, "saveFrameButton")
        #Time  spinners
        self.hourFrame = self.findChild(QSpinBox, "hourSpin")
        self.minFrame = self.findChild(QSpinBox, "minSpin")
        self.minFrame.setMaximum(59)
        self.secFrame = self.findChild(QSpinBox, "secSpin")
        self.secFrame.setMaximum(59)

        # Do something


        self.upButton.clicked.connect(self.upButtonClk)
        self.downButton.clicked.connect(self.downButtonClk)
        self.up100.clicked.connect(self.up100Clk)
        self.down100.clicked.connect(self.down100Clk)

        self.scanSlider.valueChanged.connect(self.scanSliderClk)
        self.loadFrame.clicked.connect(self.loadFrameclk)
        self.saveFrame.clicked.connect(self.saveFrameclk)

        self.readVideoImage()
        self.show()

    def scanSliderClk(self):
        scanPr = int(self.frameScanLabel.text())/100

        totalframecount = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.frameNum = scanPr * totalframecount

        self.readVideoImage()
    def saveFrameclk(self):
        base = os.path.splitext(vid_name)[0] + '-'
        t = str(int(self.frameNum))
        video_file_name = self.readImagePath()+'frame/' + base +t+'.jpg'
        frame  = cv2.resize(self.currentFrame, None, fx=4,
                            fy=4, interpolation=cv2.INTER_AREA)
        cv2.imwrite(video_file_name, frame)
        print("Save image to  " + video_file_name)

    def loadFrameclk(self):
        #Read Frame time from spinBoxs
        frameTime = self.hourFrame.value()*3600 + self.minFrame.value()*60 + self.secFrame.value()
        totalframecount =  self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.frameNum =  frameTime/self.duration * totalframecount


        self.readVideoImage()

    def up100Clk(self):
        self.frameNum =   self.frameNum +100
        self.readVideoImage()
    def down100Clk(self):
        self.frameNum =   self.frameNum -100
        self.readVideoImage()
    def upButtonClk(self):
        self.frameNum =   self.frameNum +1
        self.readVideoImage()
    def downButtonClk(self):
        self.frameNum =   self.frameNum -1
        self.readVideoImage()
    def intVideo(self):
        wd = 1800
        hg = 1000
        self.cap.set(3, wd)
        self.cap.set(4, hg)

        #  Video file data
        dim = 'Width: ' + str(self.cap.get(3)) + ' Height:' + str(self.cap.get(4))
        print(dim)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        print("FPS : '{}'".format(int(self.cap.get(cv2.CAP_PROP_FPS))))
        self.totalframecount = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f'Total frame count = {self.totalframecount} ')
        self.duration = self.totalframecount/self.fps
        print('duration (S) = ' + str(int(self.duration))+' [sec]')
        hour = self.duration/60/60
        print('duration (h) = ' + str(hour)+' [h]')




    def readImagePath(self):
        BASE_FOLDER = 'C:/Users/'+ getpass.getuser()

        BASE_FOLDER = BASE_FOLDER +'/Videos/Captures/'
        path = BASE_FOLDER

        return path
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)

        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w

        Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        keep_aspect_ratio = 2
        p = Qt_format.scaled(self.disply_width, self.display_height,keep_aspect_ratio)

        return QPixmap.fromImage(p)


    def readVideoImage (self):

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.cap.set(1,  self.frameNum)
        ret, frame = self.cap.read()
        self.currentFrame = frame

        qt_img = self.convert_cv_qt(frame)
        self.imageLabel.setPixmap(qt_img)


        seconds = int(self.frameNum/int(self.fps))
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        t = f'Time = {h:d}:{m:02d}:{s:02d}  Frame={int(self.frameNum)} / {self.totalframecount}'
        self.statusBar.showMessage(t)

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

