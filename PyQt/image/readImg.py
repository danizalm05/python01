#Display image with QtLabel

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QColor, QFont
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt,QObject
import sys
import cv2
import getpass



imgName = 'a1.jpg'  #"cat-face.png"



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Image Operation")
        self.disply_width = 1640
        self.display_height = 2480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        # create a text label
        self.textLabel = QLabel('Read Image Demo')
        self.textLabel.setFont(QFont('Helvetica', 22))

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)

        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # load the test image
        img_name = self.readImagePath(imgName)#Create pathe to the image file
        cv_img = cv2.imread(img_name)

        print("Top left pixel",  cv_img[1,1])    #Top left pixel

        # convert the image to Qt format
        qt_img = self.convert_cv_qt(cv_img)
        # display it
        self.image_label.setPixmap(qt_img)


    def readImagePath(self,imgName):
        BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
        BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
        path = BASE_FOLDER+imgName
        print(path)

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