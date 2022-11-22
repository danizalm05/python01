'''
image processing opencv  PyQt
https://www.youtube.com/watch?v=6zkOrq9YVik&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=30
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/image.py
2:37
'''

import getpass
import cv2 as cv
import numpy as np
from PIL import ImageQt
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFileDialog, QPushButton, \
    QMenu, QAction, QSlider
# noinspection PyUnresolvedReferences
from PyQt5 import uic, QtGui, Qt, QtCore  # Add the above line so uic is imported
from PyQt5.QtGui import QPixmap, QIcon
import sys

imgName = '1.jpg'
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.disply_width = 1740
        self.display_height = 1580
        # Load the ui file
        uic.loadUi("loadImage.ui", self)

        # Define Our Widgets
        self.imagelabel = self.findChild(QLabel, "imageLabel")
        self.resizeImgbutton = self.findChild(QPushButton, "resizeButton")
        self.featureImgbutton = self.findChild(QPushButton, "featuresButton")


        ####contrast slider
        self.contrastLabel = self.findChild(QLabel, "contrastLabel")
        self.contrsSlider = self.findChild(QSlider, "contrsSlider")
        self.contrsSlider.valueChanged[int].connect(self.contrsSliderClk)
        self.contrsSlider.sliderReleased.connect(self.sliderReleased)

        ####ThresholdlSlider slider
        self.Thrholdlabel = self.findChild(QLabel, "Thrholdlabel")
        self.ThresholdlSlider = self.findChild(QSlider, "ThresholdlSlider")
        self.ThresholdlSlider.valueChanged[int].connect(self.ThresholdlSliderClk)
        self.ThresholdlSlider.sliderReleased.connect(self.sliderReleased)

        #maxCornerSlider
        self.maxCorner=50
        self.maxCornerlabel = self.findChild(QLabel, "maxCornerlabel")
        self.maxCornerSlider = self.findChild(QSlider, "maxCornerSlider")
        self.maxCornerSlider.valueChanged[int].connect(self.maxCornerSliderClk)

        #blockSizeSlider

        self.blockSize = 10
        self.blockSizelabel = self.findChild(QLabel, "blockSizelabel")
        self.blockSizeSlider = self.findChild(QSlider, "blockSizeSlider")
        self.blockSizeSlider.valueChanged[int].connect(self.blockSizeSliderClk)

        # minDistSlider
        self.minDistance = 15
        self.minDistlabel = self.findChild(QLabel, "minDistlabel")
        self.minDistSlider = self.findChild(QSlider, "minDistSlider")
        self.minDistSlider.valueChanged[int].connect(self.minDistSliderClk)

        # qualitySlider
        self.qualityLevel = 0.001
        self.qualitylabel = self.findChild(QLabel, "qualitylabel")
        self.qualitySlider = self.findChild(QSlider, "qualitySlider")
        self.qualitySlider.valueChanged[int].connect(self.qualitySliderClk)


        #########################   Main  Menu   #######################
        # main menu Edit
        self.menuEdit = self.findChild(QMenu, "menuEdit")
        #Brightness
        brightAction = QAction(QIcon('bright.png'), 'bright', self)
        self.menuEdit.addAction(brightAction)
        brightAction.triggered.connect(self.brightclk)
        #hsv
        hsvAction = QAction(QIcon('hsv.png'), 'hsv', self)
        self.menuEdit.addAction(hsvAction)
        hsvAction.triggered.connect(self. hsvclk)

        # main menu File
        self.menuFile = self.findChild(QMenu, "menuFile")

        #Load Image
        openAction = QAction(QIcon('open.png'), 'Open', self)
        openAction.setShortcut('Ctrl+o')
        openAction.setStatusTip('Load Image')
        self.menuFile.addAction(openAction)
        openAction.triggered.connect(self.loadImbclk)

        # Save Image
        saveAction = QAction(QIcon('save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+s')
        self.menuFile.addAction(saveAction)
        saveAction.triggered.connect(self.saveImbclk)




        #Load default  image

        self.img00 = cv.imread(self.readImagePath() + imgName, cv.IMREAD_COLOR)
        self.img01 = self.convert_cv_qt(self.img00)
        self.imageLabel.setPixmap(self.img01)

     # Do something
        self.resizeImgbutton.clicked.connect(self.resizeImbclk)
        self.featureImgbutton.clicked.connect(self.featureImbclk)
        # Show The App
        self.show()
    ####################   end of  def __init__(self):################
    def minDistSliderClk(self,distance):
        self.minDistance = distance
        c = str(round( self.minDistance, 2))
        self.minDistlabel.setText("Dist " + c)
        self.featureImbclk()


    def qualitySliderClk(self,qulity):
        self.qualityLevel = qulity/10000
        c = str(round( self.qualityLevel, 2))
        self.qualitylabel.setText("qual " + c)
        self.featureImbclk()

    def blockSizeSliderClk(self,bsize):
        self.blockSize = bsize
        c = str(round(bsize, 2))
        self.blockSizelabel.setText("bsize " + c)
        self.featureImbclk()

    def maxCornerSliderClk(self, maxC ):

         self.maxCorner = maxC*4
         c = str(round( self.maxCorner, 2))

         self.maxCornerlabel.setText("maxCor " + c)
         self.featureImbclk()


    def featureImbclk(self):
      print (self.minDistance,  self.qualityLevel )


      im = self.img00.copy()
      gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
       # Find the top  corners using the cv2.goodFeaturesToTrack()
      corners = cv.goodFeaturesToTrack(gray, self.maxCorner, self.qualityLevel,
                                       self.minDistance,self.blockSize)
      print(self.blockSize)
      corners = np.int0(corners)
      for i in corners:
          x, y = i.ravel()
          cv.circle(im, (x, y), 5, (0, 250, 5), -1)

      qt_img = self.convert_cv_qt(im)
      self.imageLabel.setPixmap(qt_img)







    def ThresholdlSliderClk(self, Threshold):

        retval, self.img01 = cv.threshold(self.img00, Threshold, 255, cv.THRESH_BINARY)
        qt_img = self.convert_cv_qt(self.img01)
        self.imageLabel.setPixmap(qt_img)

        c = str(round(Threshold, 2))
        self.Thrholdlabel.setText("Thres " + c)  # Print  contrast value

    def contrsSliderClk(self, contrst):
       contrst = 0.01 + contrst/20

       matrix1 = np.ones(self.img00.shape) * (contrst)
       #self.img01 = np.uint8(cv.multiply(np.float64(self.img00), matrix1))
       self.img01 = np.uint8(np.clip(cv.multiply(np.float64(self.img00), matrix1), 0, 255))
       qt_img = self.convert_cv_qt(self.img01)
       self.imageLabel.setPixmap(qt_img)
       c= str(round(contrst, 2))
       self.contrastLabel.setText("Contrs " + c) # Print  contrast value


    def sliderReleased(self):

        self.img00 = self.img01.copy()


    def brightclk(self):

        matrix = np.ones( self.img00.shape, dtype="uint8") * 50
        self.img00 = cv.add( self.img00, matrix)
        qt_img = self.convert_cv_qt(self.img00)
        self.imageLabel.setPixmap(qt_img)

    def resizeImbclk(self):

       self.img00 = cv.resize(self.img00, None, fx=2, fy=2)
       qt_img = self.convert_cv_qt(self.img00)
       self.imageLabel.setPixmap(qt_img)



    def hsvclk(self):
        if(len(self.img00.shape) == 3):
          img_hsv = cv.cvtColor(self.img00, cv.COLOR_BGR2HSV)
          h, s, v = cv.split(img_hsv)
          self.img00 = v
          qt_img = self.convert_cv_qt(self.img00)
          self.imageLabel.setPixmap(qt_img)



    def loadImbclk(self):

        fname = QFileDialog.getOpenFileName(self, "Open File", self.readImagePath(),
                               "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")

        if (fname[0]!= '') :
            self.img00 = cv.imread(fname[0], cv.IMREAD_COLOR)
            qt_img = self.convert_cv_qt( self.img00)
            self.imageLabel.setPixmap(qt_img)



    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""

        rgb_image = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w

        Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        keep_aspect_ratio =2
        p = Qt_format.scaled(self.display_height,  self.disply_width, keep_aspect_ratio)
        return QPixmap.fromImage(p)


    def saveImbclk(self):

       image = ImageQt.fromqpixmap(self.imagelabel.pixmap())
       fname = QFileDialog.getSaveFileName(self, 'Save File', self.readImagePath(),
                                            "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")
       image.save(fname[0])


    def readImagePath(self):
      BASE_FOLDER = 'C:/Users/' + getpass.getuser()
      BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
      path = BASE_FOLDER
      return path

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

