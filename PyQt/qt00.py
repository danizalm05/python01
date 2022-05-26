
'''
Basic GUI design: PyQt5 tutorial - Part 01
https://www.youtube.com/watch?v=ORaBSFhh13A&list=PLjPKPFvkBtZqKg8ugYihcxkWfnIDcwR4K
https://www.youtube.com/watch?v=Vz0s-w4hksY&list=PLjPKPFvkBtZqKg8ugYihcxkWfnIDcwR4K&index=2
https://www.youtube.com/watch?v=co4ymeb3FRc&list=PLjPKPFvkBtZqKg8ugYihcxkWfnIDcwR4K&index=3
Make a simply main window with menu, items and sub-items. A user can also
add status bar text at bottom, as well as the image icon to the menu item.
Python installation: https://youtu.be/71oXpvx8CsU
PyQt5 installation, from terminal execute the commands below:

pip3 install pyqt5
pip3 install pyqt5-tools

After that simply run the command below to run qt designer in Terminal:

qt5-tools designer
c:\users\gilfm\appdata\local\programs\python\python310\lib\site-packages
C:\Users\gilfm\AppData\Local\Programs\Python\Python310\Scripts\pyuic5.exe
Translate ui  file to  python file
in CMD  run
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    textLabel = QLabel(widget)
    textLabel.setText("Hello World!")
    textLabel.move(110,85)

    widget.setGeometry(50,50,320,200)
    widget.setWindowTitle("PyQt5 Example")
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()