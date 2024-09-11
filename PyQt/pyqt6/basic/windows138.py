"""
Create GUI Applications with Python & Qt6
The hands-on guide to making apps with Python
Martin Fitzpatrick
138-140
"""

import sys
from random import randint
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))


        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    # tag::show_new_window[]
    """
    creating second window inside this method, storing it in the variable
     w and showing it. However, once we leave this method the w variable will
      be cleaned up by Python, and the window destroyed. To fix this we need 
      to keep a reference to the window somewhere — on the main window 
      self object 
    """
    def show_new_window(self, checked):
        self.w = AnotherWindow()
        self.w.show()

    # end::show_new_window[]


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

