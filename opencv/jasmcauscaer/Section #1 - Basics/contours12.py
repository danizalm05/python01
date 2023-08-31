"""
contours
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/contours.py
1:00:00
"""

import getpass
import cv2 as cv
import numpy as np
import cvzone


file_name = '2.jpg'
def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+file_name

# Read in an image
file_path = readImagePath()
img = cv.imread(file_path)
cv.imshow('org', img)


blank = np.zeros(img.shape, dtype='uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(img, 125, 175)# find edges  (edge is not the same as contor)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cannyBlur = cv.Canny(blur, 125, 175)

# Output all the images
imgList = [img, gray,canny, blur,cannyBlur, gray]
stackedImg = cvzone.stackImages(imgList, 3, 0.4)

cv.imshow("stackedImg", stackedImg)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


contours, hierarchies = cv.findContours(cannyBlur, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)
   
    