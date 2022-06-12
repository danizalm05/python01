"""
Embed An OpenCV Video Feed In A PyQt Window Using QThread
https://www.codepile.net/pile/ey9KAnxn
https://www.youtube.com/watch?v=dTDgbx-XelY

 """
import getpass
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2


vid_name = "m.mp4" #"l.mp4"   #"cars.mp4" "dog.mp4"



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
        font = cv2.FONT_HERSHEY_SIMPLEX
        self.ThreadActive = True
        input_video_file = self.readImagePath()
        Capture = cv2.VideoCapture(input_video_file)

        wd = 2800
        hg = 2000
        Capture.set(3, wd)
        Capture.set(4, hg)
        text = 'Width: ' + str(Capture.get(3)) + ' Height:' + str(Capture.get(4))
        fps =  Capture.get(cv2.CAP_PROP_FPS)
        fps =("FPS : '{}'".format(int(Capture.get(cv2.CAP_PROP_FPS))))

        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                edges = self.process(frame)

                FlippedImage = cv2.putText(edges, text, (10, 50), font, 1,
                                    (0, 255, 255), 2, cv2.LINE_AA)

                FlippedImage = cv2.putText(FlippedImage, fps, (10, 100), font, 1,
                                           (0, 255, 255), 2, cv2.LINE_AA)

                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(wd, hg, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def  process(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        Image = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
        img_gray = cv2.medianBlur(Image, 5)#reduce the noise by smoothing
        edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
        #FlippedImage = cv2.flip(edges, 1)




        return edges



    def readImagePath(self):
        BASE_FOLDER = 'C:/Users/' +  getpass.getuser() +'/Videos/Captures/'
        input_file = BASE_FOLDER + vid_name
        return input_file




    def stop(self):
        self.ThreadActive = False
        self.quit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())