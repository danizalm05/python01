"""
Blurr
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/blurring.py
 1:30:10 1:37:10
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
cv.imshow('org', img0)

def nothing(x):
    pass


cv.namedWindow('image')
cv.createTrackbar('AVR', 'image', 3, 9, nothing)
cv.createTrackbar('GUS', 'image', 3, 11, nothing)
cv.createTrackbar('MEDIAN', 'image', 3, 11, nothing)


while (True):
    #cv.imshow('image', img)
    avr = cv.getTrackbarPos('AVR', 'image')
    if avr<3: avr =3
    gus = cv.getTrackbarPos('GUS', 'image')
    if (gus % 2) == 0:
        gus = gus + 1
    if gus < 3: gus = 3

    med = cv.getTrackbarPos('MEDIAN', 'image')
    if (med % 2) == 0:
        med = med + 1
    if med < 3: med = 3



    #img[:] = [b, g, r]
    average = cv.blur(img0, (avr, avr))
    gauss   = cv.GaussianBlur(img0, (gus, gus), 0)
    median = cv.medianBlur(img0, med)
    # Bilateral
    bilateral = cv.bilateralFilter(img0, 10, 35, 25)
    imgList = [img0, average, gauss, median, bilateral, img0]
    stackedImg = cvzone.stackImages(imgList, 3, 0.6)
    cv.imshow("blur", stackedImg)


    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

   
    