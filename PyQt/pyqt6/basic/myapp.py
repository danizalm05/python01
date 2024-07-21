'''
myapp.py
'''


import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()