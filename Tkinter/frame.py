"""
Adding Frames To Your Program - Python Tkinter GUI Tutorial #11

Codemy.com

https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/frame.py
https://www.youtube.com/watch?v=_auZ8TTkojQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=11

 """
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Codemy.com')
root.iconbitmap('neton.ico')

frame = LabelFrame(root, padx=50, pady=50, text="ff is Here!")
frame.pack(padx=120, pady=10)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)
root.mainloop()
