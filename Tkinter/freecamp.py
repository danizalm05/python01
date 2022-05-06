"""
https://www.youtube.com/watch?v=YXPyB4XeYLA&t=3s 34:19
https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course
https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/hello.py
https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/grid.py
"""

from tkinter import *


def myClick():
    hhh = 'hello   ' + e.get()
    myLabel3 = Label(root, text=hhh)  # Put text from e as a label on button
    myLabel3.grid(row=5, column=0)


root = Tk()
e = Entry(root, width=50, fg="blue", bg="white", cursor="arrow",
          borderwidth=5, font='arial 18',
          highlightcolor="black",
          justify="right",

          xscrollcommand="scrollbar"
          )
e.grid(row=0, column=0)#Put the entry input window in 0,0
e.insert(0, "Default value") #Write a default string
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name Is John Elder")
# Shoving it onto the screen

myLabel1.grid(row=1, column=0)
myLabel2.grid(row=1, column=5)

myButton = Button(root, text="Click me", padx=50, pady=50, fg='red',
                  bg='yellow', command=myClick)
myButton.grid(row=4, column=8)

# Shoving it onto the screen
#


root.mainloop()
