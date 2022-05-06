# -*- coding: utf-8 -*-
"""
tkinter intro
Created on Fri Apr 29 16:35:21 2022
https://www.youtube.com/watch?v=ii89QtAbrjw&list=PL6yy_CdpgQmXZU0g0d45NN2iCe1337rXq
https://www.youtube.com/watch?v=bLVBBJqelVo&list=PL6yy_CdpgQmXZU0g0d45NN2iCe1337rXq&index=2
https://www.youtube.com/watch?v=SOCA9ywkJSw&list=PL6yy_CdpgQmXZU0g0d45NN2iCe1337rXq&index=3
https://libraries.io/pypi/cvzone
@author: rockman
"""

from tkinter import *
import tkinter.messagebox 
import sys


def exitt():
    tkinter.messagebox.showinfo("fgfgf","Exit?" )
    sys.exit("dddddd") 

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")
root.geometry('500x500')
frame1 = Frame(root, width = 500, height = 500, bg = "powder blue")
 
##root.configure(background = "powder blue")
lab1  = Label(root,text='name',font=('Times 20 bold'),width=4)
lab1.place(x=10 ,y=10)

but1 = Button(root,padx=4, pady=4,width = 6,height =3, text ="Hello", fg="red",command = exitt)
but1.place(x= 20,y=100)

text1=Text(root,width=35,height=12)
text1.place(x=150,y=100)
 

root.mainloop()
 








