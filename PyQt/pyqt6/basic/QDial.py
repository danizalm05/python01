'''
QDial= rotatable widget that functions just like the slider, but  appears as
 an analogue dial
Create GUI Applications with Python & Qt6 / Martin Fitzpatrick

Listing 24. basic/widgets_9.py page 64
'''
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDial, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App - QDial")
        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        self.setCentralWidget(widget)
    def value_changed(self, i):
     print(i)
    def slider_position(self, p):
      print("position", p)
    def slider_pressed(self):
      print("Pressed!")

    def slider_released(self):
      print("Released")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
