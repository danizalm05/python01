"""
masking.py  1:53 2:00
OpenCV Course - Full Tutorial with Python
www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/masking.py
   """
import cv2 as cv
import numpy as np

BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
mimg = "bz.JPG"
path = BASE_FOLDER + mimg

img0 = cv.imread(path)
#cv.imshow('Original', img0)

# Resizing

(m, n) = (int(img0.shape[0] // 4), int(img0.shape[1] // 4))

resized = cv.resize(img0, (m, n), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
img = resized

blank = np.zeros((img.shape[:2]), dtype='uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2  ,img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (60,60), (270,270), 255, -1)
weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('weird_shape', weird_shape)

masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)
cv.waitKey(0)