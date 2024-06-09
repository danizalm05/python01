'''
page 39
'''
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget01 = QLabel("Hello")
        font = widget01.font()#Get current font, modify it and apply it back.
        font.setPointSize(30)
        widget01.setFont(font)

        widget01.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(widget01)


        widget02 = QLabel("War")
        font = widget02.font()#Get current font, modify it and apply it back.
        font.setPointSize(20)
        widget02.setFont(font)
        align_top_left = Qt.AlignLeft | Qt.AlignTop
        widget02.setAlignment(align_top_left)
        self.setCentralWidget(widget02)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()