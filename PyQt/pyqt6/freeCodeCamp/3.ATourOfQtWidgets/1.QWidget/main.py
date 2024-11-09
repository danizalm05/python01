'''
 Learn Python GUI Development for Desktop – PySide6 and Qt Tutorial
 window with two buttons

rockwidget.py
https://github.com/rutura/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals-/blob/main/3.ATourOfQtWidgets/1.QWidget/main.py
https://www.youtube.com/watch?time_continue=3&v=Z1N9JzNax2k&embeds_referring_euri=https%3A%2F%2Fduckduckgo.com%2F
01:08:00

'''
from PySide6.QtWidgets import QApplication,QWidget
from rockwidget import RocWidget

import sys
app = QApplication(sys.argv)

window = RocWidget()
window.show()

app.exec()