"""
contours
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/contours.py
1:12:00  1:20:00
"""

import getpass
import cv2 as cv
import numpy as np
import cvzone
import matplotlib.pyplot as plt

file_name = 'lady.jpg'
def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+file_name

# Read in an image
file_path = readImagePath()
img = cv.imread(file_path)
cv.imshow('org', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv  = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab  = cv.cvtColor(img, cv.COLOR_BGR2LAB)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

imgList = [img, gray,hsv, lab,rgb, gray]
stackedImg = cvzone.stackImages(imgList, 3, 0.4)
cv.imshow("Color spaces", stackedImg)


plt.imshow(img)
plt.show()


cv.waitKey(0)
   
    