"""
edge detetion
  2:26:00
OpenCV Course - Full Tutorial with Python
www.youtube.com/watch?v=oXlwWbU8l2o
  threshold = minimum intensity   that will produce a  specified effect
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/gradients.py

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

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)