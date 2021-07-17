"""
Basic  function  57:00 1:12:00
OpenCV Course - Full Tutorial with Python
 https://www.youtube.com/watch?v=oXlwWbU8l2o
 https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/contours.py
 """
import cv2 as cv
import numpy as np


BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
mimg = "bz.JPG"
path = BASE_FOLDER +  mimg

img   = cv.imread(path)
cv.imshow('Original', img)

# Resizing

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
img = resized

blank = np.zeros(img.shape, dtype='uint8')
blank1 = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 135, 185)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)



cv.waitKey(0)