"""
Build an Image Viewer App With Python and TKinter - Python Tkinter GUI Tutorial #9
https://www.youtube.com/watch?v=zg4c92pNFeo&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=11

Adding A Status Bar - Python Tkinter GUI Tutorial #10
https://www.youtube.com/watch?v=MGu7zKi5azQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=10
7:06
https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course
https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/viewer.py
https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/status.py
"""
from tkinter import *
from PIL import ImageTk, Image
import getpass


imgName = 'p1.jpg'  #"cat-face.png"
def readImagePath(imgName):
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER + imgName
    #print(path)
    return path


class maingui:
    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)



root = Tk()
root.geometry("490x500")
root.title('Image Viewer')

root.iconbitmap('neton.ico')
imgPath = readImagePath("a1.jpg")


imgPath = readImagePath("p1.jpg")
my_img1 = ImageTk.PhotoImage(Image.open(imgPath).resize((470, 390)))

imgPath = readImagePath("p2.jpg")
my_img2 = ImageTk.PhotoImage(Image.open(imgPath).resize((470, 390)))

imgPath = readImagePath("p3.jpg")
my_img3 = ImageTk.PhotoImage(Image.open(imgPath).resize((470, 390)))

imgPath = readImagePath("p4.jpg")
my_img4 = ImageTk.PhotoImage(Image.open(imgPath).resize((470, 390)))

image_list = [my_img1, my_img2, my_img3, my_img4]
txt = "Image 1 of " + str(len(image_list))
status = Label(root, text=txt, bd=3, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

my_label = Label(image=my_img2)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number -1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number - 1))

    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    print(image_number)
    return
def backward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    # Update Status Bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
button_back = Button(root, text="<<",  state=DISABLED,command=backward )
button_exit = Button(root, text="Exit Program", command=root.quit)

button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)

button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()





