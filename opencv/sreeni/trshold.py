'''

https://www.youtube.com/watch?v=XfDkg3z3BCg
https://github.com/bnsreenu/python_for_microscopists/blob/master/027-image_processing_in_openCV_intro2-Thresholding.py

Alloy.jpg
https://raw.githubusercontent.com/bnsreenu/python_for_microscopists/master/images/Alloy.jpg

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

import requests



USER1 = "gilfm"
USER2 = "rockman"
BASE_FOLDER = 'C:/Users/'+ USER2 +'/Pictures/Saved Pictures/'
img_name = "Alloy.jpg"
path = BASE_FOLDER + img_name
img = cv2.imread(path,0)

##########################
#Adaptive histogram equalization using CLAHE to stretch the histogram.
#Contrast Limited Adaptive Histogram Equalization covered in the previous tutorial.
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  #Define tile size and clip limit.
clahe_img = clahe.apply(img)
plt.hist(clahe_img.flat, bins=100, range=(100, 255))
plt.show()
#Thresholding. Creates a uint8 image but with binary values.
#Can use this image to further segment.

#1'st  argument: source grayscale image.
#2'nd argument: threshold value  to classify the pixel values.
#3'rd  argument: maxVal,the value to be given to the thresholded pixel.

#All thresholded pixels in grey = 150
ret,thresh1 = cv2.threshold(clahe_img,185,150,cv2.THRESH_BINARY)

# All thresholded pixels in white
ret,thresh2 = cv2.threshold(clahe_img,185,255,cv2.THRESH_BINARY_INV)

cv2.imshow("Original", img)
cv2.imshow("Binary thresholded", thresh1)
cv2.imshow("Inverted Binary thresholded", thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()





plt.hist(clahe_img.flat, bins =100, range=(0,255))
plt.hist(thresh1.flat, bins =100, range=(0,255))
plt.hist(thresh2.flat, bins =100, range=(0,255))

plt.show()


#OTSU Thresholding, binarization
 

 

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  #Define tile size and clip limit. 
clahe_img = clahe.apply(img)

plt.hist(clahe_img.flat, bins =100, range=(0,255))

# binary thresholding
ret1,th1 = cv2.threshold(clahe_img,185,200,cv2.THRESH_BINARY)

# Otsu's thresholding, automatically finds the threshold point. 
#Compare wth above value provided by us (185)
ret2,th2=cv2.threshold(clahe_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow("Otsu", th2)
cv2.waitKey(0)          
cv2.destroyAllWindows() 
