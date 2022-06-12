"""
How To Create Combo Boxes - PyQt5 GUI Thursdays #2
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/combo.py
https://www.youtube.com/watch?v=O58FGYYBV7U&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=2
6:40


 """
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Hello World!!")

        # Set Vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create A Label
        my_label = qtw.QLabel("Pick Something From The List Below", self)

        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        # -------Create a Combo box -------
        #
        my_combo = qtw.QComboBox(self,
                                 editable=True,
                                 insertPolicy=qtw.QComboBox.InsertAtBottom)
        # Add Items To The Combo Box
        my_combo.addItem("Pepperoni", "Something")
        my_combo.addItem("Cheese", 2)
        my_combo.addItem("Mushroom", qtw.QWidget)
        my_combo.addItem("Peppers")
        my_combo.addItems(["One", "Two", "Three"])
        font = qtg.QFont('Arial', 18)

        # adding action to combo box
        my_combo.setFont(font)

        # Put combobox on the screen
        self.layout().addWidget(my_combo)
        # -----------------------------

        # Create a button
        my_button = qtw.QPushButton("Press Me!",
                                    clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            # Add name to label
            tex = my_combo.currentText()
            da = my_combo.currentData()
            idx = my_combo.currentIndex()
            my_label.setText(f'You Picked {tex} + {da} +{ idx}!')


app = qtw.QApplication([])
mw = MainWindow()

# Run The App
app.exec_()
