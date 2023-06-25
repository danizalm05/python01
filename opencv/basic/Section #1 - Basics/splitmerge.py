"""
split and merage
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/splitmerge.py

1:23:00  1:30:10
"""

import getpass
import cv2 as cv
import numpy as np
import cvzone
import matplotlib.pyplot as plt

file_name = '1.jpg'
def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+file_name

# Read in an image
file_path = readImagePath()
img = cv.imread(file_path)
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
b, g, r = cv.split(img)
cv.imshow('org', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

imgList = [b, g, r ,blue,green,red]
stackedImg = cvzone.stackImages(imgList, 3, 0.6)





cv.imshow("cv.split", stackedImg)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


merged = cv.merge([b,r,r])
cv.imshow('Merged Image', merged)
cv.waitKey(0)
   
    