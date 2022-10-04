# -*- coding: utf-8 -*-

"""
How To Load PYQT5 Designer UI File   #27

https://www.youtube.com/watch?v=p6Q2-m9i4Fg&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=27
3:25
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/loadui.py
https://stackoverflow.com/questions/23248017/cannot-find-reference-xxx-in-init-py
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton

# noinspection PyUnresolvedReferences
from PyQt5 import uic  # Add the above line so uic is imported

import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("loadui.ui", self)

        # Define Our Widgets
        self.label = self.findChild(QLabel, "label")
        self.textedit = self.findChild(QTextEdit, "textEdit")
        self.button = self.findChild(QPushButton, "pushButton")
        self.clear_button = self.findChild(QPushButton, "pushButton_2")

        # Do something
        self.button.clicked.connect(self.clicker)
        self.clear_button.clicked.connect(self.clearer)

        # Show The App
        self.show()

    def clearer(self):
        self.textedit.setPlainText("")
        self.label.setText("Enter Your Name...")

    def clicker(self):
        self.label.setText(f'Hello There {self.textedit.toPlainText()}')
        self.textedit.setPlainText("")

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()