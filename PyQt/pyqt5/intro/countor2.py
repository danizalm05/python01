"""

------------------------------------
https://www.youtube.com/watch?v=FgvZTJYITGg&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=33

https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/colors.py
https://github.com/flatplanet/pyqt5_youtube_playlist

02:00
"""
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic


from PyQt5 import QtGui

from PyQt5.QtGui import QPixmap, QIcon
import cv2
import sys
import getpass

BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #
mimg = "1.jpg"
image_path = BASE_FOLDER + mimg







class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.disply_width =900
        self.display_height = 1180

        # Load the ui file
        uic.loadUi("countor2.ui", self)

        # Define our widgets
        self.button = self.findChild(QPushButton, "pushButton")
        self.imageLabel = self.findChild(QLabel, "label")
        self.imageLabel.resize(self.disply_width, self.display_height)

        # Click The Dropdown Box
        self.button.clicked.connect(self.clicker)
        self.img = cv2.imread(image_path, cv2.IMREAD_COLOR)
        #############
        self.img = self.convert_cv_qt(self.img)
        self.imageLabel.setPixmap(self.img)

        ###############
        # Show The App
        self.show()



    def clicker(self):

        fname = QFileDialog.getOpenFileName(self,
                 "Open File", BASE_FOLDER, "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")

        # Open The Image
        if fname:
            self.img = cv2.imread( fname[0])


            qt_img = self.convert_cv_qt( self.img)
            self.imageLabel.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w

        Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        keep_ratio =2
        p = Qt_format.scaled(self.display_height,  self.disply_width, keep_ratio)
        return QPixmap.fromImage( p)




# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()