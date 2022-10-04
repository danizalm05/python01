# -*- coding: utf-8 -*-

''' Dail and Combo  box
 dail
  https://www.youtube.com/watch?v=sHZf729Hwgk&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=22
  https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/dial.py
 combo
 https://www.youtube.com/watch?v=31QT25J_cec&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=23
 https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/combo.py
#5:32
'''


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        font = QtGui.QFont()
        font.setPointSize(18)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1785, 1368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")

        self.dial = QtWidgets.QDial(self.widget_2)
        # Set Dial Defaults
        #self.dial.setMinimum(10)
        #self.dial.setMaximum(360)
        self.dial.setRange(100,200)
        # Set Default Startup Position
        self.dial.setValue(120)

        # Set notches
        self.dial.setNotchesVisible(True)
        # Set color
        self.dial.setStyleSheet('background-color: #377235')



        # Use Dial
        self.dial.valueChanged.connect(lambda: self.dialer())


        self.dial.setObjectName("dial")
        self.verticalLayout.addWidget(self.dial)
        self.label = QtWidgets.QLabel(self.widget_2)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")


        ##    comboBox

        self.comboBox = QtWidgets.QComboBox(self.widget_3)
        self.comboBox.setFont(font)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        #############
        # Add Items To The Combo Box
        self.comboBox.addItem("Pepperoni", "Something")
        self.comboBox.addItem("Cheese", 2)
        #self.comboBox.addItem("Mushroom", qtw.QWidget)
        self.comboBox.addItem("Peppers")
        self.comboBox.addItems(["One", "Two", "Three"])
        self.comboBox.insertItems(2, ["One", "two", "Third Thing"])

        my_toppines = ["fff","ggg","ghhgh","dg"]
        self.comboBox.addItems(my_toppines)

        self.pushButton = QtWidgets.QPushButton(self.widget_3, clicked = lambda: self.press_it())


        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setGeometry(QtCore.QRect(170, 112, 481, 81))

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.widget_3.raise_()
        self.verticalLayout_2.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1785, 56))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Make combox clickable
        self.comboBox.activated.connect(self.press_it)
 ##############################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Current Position:0"))
        self.pushButton.setText(_translate("MainWindow", "Select"))
        self.label_2.setText(_translate("MainWindow", "Selected item"))

    def dialer(self):
        # Grab the Current dial position
        value = self.dial.value()
        # Set label text
        self.label.setText(f'Current Position: {str(value)}')
    def press_it(self):
        # "combox"
        print("combox")
        #my_label.setText(f'You Picked {my_combo.currentText()}!')
        self.label_2.setText(f'You Picked {self.comboBox.currentText()}!')
        #self.label_2.setText('You Picked ')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
