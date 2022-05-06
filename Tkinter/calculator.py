"""
Calculator  Tkinter
https://www.youtube.com/watch?v=YXPyB4XeYLA&t=3s  52:00
https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course
https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/calculator.py
"""
from tkinter import *


class CalcApp:


    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        e = Entry(self.window, width=35, borderwidth=5)
        e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)




        self.button_1 = Button(self.window, text="1", padx=40, pady=20, command=lambda: self.button_click("1"))
        self.button_2 = Button(self.window, text="2", padx=40, pady=20, command=lambda: self.button_click("2"))
        self.button_3 = Button(self.window, text="3", padx=40, pady=20, command=lambda: self.button_click("3"))
        self.button_4 = Button(self.window, text="4", padx=40, pady=20, command=lambda: self.button_click("4"))
        self.button_5 = Button(self.window, text="5", padx=40, pady=20, command=lambda: self.button_click("5"))
        self.button_6 = Button(self.window, text="6", padx=40, pady=20, command=lambda: self.button_click("6"))
        self.button_7 = Button(self.window, text="7", padx=40, pady=20, command=lambda: self.button_click("7"))
        self.button_8 = Button(self.window, text="8", padx=40, pady=20, command=lambda: self.button_click("8"))
        self.button_9 = Button(self.window, text="9", padx=40, pady=20, command=lambda: self.button_click("9"))
        self.button_0 = Button(self.window, text="0", padx=40, pady=20, command=lambda: self.button_click("0"))
        self.button_add = Button(root, text="+", padx=39, pady=20, command=self.button_add)
        self.button_equal = Button(root, text="=", padx=91, pady=20, command=self.button_equal)
        self.button_clear = Button(root, text="Clear", padx=79, pady=20, command=self.button_clear)

        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)

        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)

        self.button_0.grid(row=4, column=0)
        self.button_clear.grid(row=4, column=1, columnspan=2)
        self.button_add.grid(row=5, column=0)
        self.button_equal.grid(row=5, column=1, columnspan=2)
        self.window.mainloop()

    def  button_click(self,number):
        print(number)
        return
    def button_add(self):
             print('add')
    def  button_equal(self):
        print('button_equal')
    def  button_clear(self):
        print('button_clear')



root = Tk()
CalcApp(root, "Simple Calculator")


