"""
masking.py  2:00:00   2:15:00
OpenCV Course - Full Tutorial with Python
www.youtube.com/watch?v=oXlwWbU8l2o
histogram: distrabution  of pixel  intensity
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/histogram.py
   """
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def hist(ihist, title):
    plt.figure()
    plt.title(title)
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    plt.plot(ihist)
    plt.xlim([0, 256])  # limit of the X aix


BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
mimg = "bz.JPG"
path = BASE_FOLDER + mimg

img0 = cv.imread(path)
#cv.imshow('Original', img0)

# Resizing

(m, n) = (int(img0.shape[0] // 4), int(img0.shape[1] // 4))

resized = cv.resize(img0, (m, n), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
img = resized

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



# GRayscale histogram
#            calcHist(images, channels, mask, histSize, ranges) _

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256] )

hist(gray_hist, 'Grayscale Histogram')


circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Mask', masked)

gray_hist1 = cv.calcHist([gray], [0], circle, [256], [0, 256] )
hist(gray_hist1, 'Grayscale Histogram Masked')

cv.imshow('Original Image', resized)

# Colour Histogram

plt.figure()
plt.title('Colour Histogram masked Image')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([resized], [i], circle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])


plt.show()
cv.waitKey(0)