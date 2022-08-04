"""
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/transformations.py 31:38 44:17

48:00
"""

import getpass
import cv2 as cv
import numpy as np



file_name = 'a4.jpg'
def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+file_name

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    scale = 1.0
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)




# Read in an image
file_path = readImagePath()
img = cv.imread(file_path)
cv.imshow('org', img)

translated = translate(img, 100, 100) #shift image right 100 pix and down 100 px
cv.imshow('Translated', translated)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[20 :40 , 30 :40 ]
cv.imshow('Cropped', cropped)

cv.waitKey(0)