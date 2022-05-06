# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:50:59 2022
https://solarianprogrammer.com/2018/04/20/python-opencv-show-image-tkinter-window/ 
"""

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import getpass

imgName = 'p1.jpg'  #"cat-face.png"

def readImagePath(imgName):
   BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
   BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
   path = BASE_FOLDER+imgName
   print(path)

   return path




class App:
    def __init__(self, window, window_title, image_path="cat-face.png"):
        self.window = window
        self.window.title(window_title)

        # Load an image using OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape

        # Create a canvas that can fit the above image

        self.canvas = tkinter.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

    # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))

    # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    # Button that lets the user blur the image
        self.btn_blur = tkinter.Button(window, text="Blur", width=50, command=self.blur_image)
        self.btn_blur.pack(anchor=tkinter.CENTER, expand=True)




        self.window.mainloop()


# Callback for the "Blur" button
    def blur_image(self):
     self.cv_img = cv2.blur(self.cv_img, (3, 3))
     self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
     self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)


# Create a window and pass it to the Application object

imgPath = readImagePath(imgName)
App(tkinter.Tk(), "Tkinter and OpenCV",imgPath)