# -*- coding: utf-8 -*-
"""
Todo list gui   #13
https://www.youtube.com/watch?v=EFKI9bu4lrY&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=13

https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/todo.py
https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/todo2.py

https://github.com/flatplanet/pyqt5_youtube_playlist
9:41
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # add
        self.additem_pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                        clicked=lambda: self.add_it())
        self.additem_pushButton.setGeometry(QtCore.QRect(80, 150, 231, 81))
        self.additem_pushButton.setObjectName("additem_pushButton")

        #Delete

        self.deleteitem_pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                        clicked=lambda: self.delete_it())
        self.deleteitem_pushButton.setGeometry(QtCore.QRect(340, 150, 231, 81))
        self.deleteitem_pushButton.setObjectName("deleteitem_pushButton")

        #clear

        self.clearAll_pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                           clicked=lambda: self.clear_it())
        self.clearAll_pushButton.setGeometry(QtCore.QRect(600, 150, 241, 81))
        self.clearAll_pushButton.setObjectName("clearAll_pushButton")


        self.addItem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addItem_lineEdit.setGeometry(QtCore.QRect(80, 50, 761, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.addItem_lineEdit.setFont(font)
        self.addItem_lineEdit.setText("")
        self.addItem_lineEdit.setObjectName("addItem_lineEdit")

        self.myList_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.myList_listWidget.setGeometry(QtCore.QRect(60, 250, 801, 791))
        self.myList_listWidget.setFont(font)
        self.myList_listWidget.setObjectName("myList_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def add_it(self):
        item = self.addItem_lineEdit.text()
        self.myList_listWidget.addItem(item)
        self.addItem_lineEdit.setText("")

    def delete_it(self):
        print("del it")
        # Grab the selected row or current row
        clicked = self.myList_listWidget.currentRow()#return the index of the selected item
        print(clicked)
        self.myList_listWidget.takeItem(clicked)

    def clear_it(self):
         self.myList_listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDoList"))
        self.additem_pushButton.setText(_translate("MainWindow", "Add"))
        self.deleteitem_pushButton.setText(_translate("MainWindow", "Delete"))
        self.clearAll_pushButton.setText(_translate("MainWindow", "Clear all"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
