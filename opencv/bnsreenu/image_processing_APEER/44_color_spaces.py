"""
44 - A note about color spaces in python
7:00
-----------------------------------------------------
 
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial44_a_note_about_color_spaces.py 
https://www.youtube.com/watch?v=kL4j-qGkTnY&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=45 

Color spaces are a way to represent color in the image,
The three main color spaces for image processing are: 
 
 RGB - Red, Green, Blue 
 HSV - Hue, Saturation, Value
 LAB - Lightness, A (Green to red), B (Blue to Yellow)

Image segmentation and analysis tasks are usually 
simplified by converting images from one color space to
 the other. 

"""

import cv2
import numpy as np
from skimage import io
import getpass
import os
 

USER = getpass.getuser()

BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE_NAME = '2.jpg' #'2.jpg' 'lena.jpg'

img_list = []

for (image) in os.listdir(BASE_FOLDER):  # iterate through each file to perform some action
    img_list.append(image)

img_num = 14
IMAGE = BASE_FOLDER + img_list[img_num]
#IMAGE = BASE_FOLDER + IMAGE_NAME

print(IMAGE)
img = cv2.imread(IMAGE, 1)

################   BGR  *
#Needs 8 bit, not float.
color_opencv = cv2.imread(IMAGE, 1)
gray_opencv = cv2.imread(IMAGE, 0)
color_skimage = io.imread(IMAGE, as_gray=False)
gray_skimage = io.imread(IMAGE, as_gray=True)
  
B, G, R = cv2.split(color_opencv)
cv2.imshow("Original", color_opencv)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
#cv2.waitKey(0)          
#cv2.destroyAllWindows() 
 

##########################################################

hsv_image = cv2.cvtColor(color_skimage, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)

cv2.imshow("Original", color_opencv)
cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)


lab_image = cv2.cvtColor(color_skimage, cv2.COLOR_BGR2LAB)
L, A, B = cv2.split(lab_image)

cv2.imshow("Original", color_opencv)
cv2.imshow("lab_L", L)
cv2.imshow("lab_A", A)
cv2.imshow("lab_B", B)


cv2.waitKey(0)          
cv2.destroyAllWindows() 