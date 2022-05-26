
from tkinter import *
from PIL import Image, ImageTk
import cv2
import getpass

BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/faces/'
imgPath = BASE_FOLDER+'b1.jpg'  #'b1.jpg'   'bb.jpg'
print(imgPath)


# Create an instance of TKinter Window or frame
win = Tk()




# Create a Label to capture the Video frames
label =Label(win)
label.grid(row=0, column=0)

frameWidth = 640
frameHeight = 480
win.geometry("645x490")
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

#path = 'C:/Users/gilfm/Videos/Captures/highway.mp4'
#cap = cv2.VideoCapture(path)
# Define function to show frame
def show_frames():
    # Get the latest frame and convert into Image
    success, img = cap.read()

    #img = cv2.imread(imgPath)
    cv2image= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(cv2image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_DEFAULT)
    canny = cv2.Canny(blur, 200, 200)
    img = Image.fromarray(canny)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label.after(20, show_frames)

show_frames()
win.mainloop()