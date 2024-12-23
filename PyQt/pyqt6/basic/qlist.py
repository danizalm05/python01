'''
QListWidget
Create GUI Applications with Python & Qt6 / Martin Fitzpatrick
Listing 20. basic/widgets_5.py  page 51-54
'''

import sys
from PySide6.QtWidgets import QApplication, QListWidget, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget = QListWidget()
        widget.addItems(["eeffdfe", "ddf", "Thrggdfgee"])
        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        self.setCentralWidget(widget)
    def index_changed(self, i): # Not an index, i is a QListItem
      print("index_changed = ",i.text())
    def text_changed(self, s): # s is a str
      print("text_changed = ",s)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
