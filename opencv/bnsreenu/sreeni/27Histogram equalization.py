'''
Histogram equalization is a good way to stretch the histogram and thus
 improve the image.
Histogram equalization often makes images easy to threshold and further segment.
 This tutorial demonstrates the use of Contrast Limited Adaptive Histogram Equalization
 (CLAHE) and subsequent thresholding using openCV library in Python.

https://www.youtube.com/watch?v=XfDkg3z3BCg
https://github.com/bnsreenu/python_for_microscopists/blob/master/027-image_processing_in_openCV_intro2-Thresholding.py

Alloy.jpg
https://raw.githubusercontent.com/bnsreenu/python_for_microscopists/master/images/Alloy.jpg
6:50
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

import requests

def imreadURL(url, color):
 #Read image from url
 resp = requests.get(url, stream=True).raw
 image = np.asarray(bytearray(resp.read()), dtype="uint8")
 if color == 1 :
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 if color == 0:
        image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
 return image
##############################

USER1 = "gilfm"
USER2 = "rockman"
BASE_FOLDER = 'C:/Users/'+ USER2 +'/Pictures/Saved Pictures/'
img_name = "Alloy.jpg"
path = BASE_FOLDER + img_name
img = cv2.imread(path,0)

###############################
equ = cv2.equalizeHist(img)
plt.hist(img.flat, bins=100, range=(0, 255))
plt.hist(equ.flat, bins=100, range=(0, 255))
plt.title('cv2.equalizeHist(img)')
plt.show()


'''
Histogram Equalization considers the global contrast of the image, may not give good
results.
Adaptive histogram equalization divides images into small tiles and performs 
hist.eq.
Contrast limiting is also applied to minimize amplification of noise.
Together the algorithm is called: Contrast Limited Adaptive Histogram Equalization 
(CLAHE)
'''
# Start by creating a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  #Define tile size and clip limit.
cl1 = clahe.apply(img)

cv2.imshow("Original Image", img)
cv2.imshow("Equalized", equ)
cv2.imshow("CLAHE", cl1)



cv2.waitKey(0)
cv2.destroyAllWindows()

#load image   from  url
u = 'https://iiif.lib.ncsu.edu/iiif/0052574/full/800,/0/default.jpg'
image = imreadURL(u, 1)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()