"""
Exterct a frame from video file

 """
import getpass
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2


vid_name = "l.mkv" #"l.mkv"   #"m.mp4" "dog.mp4"
MainFrame =320000


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()


        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)


        self.framelBTN = QPushButton("Feame")
        self.framelBTN.clicked.connect(self.moveToFrame)
        self.VBL.addWidget(self.framelBTN)


        # Create an entry box
        self.my_entry = QLineEdit()
        self.my_entry.setObjectName("name_field")
        self.my_entry.setText("1234")
        self.VBL.addWidget(self.my_entry)

        self.Worker1 = Worker1( )
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)



    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def moveToFrame(self):

        self.MainFrame = self.my_entry.text()
        print("elf.MainFrame ",self.MainFrame)
        #return x


    def CancelFeed(self):
        self.Worker1.stop()
##################################################


class Worker1(QThread ):
    ImageUpdate = pyqtSignal(QImage)
    
    def run(self):
        font = cv2.FONT_HERSHEY_SIMPLEX
        self.ThreadActive = True
        input_video_file = self.readImagePath()
        cap = cv2.VideoCapture(input_video_file)

        wd = 1800
        hg = 1000
        cap.set(3, wd)
        cap.set(4, hg)

        self.vidData(cap)



        while self.ThreadActive:


            #print(i)
            cap.set(1, MainFrame )
            ret, frame = cap.read()

            if ret:
                img = self.process(frame)
                ConvertToQtFormat = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(wd, hg, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)


    def  process(self,frame):
         imgP = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
         return imgP

    def vidData(self,cap0):
          #  Video file data
        dim = 'Width: ' + str(cap0.get(3)) + ' Height:' + str(cap0.get(4))
        print(dim)

        fps = cap0.get(cv2.CAP_PROP_FPS)
        fps =("FPS : '{}'".format(int(cap0.get(cv2.CAP_PROP_FPS))))
        print(fps)
        totalframecount = int(cap0.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f'Total frame count = {totalframecount} ')

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