'''
ToolBar96.py
Create GUI Applications with Python & Qt6 / Martin Fitzpatrick

Listing 37. basic/toolbars_and_menus_1.py
#page  96 -105
https://www.pythonguis.com/pyqt6/
'''

import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon

from PySide6.QtWidgets import (
    QApplication, QLabel,QToolBar, QStatusBar,
    QMainWindow, QPushButton, QTabWidget, QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

  

        button_action = QAction(QIcon("icon.png"), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)#turn QAction toggleable
        toolbar.addAction(button_action)
        self.setStatusBar(QStatusBar(self))
    
    # function accept the signal from the QAction
    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()