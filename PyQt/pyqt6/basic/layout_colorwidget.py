'''
Create GUI Applications with Python & Qt6 / Martin Fitzpatrick

Widget that displays a solid color. This will help to distinguish
widgets that we add to the layout.
Call: widget = Color("red")
Listing 25. basic/layout_colorwidget.py page 68
'''

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget
class Color(QWidget):
    def __init__(self, color):
      super().__init__()
      self.setAutoFillBackground(True)
      palette = self.palette()
      palette.setColor(QPalette.Window, QColor(color))
      self.setPalette(palette)



