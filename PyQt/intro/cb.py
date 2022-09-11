# -*- coding: utf-8 -*-
"""
Using The Command Link Button  #16
https://www.youtube.com/watch?v=49PJrKsSZ6c&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=16
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/cb.py
1:00
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.count = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 132)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.next_commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.next_commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget, clicked=lambda: self.increment())
        self.next_commandLinkButton.setGeometry(QtCore.QRect(20, 10, 222, 48))
        self.next_commandLinkButton.setObjectName("next_commandLinkButton")
        self.next_label = QtWidgets.QLabel(self.centralwidget)
        self.next_label.setGeometry(QtCore.QRect(430, 15, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.next_label.setFont(font)
        self.next_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.next_label.setObjectName("next_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_commandLinkButton.setText(_translate("MainWindow", "Inc Counter"))
        self.next_label.setText(_translate("MainWindow", "0"))

    def increment(self):
        # Increment the Counter
        self.count += 1

        # Output to the label
        self.next_label.setText(str(self.count))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
