'''
Create GUI Applications with Python & Qt6
Martin Fitzpatrick
page 28

'''
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")#reference  so we can access our

        self.button.clicked.connect(self.the_button_was_clicked)
# Set the central widget of the Window.
        self.setCentralWidget(self.button)
    def the_button_was_clicked(self):
          self.button.setText("You already clicked me.")
          self.button.setEnabled(False)#disable a button
          
# Also change the window title.
          self.setWindowTitle("My Oneshot App")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()