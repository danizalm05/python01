#Read one frame from a video file and display it with QtLabel
import datetime
import os

import numpy as np
from PyQt5 import  QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QTextEdit, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap,  QFont
from PyQt5.QtCore import Qt
import sys
import cv2
import getpass

vid_name = "3.mov"#"l.mkv"#"dog.mp4" #"r.mp4"

class App(QWidget):
    def __init__(self):
        super().__init__()
        #Initilize  Video file
        video_file = self.readImagePath() + vid_name#Create path to the video
        print(video_file)
        self.cap = cv2.VideoCapture(video_file)
        self.intVideo()

        self.currentFrame= np.zeros((3, 3, 3), np.uint8)
        self.frameNum =34
        self.fps = 1
        ##############################################
        self.setWindowTitle("Read Frame Operation")
        self.disply_width = 1980
        self.display_height = 980
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)

        # create a text label
        self.textLabel = QLabel('Read Image Demo')
        self.textLabel.setFont(QFont('Helvetica', 18))
        #self.frameNumber = QLineEdit(self)

        self.frameNumber = QTextEdit(self,
                                plainText="",
                                #html = "<center><h1><em>Big Header Text!</em></h1></center>",
                                acceptRichText= False,
                                lineWrapMode=QTextEdit.FixedColumnWidth,
                                lineWrapColumnOrWidth=35,
                                placeholderText="Input Frame Number",
                                readOnly=False,
                                )
        self.frameNumber.setFont(QFont('Helvetica', 18))
        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.frameNumber)
        vbox.addWidget(self.textLabel)

        up_100_frame_button = QPushButton("up",
                                   clicked = lambda: self.up100frame())
        vbox.addWidget(up_100_frame_button)

        time_frame_button = QPushButton("time frame",
                                          clicked = lambda: self.timeframe())
        vbox.addWidget(time_frame_button)


        save_button = QPushButton("Save",
                                        clicked = lambda: self.saveframe())
        vbox.addWidget(save_button)

        # set the vbox layout as the widgets layout
        self.setLayout(vbox)
        self.readVideoImage()
########################################################

    def saveframe(self):
        base = os.path.splitext(vid_name)[0] + '-'
        t = self.frameNumber.toPlainText()
        video_file_name = self.readImagePath()+'frame/' + base +t+'.jpg'

        frame  = cv2.resize(self.currentFrame, None, fx=4,
                             fy=4, interpolation=cv2.INTER_AREA)

        cv2.imwrite(video_file_name, frame)
        print("Save image to  " + video_file_name)




    def timeframe(self):
        time_str = (self.frameNumber.toPlainText())
        """Get seconds from time."""
        h, m, s = time_str.split('_')
        t = (int(h) * 3600 + int(m) * 60 + int(s))*int(self.fps)

        self.frameNum = t
        #self.frameNumber.setPlainText(str(t))
        self.readVideoImage()



    def up100frame(self):
        self.frameNum =   self.frameNum +100
        seconds = int(self.frameNum/int(self.fps))
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        t = f'{h:d}_{m:02d}_{s:02d}'
        print(t)
        self.frameNumber.setPlainText(t)
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
        totalframecount = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f'Total frame count = {totalframecount} ')

    def readVideoImage (self):

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.cap.set(1,  self.frameNum)
        ret, frame = self.cap.read()


        self.currentFrame = frame

        qt_img = self.convert_cv_qt(frame)
        self.image_label.setPixmap(qt_img)



    def readImagePath(self):
        BASE_FOLDER = 'C:/Users/'+ getpass.getuser()

        BASE_FOLDER = BASE_FOLDER +'/Videos/Captures/'
        path = BASE_FOLDER
        print("readImagePath  ",path)
        return path

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""

        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)

        return QPixmap.fromImage(p)

if __name__=="__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())