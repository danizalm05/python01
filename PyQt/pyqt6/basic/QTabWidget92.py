'''
QTabWidget
Create GUI Applications with Python & Qt6 / Martin Fitzpatrick

Listing 35. basic/layout_9.py
#page  92    /88
'''

import sys
from PySide6.QtCore import Qt,QSize

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
)
from layout_colorwidget import Color
class MainWindow(QMainWindow):
    def __init__(self):
      super().__init__()
      self.setWindowTitle("My App")
      tabs = QTabWidget()
      tabs.setTabPosition(QTabWidget.West)
      tabs.setMovable(True)
      for n, color in enumerate(["red", "green", "blue", "yellow"]):
           tabs.addTab(Color(color), color)
      self.setCentralWidget(tabs)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()