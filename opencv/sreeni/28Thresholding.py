# -*- coding: utf-8 -*-
"""
https://www.youtube.com/watch?v=WQK_oOWW5Zo
https://github.com/bnsreenu/python_for_microscopists
https://github.com/bnsreenu/python_for_microscopists/blob/master/028-image_processing_in_openCV_intro2-Thresholding.py

11:00
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests

import getpass
 
def imreadURL(url, color):
 #Read image from url
 resp = requests.get(url, stream=True).raw
 image = np.asarray(bytearray(resp.read()), dtype="uint8")
 if color == 1 :
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 if color == 0:
        image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
 return image




BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
img_name = "BSE_Google_noisy.jpg"
path = BASE_FOLDER + img_name
img = cv2.imread(path,0)

#u='https'
#img = imreadURL(u, 0)

plt.hist(img.flat,bins=100, range=(0,255))
ret,th = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
# ret is the  optimal  treshold value 

kernel = np.ones((3,3),np.uint8)   # 3x3 kernel with all ones. 
 #Erodes pixels based on the kernel defined
erosion = cv2.erode(th,kernel,iterations = 1)
 #Apply dilation after erosion to see the effect.
dilation = cv2.dilate(erosion,kernel,iterations = 1)  

opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)   


#Start from beinning with Different aproch
median=cv2.medianBlur(img,3)
ret,th = cv2.threshold(median,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 



cv2.imshow("Original Image", img)
cv2.imshow("threshold", th)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("morphologyEx", opening)
cv2.imshow("median", median)
cv2.waitKey(0)
cv2.destroyAllWindows()