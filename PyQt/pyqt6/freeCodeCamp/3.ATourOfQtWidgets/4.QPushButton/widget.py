'''
 Learn Python GUI Development for Desktop – PySide6 and Qt Tutorial

https://www.youtube.com/watch?v=Z1N9JzNax2k&t=3s 
https://github.com/rutura/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals-/blob/main/3.ATourOfQtWidgets/4.QPushButton/widget.py



01:59: -   1:59 :00
'''
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom MainWindow")

        button = QPushButton("Click")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def button_clicked(self):
        print("Clicked")
    def button_pressed(self): 
        print("Pressed")
    def button_released(self):
        print("Released")