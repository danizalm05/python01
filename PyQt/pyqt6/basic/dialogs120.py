'''
Create GUI Applications with Python & Qt6
The hands-on guide to making apps with Python
Martin Fitzpatrick
120-126
'''

import sys

from PySide6.QtWidgets import (
   QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HELLO!")

        buttons = (
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )
        '''construct a line of multiple buttons by OR-ing 
           them together using a pipe (|) '''
        self.buttonBox = QDialogButtonBox(buttons)
        '''QDialogButtonBox instance to hold the buttons.
           flag for the buttons to display is passed in 
           as the first parameter.'''
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self,is_checked):
        print("click", is_checked)

        dlg = CustomDialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

    # end::button_clicked[]

 
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
QApplication.shutdown(app) 