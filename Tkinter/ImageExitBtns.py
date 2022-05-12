"""
Using Icons, Images, and Exit Buttons - Python Tkinter GUI Tutorial #8

https://www.youtube.com/watch?v=NoTM8JciWaQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=9
https://www.youtube.com/watch?v=zg4c92pNFeo&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=10

PIL: Python Image Library
https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course
https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/images.py
"""
from tkinter import *
from PIL import ImageTk, Image
import getpass





imgName = 'p1.jpg'  #"cat-face.png"
def readImagePath(imgName):
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER + imgName
    print(path)

    return path


root = Tk()
root.title('Learn To Code at Codemy.com')

root.iconbitmap('neton.ico')
imgPath = readImagePath(imgName)
my_img = ImageTk.PhotoImage(Image.open(imgPath))
root.my_label = Label(image=my_img)
root.my_label.pack()
Button_Quit = Button(root,text="exit",command= root.quit)
Button_Quit.pack()
root.mainloop()





