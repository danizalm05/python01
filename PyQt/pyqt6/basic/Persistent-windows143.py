"""
Create GUI Applications with Python & Qt6 - Martin Fitzpatrick

create the additional windows first, then use   .show() 
to display them when needed. we create our external window in the
 __init__ block for the main window, and then our show_new_window method 
 simply calls self.w.show() to display it.
143-
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
        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, is_checked):
        self.w.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
QApplication.shutdown(app)