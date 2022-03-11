"""
thresh.py  2:15:00 2:26:00
OpenCV Course - Full Tutorial with Python
www.youtube.com/watch?v=oXlwWbU8l2o
  threshold = minimum intensity   that will produce a  specified effect
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/thresh.py

"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt




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


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)
cv.waitKey(0)