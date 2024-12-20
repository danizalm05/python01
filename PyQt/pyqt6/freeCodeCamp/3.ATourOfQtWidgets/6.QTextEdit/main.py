"""
 
 Learn Python GUI Development for Desktop – PySide6 and Qt Tutorial
  6.QTextEdit/

https://www.youtube.com/watch?v=Z1N9JzNax2k&t=3s 

https://github.com/rutura/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals-/tree/main/3.ATourOfQtWidgets/6.QTextEdit

https://doc.qt.io/qtforpython-6.5/PySide6/QtWidgets 
02:24:00
"""
from PySide6.QtWidgets import QApplication
from widget import Widget
import sys
 
 

app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()

QApplication.shutdown(app)
 