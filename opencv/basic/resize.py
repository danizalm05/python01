"""
 resize
Murtaza's Workshop - Robotics and AI  27:34 34:40
 https://www.youtube.com/watch?v=WQeoO7MI0Bs&list=PLMoSUbG1Q_r9p7iYBg6z6tZP002DAJ41H
 """

import cv2
import numpy as np
def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
mimg = "bz.JPG"
path = BASE_FOLDER +  mimg

img = cv2.imread(path)
img0  = rescaleFrame(img,  scale=.25)
cv2.imshow('Original scale=.25', img0)

print(img.shape)

imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)
cv2.imshow('imgResize = cv2.resize(img,(1000,500)) ', imgResize)
imgCropped = img[46:119,200:495]

cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)