'''
QListWidget
Create GUI Applications with Python & Qt6 / Martin Fitzpatrick
Listing 21. basic/widgets_6.py page 54-57
'''
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")#place holder text
        #widget.setInputMask('000.000.000.000;_')#validation using an input mask
        # widget.setReadOnly(True) # uncomment this to make readonly
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        self.setCentralWidget(widget)
    def return_pressed(self):
          print("Return pressed!")
          self.centralWidget().setText("BOOM!")
    def selection_changed(self):
          print("Selection changed")
          print(self.centralWidget().selectedText())
#55

    def text_changed(self, s):
          print("Text changed...")
          print(s)
    def text_edited(self, s):
          print("Text edited...")
          print(s)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
