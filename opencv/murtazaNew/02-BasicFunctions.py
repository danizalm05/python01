'''
Basic Functions
https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=549s  17:00
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter2.py
'''


import numpy as np
import cv2
import getpass
import os


frameWidth = 640
frameHeight = 480
BASE_FOLDER = 'C:/Users/'+ getpass.getuser()


BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
path = BASE_FOLDER+'2.jpg'  #'b1.jpg' 'lena.png' 'bb.jpg'
print(path)

 
if os.path.isfile(path):
    img = cv2.imread(path)
    kernel = np.ones((5,5),np.uint8)
    imageGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    imgBlur = cv2.GaussianBlur(imageGray,(7,7),0)
    imgCanny = cv2.Canny(img,150,200)  # Edge detector
    imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
    imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

    cv2.imshow("Gray Image",imageGray)
    cv2.imshow("Blur Image",imgBlur)
    cv2.imshow("Canny Image",imgCanny)
    cv2.imshow("Dialation Image",imgDialation)
    cv2.imshow("Eroded Image",imgEroded)
    cv2.waitKey(0)
else:
    print("ERROR --> Missing File: " + path   )    




