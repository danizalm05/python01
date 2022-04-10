"""
color   1:12:30   1:23:00
OpenCV Course - Full Tutorial with Python
 https://www.youtube.com/watch?v=oXlwWbU8l2o
 https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/colour_spaces.py
 """
import cv2 as cv

import matplotlib.pyplot as plt


BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
mimg = "bz.JPG"
path = BASE_FOLDER +  mimg

img   = cv.imread(path)
cv.imshow('Original', img)

# Resizing

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
img = resized


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to   HSV (hue, saturation, value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
# L* for perceptual lightness
# a* and b* for the 4 unique colors red, green, blue, and yellow
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
''' 

'''
# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)