'''
Create GUI Applications with Python & Qt6 / Martin Fitzpatrick
using QStackedLayout.
This layout allows you to position elements directly in front of one another.
 You can then select which widget you want to show.
 You will see only the last widget you added.
 QStackedWidget is how tabbed views in applications work. Only one view
 ('tab') is visible at any one time. You can control which widget to show
 at any time by  using '.setCurrentIndex()' or '.setCurrentWidget()' to set
 the item by either the index (in order the widgets were added) or by the
 widget itself.


 Qt provides a built-in tab widget that provides this kind of layout out of
the box - although it’s actually a widget, not a layout. Below the tab demo is
recreated using QTabWidget —


Listing 33. basic/layout_7.py
#page  90    /88
'''
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)
from layout_colorwidget import Color
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()
        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)
        btn = QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("red"))
        btn = QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("green"))
        btn = QPushButton("yellow")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("yellow"))
        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
         self.stacklayout.setCurrentIndex(0)
    def activate_tab_2(self):
         self.stacklayout.setCurrentIndex(1)
    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
QApplication.shutdown(app) 