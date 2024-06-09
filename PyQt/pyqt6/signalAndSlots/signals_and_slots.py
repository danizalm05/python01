'''
Create GUI Applications with Python & Qt6
Martin Fitzpatrick
page 22 - 28

'''

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)  # <1>

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # <2>
        self.button_is_checked = True #Set the default value for our variable.
        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")



        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)#Use the default value to set the initial state of the widget.
        # Set the central widget of the Window.
        self.setCentralWidget(self.button)
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print("the_button_was_released ",self.button_is_checked)

    def the_button_was_clicked(self):
        print("Clicked!")
    def the_button_was_toggled(self, checked):
        #toggle signal for button,the signals send data (checked =True or False)
        print("Checked?", checked)
        self.button_is_checked = checked
        print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
