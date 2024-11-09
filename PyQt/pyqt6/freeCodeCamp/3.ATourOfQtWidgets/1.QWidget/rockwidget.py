'''
 window with two buttons

rockwidget.py

https://github.com/rutura/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals-/blob/main/3.ATourOfQtWidgets/1.QWidget/rockwidget.py
https://www.youtube.com/watch?time_continue=3&v=Z1N9JzNax2k&embeds_referring_euri=https%3A%2F%2Fduckduckgo.com%2F
'''
from PySide6.QtWidgets import QWidget,QPushButton,QHBoxLayout,QVBoxLayout

class RocWidget (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.button2_clicked)


        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)

    def button1_clicked(self):
        print("Button1 clicked")

    def button2_clicked(self):
        print("Button2 clicked")