"""
42 - Histogram equalization and contrast limited adaptive histogram
     equalization (CLAHE)
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial42_what_is_histogram_equalization_CLAHE.py
https://www.youtube.com/watch?v=48WvE9znnRw&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=43
5:23

CLAHE: COntrast limited adaptive histogram equalization
--------------------------------------------------------------
Regular histogram equalization uses global contrast of the image. 
This results in too bright and too dark regions as the histogram stretches 
and is not confined to specific region.

Adaptive histogram equalization divides the image into small tiles and 
within  each tile the histogram is equalized. Tile size is typically 8x8. 
If the image contains noise, it gets amplified during this process. 
Therefore, contrast limiting is applied to limit the contrast below a
 specific limit.
Bilinear interpolation is performed between tile borders. 

We will  perform both histogram equalization and CLAHE and compare the 
results. 
The best way to work with color images is by converting them to luminance 
space, e.g. LAB, and enhancing lumincnace channel only and eventually
combining all channels. 
    
"""


import cv2
import getpass
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np

from PySide6.QtWidgets import QApplication, QWidget
import sys

USER = getpass.getuser()

IMAGE_NAME = '22.jpg' #'2.jpg' 'lena.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

print(IMAGE)

path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  # iterate through each file to perform some action
    print(image)

img = cv2.imread(IMAGE, 1) # load an image
#  Converting image to LAB Color so CLAHE can be applied to the
#  luminance channel
lab_img= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

#Splitting the LAB image to L, A and B channels, respectively
l, a, b = cv2.split(lab_img)



###########Histogram Equlization#############
#Apply histogram equalization to the L channel
equ = cv2.equalizeHist(l)

plt.hist(l.flat, bins=100, range=(0,255))
plt.hist(equ.flat, bins=100, range=(0,255))
plt.show()

#Combine the Hist. equalized L-channel back with A and B channels
updated_lab_img1 = cv2.merge((equ,a,b))

#Convert LAB image back to color (RGB)
hist_eq_img = cv2.cvtColor(updated_lab_img1, cv2.COLOR_LAB2BGR)


#seconed method
###########CLAHE#########################
#Apply CLAHE to L channel
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
clahe_img = clahe.apply(l)
#plt.hist(clahe_img.flat, bins=100, range=(0,255))

#Combine the CLAHE enhanced L-channel back with A and B channels
updated_lab_img2 = cv2.merge((clahe_img,a,b))

#Convert LAB image back to color (RGB)
CLAHE_img = cv2.cvtColor(updated_lab_img2, cv2.COLOR_LAB2BGR)



cv2.imshow("Original image", img)
cv2.imshow("equ", equ)
cv2.imshow("Equalized image", hist_eq_img)
cv2.imshow('CLAHE Image', CLAHE_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

