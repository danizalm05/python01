'''
Create GUI Applications with Python & Qt6
The hands-on guide to making apps with Python
Martin Fitzpatrick
132-138
'''
import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        #but2 = QPushButton("Pr !")
        #self.setCentralWidget(but2)
    # tag::button_clicked[]
    def button_clicked(self, s):

        '''
        button = QMessageBox.question(
            self, "Question dialog", "The longer message"
        )
        '''
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll |
                    QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )
        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")

        ''' 
        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")
       '''
    # end::button_clicked[]


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
QApplication.shutdown(app)
'''
Button types:
QDialogButtonBox.Ok
QDialogButtonBox.Open
QDialogButtonBox.Save
QDialogButtonBox.Cancel
QDialogButtonBox.Close
QDialogButtonBox.Discard
QDialogButtonBox.Apply
QDialogButtonBox.Reset
QDialogButtonBox.RestoreDefaults
QDialogButtonBox.Help
QDialogButtonBox.SaveAll
QDialogButtonBox.Yes
QDialogButtonBox.YesToAll
QDialogButtonBox.No
QDialogButtonBox.NoToAll
QDialogButtonBox.Abort
QDialogButtonBox.Retry
QDialogButtonBox.Ignore
QDialogButtonBox.NoButton

QMessageBox.about(parent, title, message)
QMessageBox.critical(parent, title, message)
QMessageBox.information(parent, title, message)
QMessageBox.question(parent, title, message)
QMessageBox.warning(parent, title, message)
The
'''