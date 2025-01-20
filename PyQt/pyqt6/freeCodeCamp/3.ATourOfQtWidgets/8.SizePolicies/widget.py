'''
      8.SizePolicies

 Learn Python GUI Development for Desktop – PySide6 and Qt Tutorial

https://www.youtube.com/watch?v=Z1N9JzNax2k&t=3s 

https://github.com/rutura/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals-/blob/main/3.ATourOfQtWidgets/8.SizePolicies/widget.py
 

  02:41:00   03:00:00 
      
from tkinter import Label
from PySide6.QtWidgets import QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy, QLineEdit, QPushButton
      
      
      
      
''' 

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy,  QLineEdit,QPushButton
import getpass

USER = getpass.getuser()

IMAGE_NAME = 'Osteosarcoma_01.tif'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME
print(IMAGE)


class Widget(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("Size policies and stretches")

        #Size policy : how the widgets behaves if container space is expanded or shrunk.
        label = QLabel("Some text : ")
        line_edit = QLineEdit()

        line_edit.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)


        button_1 = QPushButton("1One")
        button_2 = QPushButton("2Two")
        button_3 = QPushButton("3Three")

        #stretch : how much of the available space (in the layout) is occupied by each widget.
        #You specify the stretch when you add things to the layout : button_1 takes up 2 units ,
        # button_2 and button_3 each take up 1 unit
        
        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button_1,2)
        h_layout_2.addWidget(button_2,1)
        h_layout_2.addWidget(button_3,1)


        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)
        
        self.setLayout(v_layout)









'''
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle(IMAGE)

        image_label = QLabel()
        image_label.setPixmap(QPixmap(IMAGE))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)
        
'''        