# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:25:14 2022
https://www.youtube.com/watch?v=n6JEgSqXOrU&list=PL6yy_CdpgQmXZU0g0d45NN2iCe1337rXq&index=4
 5:30
@author: 
"""
from tkinter import *
from tkinter import messagebox
import sys


root =Tk()
root.title("Welcome")
root.geometry("300x300")

menu = Menu(root)
root.config(menu = menu)   

def exitt():
    messagebox.showinfo("fgfgf","Exit?" )
    sys.exit("dddddd") 



subm = Menu(menu)
menu.add_cascade(label="File", menu = subm )  
subm.add_command(label="Save")
subm.add_command(label="Exit",command = exitt)

subl = Menu(menu)
menu.add_cascade(label="Tools", menu = subl )  
subl.add_command(label="Draw") 

root.mainloop() 
