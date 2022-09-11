"""
bitwise.py    masking.py
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/bitwise.py
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/masking.py
01:53:10

"""



import getpass
import cv2 as cv
import numpy as np
import cvzone
import matplotlib.pyplot as plt

file_name = '1.jpg'
def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+file_name

# Read in an image
file_path = readImagePath()
img0 = cv.imread(file_path)
#cv.imshow('org', img0)

def nothing(x):
    pass


cv.namedWindow('image')
cv.createTrackbar('radios', 'image', 50, 550, nothing)
cv.createTrackbar('length', 'image', 50, 590, nothing)
cv.createTrackbar('upr', 'image', 3, 90, nothing)


while (True):

    w, h,_  = img0.shape

    r = cv.getTrackbarPos('radios', 'image')
    l = cv.getTrackbarPos('length', 'image')
    ur = cv.getTrackbarPos('upr', 'image')

    #blank = np.zeros((w, h), dtype='uint8')
    blank = np.zeros(img0.shape[:2], dtype='uint8')
    rectangle = cv.rectangle(blank.copy(), (ur, ur), (ur+l,ur+ l), 255, -1)
    circle = cv.circle(blank.copy(), (200, 200), r, 255, -1)

    # bitwise AND --> intersecting regions
    bitwise_and = cv.bitwise_and(rectangle, circle)

    # bitwise OR --> non-intersecting and intersecting regions
    bitwise_or = cv.bitwise_or(rectangle, circle)

    # bitwise XOR --> non-intersecting regions
    bitwise_xor = cv.bitwise_xor(rectangle, circle)


    bitwise_not = cv.bitwise_not(circle)
    weird_shape = cv.bitwise_and(circle, rectangle)



    imgList = [rectangle, circle, bitwise_and, bitwise_or, bitwise_xor ,bitwise_not]
    stackedImg = cvzone.stackImages(imgList, 3, 0.5)
    cv.imshow("Result", stackedImg)
    #masked = cv.bitwise_and(img0, img0, mask=weird_shape)
    masked = cv.bitwise_and(img0, img0, mask=bitwise_xor)

    cv.imshow('image', masked)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

   
    