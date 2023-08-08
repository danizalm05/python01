"""
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/basic_functions.py
5:03
"""
#pylint:disable=no-member
import getpass

import cv2 as cv

file_name = 'a1.jpg'
def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+file_name

def rescaleFrame(frame, scale = 0.75):
    width  = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    resiz = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    return resiz

# Read in an image
file_path = readImagePath()
img = cv.imread(file_path)
cv.imshow('Origin', img)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
rescale =rescaleFrame(img, 0.5)
cv.imshow('Rescale',rescale)
cv.waitKey(0)