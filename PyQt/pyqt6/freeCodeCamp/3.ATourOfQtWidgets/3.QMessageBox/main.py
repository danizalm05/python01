'''
 Learn Python GUI Development for Desktop – PySide6 and Qt Tutorial


https://www.youtube.com/watch?v=Z1N9JzNax2k&t=3s
https://github.com/rutura/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals-/tree/main/3.ATourOfQtWidgets/3.QMessageBox
01:45:00 -   1: :00

'''
from PySide6.QtWidgets import QApplication
from widget import Widget
import sys

app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()

QApplication.shutdown(app) 