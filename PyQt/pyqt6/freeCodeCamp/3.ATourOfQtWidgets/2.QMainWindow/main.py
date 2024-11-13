'''
 Learn Python GUI Development for Desktop – PySide6 and Qt Tutorial


https://www.youtube.com/watch?v=Z1N9JzNax2k&t=3s
https://github.com/rutura/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals-/tree/main/3.ATourOfQtWidgets/2.QMainWindow
01:26:30 -   1:42:00

'''
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()

QApplication.shutdown(app) 