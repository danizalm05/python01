"""
Basic  function  32:00   43:16
OpenCV Course - Full Tutorial with Python
 https://www.youtube.com/watch?v=oXlwWbU8l2o
 https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/basic_functions.py

Murtaza's Workshop - Robotics and AI  17:14  27:34
 https://www.youtube.com/watch?v=WQeoO7MI0Bs&list=PLMoSUbG1Q_r9p7iYBg6z6tZP002DAJ41H
 """
import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/fourier/'
BASE_FOLDER = 'C:/Users/gilfm/Pictures/Saved Pictures/'
#BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
mimg = "lena.png"
path = BASE_FOLDER +  mimg

img0 = cv.imread(path)
img  = rescaleFrame(img0,  scale=.25)
cv.imshow('Original', img)
kernel = np.ones((5, 5), np.uint8)# 5x5 matrix of 1s

# Resize
resized = cv.resize(img, (700,200), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur

sz = 7 # kernal size  must be  odd   number
blur = cv.GaussianBlur(img, (sz,sz), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
tx = 125
ty =175 #treshold tx,ty
cannyblur = cv.Canny(blur, tx, ty)
cv.imshow('Canny Edges blur', cannyblur)

 
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)


imgDialation = cv.dilate(canny,kernel,iterations=5)
cv.imshow('imgDialation', imgDialation)

# Eroding (oposite  of  Dilating
eroded = cv.erode(dilated, (7,7), iterations=1)
cv.imshow('Eroded', eroded)


# Cropping
cropped = img[50:80, 200:230]
#cv.imshow('Cropped', cropped)

cv.waitKey(0)