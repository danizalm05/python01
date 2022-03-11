"""
Basic  function   43:16  57:00
OpenCV Course - Full Tutorial with Python
 https://www.youtube.com/watch?v=oXlwWbU8l2o
 https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/transformations.py

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




# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down


translated = translate(img, -100, 100)#Left  and Down  100
cv.imshow('Translated', translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)