# -*- coding: utf-8 -*-

import os
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import cv2
import getpass

from PyQt5.QtGui import QPixmap

vid_name = "n.mp4" #"n.mp4" "l.mkv"

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        #Initilize  Video file
        video_file = self.readImagePath() + vid_name#Create path to the video
        print(video_file)
        self.cap = cv2.VideoCapture(video_file)
        self.intVideo()
        self.currentFrame= np.zeros((3, 3, 3), np.uint8)
        self.frameNum =30
        self.fps = 1
        self.disply_width = 2640
        self.display_height = 1480



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2176, 1561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(30, 30, 2321, 1200))
        self.image_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.image_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")

        self.loadFrame_button = QtWidgets.QPushButton(self.centralwidget,
                                                      clicked = lambda: self.timeframe()
                                                      )
        self.loadFrame_button.setGeometry(QtCore.QRect(30, 1250, 201, 121))
        self.loadFrame_button.setObjectName("loadFrame_button")


        self.up_button = QtWidgets.QPushButton(self.centralwidget,
                                      clicked = lambda: self.upframe()
                                               )
        self.up_button.setGeometry(QtCore.QRect(40, 1410, 201, 121))
        self.up_button.setObjectName("up_button")
        self.down_button = QtWidgets.QPushButton(self.centralwidget)
        self.down_button.setGeometry(QtCore.QRect(280, 1410, 201, 121))
        self.down_button.setObjectName("down__button")


        self.up100_button = QtWidgets.QPushButton(self.centralwidget,
                                 clicked = lambda: self.up100frame())
        self.up100_button.setGeometry(QtCore.QRect(760, 1410, 201, 121))
        self.up100_button.setObjectName("up100_button")


        self.down100_button = QtWidgets.QPushButton(self.centralwidget)
        self.down100_button.setGeometry(QtCore.QRect(980, 1410, 201, 121))
        self.down100_button.setObjectName("down100_button")

       #def saveframe(self):
        self.save_button = QtWidgets.QPushButton(self.centralwidget,
                                    clicked = lambda: self.saveframe()
                                                 )
        self.save_button.setGeometry(QtCore.QRect(1890, 1410, 201, 121))
        self.save_button.setObjectName("save_button")

        self.FrameNumEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.FrameNumEdit.setGeometry(QtCore.QRect(270, 1260, 501, 111))
        self.FrameNumEdit.setPlainText("1_28_00")
        font = QtGui.QFont()
        font.setPointSize(24)
        self.FrameNumEdit.setFont(font)
        self.FrameNumEdit.setObjectName("frame_num_edit")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2176, 56))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.readVideoImage()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.loadFrame_button.setText(_translate("MainWindow", "Load Frame"))
        self.up_button.setText(_translate("MainWindow", "Up"))
        self.down_button.setText(_translate("MainWindow", "Down"))
        self.up100_button.setText(_translate("MainWindow", "Up100"))
        self.down100_button.setText(_translate("MainWindow", "Down100"))
        self.save_button.setText(_translate("MainWindow", "Save"))

    def readImagePath(self):
        BASE_FOLDER = 'C:/Users/'+ getpass.getuser()

        BASE_FOLDER = BASE_FOLDER +'/Videos/Captures/'
        path = BASE_FOLDER
        print("readImagePath  ",path)
        return path

    def up100frame(self):
        self.frameNum =   self.frameNum +100
        seconds = int(self.frameNum/int(self.fps))
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        t = f'{h:d}_{m:02d}_{s:02d}'
        self.FrameNumEdit.setPlainText(t)
        self.readVideoImage()


    def upframe(self):

        self.frameNum =   self.frameNum +1

        seconds = int(self.frameNum/int(self.fps))
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        t = f'{h:d}_{m:02d}_{s:02d}'
        self.FrameNumEdit.setPlainText(t)
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

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""

        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)

        return QPixmap.fromImage(p)

    def timeframe(self):
        time_str = self.FrameNumEdit.toPlainText()
        """Get seconds from time."""
        h, m, s = time_str.split('_')
        print ( h, m, s)
        t = (int(h) * 3600 + int(m) * 60 + int(s))*int(self.fps)
        print(t)
        self.frameNum = t
        ###self.frameNumber.setPlainText(str(t))
        self.readVideoImage()

    def saveframe(self):

      base = os.path.splitext(vid_name)[0] + '-'
      t = self.FrameNumEdit.toPlainText()

      print(t)
      video_file_name = self.readImagePath()+'/pic/' + base +t+'.jpg'

      frame  = cv2.resize(self.currentFrame, None, fx=4,
                      fy=4, interpolation=cv2.INTER_AREA)

      cv2.imwrite(video_file_name, frame)
      print("Save image to  " + video_file_name)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
