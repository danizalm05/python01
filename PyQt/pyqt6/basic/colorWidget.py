'''
Create GUI Applications with Python & Qt6 / Martin Fitzpatrick
using QVBoxLayout
Listing 26. basic/layout_1.py  page 69
Listing 28. basic/layout_2b.py add a few more colored widgets to the layout
            page 74
#page  82
'''
import sys
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QApplication, QMainWindow,QHBoxLayout, \
                 QVBoxLayout, QWidget

from layout_colorwidget import Color       #A file in local directory

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BoxLayout")
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        # Spacing around the layout using .setContentMargins
        # Spacing between elements using .setSpacing.
        layout1.setContentsMargins(5, 1, 0, 0)
        layout1.setSpacing(20)

        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("green"))
        layout2.addWidget(Color("blue"))

        layout1.addLayout(layout2)

        layout1.addWidget(Color("green"))
        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("purple"))

        layout1.addLayout(layout3)
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
