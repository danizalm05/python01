'''
Apeer_micro
Dr Sreenivas Bhattiprolu
https://twitter.com/digitalsreeni

Tutorial 30 - Basic image processing using opencv.
Apeer_micro
Dr Sreenivas Bhattiprolu
https://www.youtube.com/watch?v=3J1YG17FDjw&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=31
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial30_image_processing_using_opencv.py
Video Playlist:
https://www.youtube.com/playlist?list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG

Useful preprocessing steps for image processing, for example segmentation.
#1. SPlit & Merge channels
#2. Scaling / resizing
#4. Edge detection
https://docs.opencv.org/3.3.1/da/d6e/tutorial_py_geometric_transformations.html
'''
import numpy as np
from matplotlib import pyplot as plt
import cv2
import scipy.fftpack

import getpass

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
     # "modrain.jpg"#"grains.jpg" #

print(BASE_FOLDER)
img0 = cv2.imread(BASE_FOLDER + "lena.png",0)
img1 = cv2.imread(BASE_FOLDER + 'p3.jpg',0)
img2 = cv2.imread(BASE_FOLDER + 'p2.jpg',0)

print(BASE_FOLDER + "lena.png")

# Images Input, layout, and transforms

img_input = [img0, img1, img2]
picture_name = ['lena', 'moderian', 'horizen' ]
'''
i=0
for x in img_input:
     cv2.imshow(picture_name[i], x)
     print (i,picture_name[i])
     i += 1
cv2.waitKey(0)
'''
img = cv2.imread(BASE_FOLDER + "lena.png",1) #Color is BGR not RGB


#use cv2.resize. Can specify size or scaling factor.
#Inter_cubic or Inter_linear for zooming.
#Use INTER_AREA for shrinking
#Following xample zooms by 2 times.

resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow("original pic", img0)
cv2.imshow("resized pic", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


###################################
#Pixel values, split and merge channels,


grey_img = cv2.imread(BASE_FOLDER + "p1.jpg", 0)
img      = cv2.imread(BASE_FOLDER + "p1.jpg", 1)   #Color is BGR not RGB
h, w, c = img.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)

print("Top left", img[0,0])    #Top left pixel
print("Top right", img[0, w-1])  # Top right
print("Bottom Left", img[h-1, 0]) # Bottom left
print("Bottom right", img[h-1, h-1])  # Bottom right

cv2.imshow("color pic", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Split and merging channels
#Show individual color channels in the image
blue = img[:, :, 0]   #Show only blue pic. (BGR so B=0)
green = img[:, :, 1]  #Show only green pixels
red = img[:, :, 2]  #red only


cv2.imshow("red pic", red)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Or split all channels at once

b,g,r = cv2.split(img)

cv2.imshow("green pic", g)
cv2.waitKey(0)
cv2.destroyAllWindows()

#to merge each image into bgr

img_merged = cv2.merge((b,g,r))

cv2.imshow("merged pic", img_merged)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Edge detection:
edges = cv2.Canny(img1,100,200)   #Image, min and max values

cv2.imshow("Original Image", img1)
cv2.imshow("Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()