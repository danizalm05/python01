"""
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/transformations.py 31:38 44:17
"""

import getpass
import cv2 as cv

file_name = 'a1.jpg'
def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+file_name

# Read in an image
file_path = readImagePath()
img = cv.imread(file_path)
cv.imshow('Park', img)


cv.waitKey(0)