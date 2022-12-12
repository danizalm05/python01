"""
38 Language Translation App!

------------------------------------
https://www.youtube.com/watch?v=9FfxQvQMlg8&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=38
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/translate.py

install
1. pip install googletrans
2. pip install  textblob
"""
from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QPushButton, QComboBox, QTextEdit, QMessageBox

# noinspection PyUnresolvedReferences
from PyQt5 import uic  # Add the above line so uic is imported

import sys
import googletrans
import textblob


# ----------------------------------
class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("translate.ui", self)
        self.setWindowTitle("Translator App!")

        # -----------------------------------------------
        # Define our widgets

        self.t_button = self.findChild(QPushButton, "pushButton")
        self.c_button = self.findChild(QPushButton, "pushButton_2")

        self.combo_1 = self.findChild(QComboBox, "comboBox")
        self.combo_2 = self.findChild(QComboBox, "comboBox_2")

        self.text_1 = self.findChild(QTextEdit, "textEdit")
        self.text_2 = self.findChild(QTextEdit, "textEdit_2")

        #Connect to Function
        # -----------------------------------------------
        # Click the buttons
        self.t_button.clicked.connect(self.translate)
        self.c_button.clicked.connect(self.clear)
        # Add languages to the combo boxes
        self.languages = googletrans.LANGUAGES
        # Convert to list
        self.language_list = list(self.languages.values())
        # Add items to combo boxes
        self.combo_1.addItems(self.language_list)
        self.combo_2.addItems(self.language_list)

        # Set default combo item
        self.combo_1.setCurrentText("english")
        self.combo_2.setCurrentText("hebrew")

        self.show()
#Functions
        # -----------------------------------------------

    def translate(self):
        try:

            #self.languages.items() = dict_items([('af', 'afrikaans'),.......
            # Get Original Language Key
            for key,value in self.languages.items():
                #print(key, value) # af afrikaans.....
                #self.combo_1.currentText()) the chosen languages
                if (value == self.combo_1.currentText()):
                    from_language_key = key

                    # Get translated Language Key
            for key,value in self.languages.items():
                    if (value == self.combo_2.currentText()):
                        to_language_key = key
            #self.text_1.setText(from_language_key)#show the key of lanuage
            #self.text_2.setText(to_language_key)
            #Turn original text into aTextBlob: Simplified Text Processing
            words = textblob.TextBlob(self.text_1.toPlainText())
            # Translate words!
            words = words.translate(from_lang=from_language_key, to=to_language_key)

            # Output to text_2
            self.text_2.setText(str(words))

        except Exception as e:
            QMessageBox.about(self, "Translator", str(e))

    def clear(self):
        #Clear the text boxes
        self.textEdit.setText("")
        self.textEdit_2.setText("")

        # Reset the combo boxes
        self.combo_1.setCurrentText("english")
        self.combo_2.setCurrentText("hebrew")

        #----------------------



# ----------------------


# Initialize The App


app = QApplication(sys.argv)

UIWindow = UI()
app.exec_()
