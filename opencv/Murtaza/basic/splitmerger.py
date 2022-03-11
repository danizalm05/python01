"""
splitmerge   1:23:20  1:30
OpenCV Course - Full Tutorial with Python
 https://www.youtube.com/watch?v=oXlwWbU8l2o
 https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/splitmerge.py """
import cv2 as cv
import numpy as np

BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
mimg = "bz.JPG"
path = BASE_FOLDER + mimg

img0 = cv.imread(path)
cv.imshow('Original', img0)

# Resizing

(m, n) = (int(img0.shape[0] / 4), int(img0.shape[1] / 4))

resized = cv.resize(img0, (m, n), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
img = resized

blank = np.zeros(img.shape[:2], dtype='uint8')
b, g, r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blueb', blue)
cv.imshow('Greenb', green)
cv.imshow('Redb', red)
cv.waitKey(0)
