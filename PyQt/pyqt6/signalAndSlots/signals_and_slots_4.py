'''

page 33
Qt widgets directly to one another.
In the following example, we add a QLineEdit widget and a QLabel to the window.
In the __init__ for the window we connect our line edit .textChanged signal to
the .setText method on the QLabel. Now any time the text changes in the
QLineEdit the QLabel will receive that text to it’s .setText method.
33
'''
from PySide6.QtWidgets import QApplication, \
    QMainWindow, QLabel, QLineEdit, \
    QVBoxLayout, QWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.label = QLabel()
        self.input = QLineEdit()
       #connect  .textChanged signal to  .setText method on QLabel

        self.input.textChanged.connect(self.label.setText)
        layout = QVBoxLayout()  # Adds the two widgets to a layout

        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        # Set the central widget of the Window.
        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
