'''
Resizing image
https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=549s  27:00
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter3.py
'''


import numpy as np
import cv2
import getpass

frameWidth = 640
frameHeight = 480
BASE_FOLDER = 'C:/Users/'+ getpass.getuser()


BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
path = BASE_FOLDER+'road.jpg'  #'b1.jpg' 'lena.png' 'bb.jpg'
print(path)

img = cv2.imread(path)
print(img.shape)


imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)
imgCropped = img[46:219,252:495]

cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image",img)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)




