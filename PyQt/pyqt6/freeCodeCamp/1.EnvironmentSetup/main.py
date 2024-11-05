'''
 Learn Python GUI Development for Desktop – PySide6 and Qt Tutorial

 https://github.com/rutura/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals-
 https://www.youtube.com/watch?time_continue=3&v=Z1N9JzNax2k&embeds_referring_euri=https%3A%2F%2Fduckduckgo.com%2F
https://doc.qt.io/qtforpython-6/
52:00
'''

import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder
app = QApplication(sys.argv)

window = ButtonHolder()
window.show() 
app.exec()