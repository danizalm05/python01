"""
Embed An OpenCV Video Feed In A PyQt Window Using QThread
https://www.codepile.net/pile/ey9KAnxn
https://www.youtube.com/watch?v=dTDgbx-XelY
3:00
 """
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        #
        wd = 2800
        hg = 2000
        Capture.set(3, wd)
        Capture.set(4, hg)
        text = 'Width: ' + str(Capture.get(3)) + ' Height:' + str(Capture.get(4))

        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                Image = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
                #smoothed =  cv2.GaussianBlur(Image, (9, 9), 10)
                # Apply median filter
                img_gray = cv2.medianBlur(Image, 5)#reduce the noise by smoothing
                # Detect edges using cv2.Laplacian()
                edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
                thresholded = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)

                font = cv2.FONT_HERSHEY_SIMPLEX

                FlippedImage =   cv2.flip(edges, 1)

                FlippedImage = cv2.putText(FlippedImage, text, (10, 50), font, 1,
                                    (0, 255, 255), 2, cv2.LINE_AA)

                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(wd, hg, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())