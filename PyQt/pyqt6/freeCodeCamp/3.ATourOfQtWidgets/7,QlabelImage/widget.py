'''
        5.QLabel_QLineEdit

 Learn Python GUI Development for Desktop – PySide6 and Qt Tutorial

https://www.youtube.com/watch?v=Z1N9JzNax2k&t=3s 

https://github.com/rutura/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals-/blob/main/3.ATourOfQtWidgets/7.QLabel_Images/widget.py
https://doc.qt.io/qtforpython-6.5/PySide6/QtWidgets/QTextEdit.html

  02:41:00   02:   
''' 

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QPushButton
import getpass

USER = getpass.getuser()

IMAGE_NAME = 'Osteosarcoma_01.tif'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME
print(IMAGE)

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle(IMAGE)

        image_label = QLabel()
        image_label.setPixmap(QPixmap(IMAGE))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)