# -*- coding: utf-8 -*-

"""
Using The Statusbar  #17
https://www.youtube.com/watch?v=m_DYnnr8N00&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=17
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/status.py
3:24
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 353)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.button1_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.push_1())

        self.button1_pushButton.setGeometry(QtCore.QRect(32, 50, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button1_pushButton.setFont(font)
        self.button1_pushButton.setObjectName("button1_pushButton")

        self.button2_pushButton_2  = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.push_2())

        self.button2_pushButton_2.setGeometry(QtCore.QRect(370, 50, 271, 81))

        font = QtGui.QFont()
        font.setPointSize(16)
        self.button2_pushButton_2.setFont(font)
        self.button2_pushButton_2.setObjectName("button2_pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.setFont(QFont('Times', 16))
        self.statusbar.showMessage("Start ....")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Status Bar"))
        self.button1_pushButton.setText(_translate("MainWindow", "Bu1"))
        self.button2_pushButton_2.setText(_translate("MainWindow", "Button2"))

    def push_1(self):
        self.statusbar.showMessage("push 1")
    def push_2(self):
        self.statusbar.showMessage("push 2")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
