"""
blurring.py    1:31 1:44
OpenCV Course - Full Tutorial with Python
www.youtube.com/watch?v=oXlwWbU8l2o
github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/blurring.py
   """
import cv2 as cv
import numpy as np

BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
mimg = "bz.JPG"
path = BASE_FOLDER + mimg

img0 = cv.imread(path)
#cv.imshow('Original', img0)

# Resizing

(m, n) = (int(img0.shape[0] / 4), int(img0.shape[1] / 4))

resized = cv.resize(img0, (m, n), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
img = resized

# Averaging
average = cv.blur(img, (11,11))
cv.imshow('Average Blur', average)


# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7 ), 0)
cv.imshow('Gaussian Blur', gauss)
# Median Blur

median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 50, 75, 75)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)