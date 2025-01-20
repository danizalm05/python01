"""
8.SizePolicies
https://www.youtube.com/watch?v=Z1N9JzNax2k&t=3s 
https://github.com/rutura/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals-/blob/main/3.ATourOfQtWidgets/8.SizePolicies/main.py
 
02:48:00  03:00:00   
"""

from PySide6.QtWidgets import QApplication
from widget import Widget
import sys

app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()
QApplication.shutdown(app) 