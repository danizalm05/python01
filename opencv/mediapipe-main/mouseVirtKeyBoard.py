#virtual keboard using mouse
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QTextEdit
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
import KeyBoardModule as Kb

scaling_factor = 2.5
massage = "--"

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()

        self.keybrd = Kb.KeyBoard(Kb.keyboard_keys, '')# Initialize the virtual keyboard
        self.buttonL = self.keybrd.CreateBtnlList()

        self._run_flag = True

    def run(self):
        # capture from web cam
        #keybrd = Kb.KeyBoard(Kb.keyboard_keys, '')# Initialize the virtual keyboard
        #buttonL = keybrd.CreateBtnlList()

        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        ret, img = cap.read()
        img_h, img_w = img.shape[:2]
        mask = np.zeros((img_h, img_w), dtype=np.uint8)
        cap.set(3, 1280)
        cap.set(4, 720)
        cv2.namedWindow('output')
        cv2.setMouseCallback('output', self.keybrd.key_clk)
       #########
        while self._run_flag:
            ######### Read keybord commands here
            ret, img = cap.read()

            img = cv2.flip(img, 1)
            x1 = 650
            x2=  40
            y2 = 160
            y1 = 420
            frame = mask[ y2 :y1, x2: x1]

            img01 = cv2.resize(frame, None, fx=scaling_factor,
                              fy=scaling_factor, interpolation=cv2.INTER_AREA)

            img01 = self.keybrd.DrawKeyBoard(img01, self.buttonL)

            if ret:
                cv2.imshow("output", img01)
                key = cv2.waitKey(1)
                global massage
                massage = self.keybrd.msg
                #print(massage)

                if key == ord('q'):
                     break
                self.change_pixmap_signal.emit(img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt live Virtual keyboard")


        self.disply_width = 1640
        self.display_height = 1480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        # create a text label
        #self.textLabel = QLabel('Webcam')
        font = QtGui.QFont()
        font.setPointSize(24)
        #self.textLabel.setFont(font)

        self.msgEdit = QTextEdit()
        self.msgEdit.setFont(font)

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        #vbox.addWidget(self.textLabel)
        vbox.addWidget(self.msgEdit)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()



    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

        #self.textLabel.setText(massage)
        self.msgEdit.setText(massage)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        #rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        rgb_image = cv2.cvtColor( cv_img, cv2.COLOR_BGR2RGB)


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