'''
Grabe a frame from a video  file
https://www.youtube.com/watch?v=p6Q2-m9i4Fg&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=28
How To Load PYQT5 Designer UI File
9:42
'''
import numpy as np



from PyQt5 import  QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, \
    QSpinBox
from PyQt5.QtGui import QPixmap,  QFont
from PyQt5.QtCore import Qt

# noinspection PyUnresolvedReferences
from PyQt5 import uic
import sys
import getpass
import cv2





vid_name = "l.mkv"#"l.mkv"#"dog.mp4" #"r.mp4"


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        video_file = self.readImagePath() + vid_name#Create path to the video
        print(video_file)

        self.cap = cv2.VideoCapture(video_file)
        self.intVideo()
        self.currentFrame= np.zeros((3, 3, 3), np.uint8)
        self.frameNum =155334
        self.fps = 1
        self.disply_width = 1980
        self.display_height = 980
        # create the label that holds the image





        # Load the ui file framegrab.ui
        uic.loadUi("framegrab.ui", self)

        # Define Our Widgets


        #<widget class="QPushButton" name="upButton">
        self.upButton = self.findChild(QPushButton, "upButton")
        self.imageLabel = self.findChild(QLabel, "imageLabel")
        self.imageLabel.resize(self.disply_width, self.display_height)

        self.up100 = self.findChild(QPushButton, "up100Button")
        # <widget class="QPushButton" name="loadFrameButton">
        self.loadFrame = self.findChild(QPushButton, "loadFrameButton")

        #Time  spinners">
        self.hourFrame = self.findChild(QSpinBox, "hourSpin")
        self.minFrame = self.findChild(QSpinBox, "minSpin")
        self.minFrame.setMaximum(59)
        self.secFrame = self.findChild(QSpinBox, "secSpin")
        self.secFrame.setMaximum(59)
        # Do something

        self.upButton.clicked.connect(self.upButtonClk)
        self.up100.clicked.connect(self.up100Clk)
        self.loadFrame.clicked.connect(self.loadFrameclk)
        self.readVideoImage()
        self.show()

    def loadFrameclk(self):
        h = str(self.hourFrame.value())
        m = str(self.minFrame.value())
        s = str(self.secFrame.value())
        print(h,m,s)
    def up100Clk(self):
        self.frameNum =   self.frameNum +100
        seconds = int(self.frameNum/int(self.fps))
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        t = f'{h:d}_{m:02d}_{s:02d}'
        print(t)
        #self.frameNumber.setPlainText(t)
        self.readVideoImage()

    def upButtonClk(self):
        print("up  clicked")

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
        totalframecount = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f'Total frame count = {totalframecount} ')
        duration = totalframecount/self.fps
        print('duration (S) = ' + str(int(duration))+' [sec]')
        hour = duration/60/60
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

        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)

        return QPixmap.fromImage(p)


    def readVideoImage (self):

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.cap.set(1,  self.frameNum)
        ret, frame = self.cap.read()
        self.currentFrame = frame

        qt_img = self.convert_cv_qt(frame)
        self.imageLabel.setPixmap(qt_img)

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
'''


    def readImagePath(self):
        BASE_FOLDER = 'C:/Users/'+ getpass.getuser()

        BASE_FOLDER = BASE_FOLDER +'/Videos/Captures/'
        path = BASE_FOLDER
        print("readImagePath  ",path)
        return path
 '''
