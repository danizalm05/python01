'''
QComboBox
Create GUI Applications with Python & Qt6 / Martin Fitzpatrick
Listing 19. basic/widgets_4.py  page 48-51
'''


import sys

from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])
        #widget.setEditable(True)  #  allow  editing of values
        '''
          .currentIndexChanged signal is triggered when the currently selected 
          item is updated, by default passing the index of the selected item in 
          the list. 
          There is also a .currentTextChanged signal which instead provides the
           label of the currently selected item, which is often more useful.
        
        '''
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        self.setCentralWidget(widget)
    def index_changed(self, i): # i is an int
        print("index_changed = ",i)
    def text_changed(self, s): # s is a str
        print("text_changed = ",s)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
app.shutdown()