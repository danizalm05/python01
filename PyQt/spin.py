"""
How To Create Spin Boxes - PyQt5 GUI Thursdays #3
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/spin.py
https://www.youtube.com/watch?v=O58FGYYBV7U&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=3https://www.youtube.com/watch?v=2NyculhiSh4&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=3

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

        # -------Create a Spinbox -------
        #
        #my_spin = qtw.QSpinBox(self, value=10,
        my_spin = qtw.QDoubleSpinBox(self, value=10,
                              minimum=0,maximum=100,
                              singleStep=5.5,
                              prefix="#",  suffix="!!!",)

        font = qtg.QFont('Arial', 18)

        # adding action to combo box
        my_spin.setFont(font)

        # Put combobox on the screen
        self.layout().addWidget(my_spin)
        # -----------------------------

        # Create a button
        my_button = qtw.QPushButton("Press Me!",
                                    clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            # Add name to label
            value = my_spin.value()
            my_label.setText(f'You Picked {value}!')


app = qtw.QApplication([])
mw = MainWindow()

# Run The App
app.exec_()
