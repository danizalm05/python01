'''
Create GUI Applications with Python & Qt6 / Martin Fitzpatrick
Listing 16. basic/widgets_2a.py  page 42

'''
import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setWindowTitle("My App")
     widget = QLabel("Hello")
     widget.setPixmap(QPixmap("test2.jpg"))
     widget.setScaledContents(True)# stretch or scale to fit window completely

     self.setCentralWidget(widget)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
