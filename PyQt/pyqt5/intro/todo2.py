# -*- coding: utf-8 -*-
"""
Add A Database To Our ToDo List part 1  #14
Using SQLite3 For Our ToDo List part 2  #15
https://www.youtube.com/watch?v=EFKI9bu4lrY&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=13
https://www.youtube.com/watch?v=4wplGk935r8&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=15

https://github.com/flatplanet/pyqt5_youtube_playlist/blob/main/todo2.py

https://github.com/flatplanet/pyqt5_youtube_playlist

8:11
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QMessageBox
import sqlite3

conn = sqlite3.connect('mylist.db')
c = conn.cursor()
#Create databse with one column:  'list_item'   type: 'text'"
c.execute(""" CREATE TABLE if not exists todo_list( list_item text)  """)
conn.commit()
conn.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 1166)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # add
        self.additem_pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                        clicked=lambda: self.add_it())
        self.additem_pushButton.setGeometry(QtCore.QRect(80, 150, 231, 81))
        self.additem_pushButton.setObjectName("additem_pushButton")

        # Delete
        self.deleteitem_pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                           clicked=lambda: self.delete_it())
        self.deleteitem_pushButton.setGeometry(QtCore.QRect(340, 150, 231, 81))
        self.deleteitem_pushButton.setObjectName("deleteitem_pushButton")

        # clear
        self.clearAll_pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                         clicked=lambda: self.clear_it())
        self.clearAll_pushButton.setGeometry(QtCore.QRect(600, 150, 241, 81))
        self.clearAll_pushButton.setObjectName("clearAll_pushButton")

        self.addItem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addItem_lineEdit.setGeometry(QtCore.QRect(70, 50, 1031, 81))

        self.addItem_lineEdit.setFont(font)
        self.addItem_lineEdit.setText("")
        self.addItem_lineEdit.setObjectName("addItem_lineEdit")
        self.myList_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.myList_listWidget.setGeometry(QtCore.QRect(60, 250, 1041, 791))
        self.myList_listWidget.setFont(font)
        self.myList_listWidget.setObjectName("myList_listWidget")

        #Save DB
        #self.save_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.save_pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                         clicked=lambda: self.save_it())
        self.save_pushButton.setGeometry(QtCore.QRect(860, 150, 241, 81))
        self.save_pushButton.setObjectName("save_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #grab all the items from the database
        self.grab_all()

    def grab_all(self):

        conn = sqlite3.connect('mylist.db')
        c = conn.cursor()
        # Create databse with one column:  'list_item'   type: 'text'"
        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()
        conn.commit()
        conn.close()

        for record in records:
            self.myList_listWidget.addItem(str(record[0]))

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

    #Save to a data base
    def save_it(self):
        conn = sqlite3.connect('mylist.db')
        c = conn.cursor()
        c.execute('DELETE FROM todo_list;',)
        items =[]
        for index in range(self.myList_listWidget.count()):
            items.append(self.myList_listWidget.item(index))

        for item in items:
            #print(item.text())
            c.execute("INSERT INTO todo_list VALUES(:item)",
                {
                    'item': item.text(),
                })
        conn.commit()
        conn.close()

        # Pop up box
        msg = QMessageBox()
        msg.setWindowTitle("Saved To Database!!")
        msg.setText("Your Todo List Has Been Saved!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDoList"))
        self.additem_pushButton.setText(_translate("MainWindow", "Add"))
        self.deleteitem_pushButton.setText(_translate("MainWindow", "Delete"))
        self.clearAll_pushButton.setText(_translate("MainWindow", "Clear all"))
        self.save_pushButton.setText(_translate("MainWindow", "Save to DB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
