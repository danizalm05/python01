'''
                                Threshold
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=4017
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=4344

https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/thresh.py

https://docs.opencv.org/4.x/
https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html


'''

import cv2 as cv
#import sys
import getpass

img='2.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
path = BASE_FOLDER+img
print("Image  = ",path) 
print("Image  shape  = ",path) 



import numpy as np
 
from matplotlib import pyplot as plt
 
img = cv.imread(path)
assert img is not None, "file could not be read, check with os.path.exists()"
 
k_size = 7

# Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )


# .median Blur  ( effective against salt-and-pepper)
median = cv.medianBlur(img,k_size)

 
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)

plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.subplot(232),plt.imshow(gray),plt.title('gray')
plt.subplot(233),plt.imshow(thresh),plt.title('bin-thresh') 
plt.subplot(234),plt.imshow(median),plt.title('median') 
plt.subplot(236),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
 

cv.imshow("Display window", img)
cv.imshow(" gray" , gray)
cv.imshow(" Gaussianblur" , thresh)
cv.imshow(" median" , median)

cv.waitKey(0)
cv.destroyAllWindows() 
 
 
