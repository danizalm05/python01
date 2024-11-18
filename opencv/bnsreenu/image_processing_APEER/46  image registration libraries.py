"""
46 - Useful image registration libraries in python 
#-----------------------------------------------------
https://www.youtube.com/watch?v=F4AV6SsUxXE&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=47
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial46_img_registration_libraries_in_python.py

https://github.com/bnsreenu/python_for_image_processing_APEER/tree/master/images

A couple of ways to perform image registration
https://image-registration.readthedocs.io/en/latest/image_registration.html

pip install image_registration
 
input photos:   Osteosarcoma_01.tif Osteosarcoma_01_transl.tif
 
07:00
"""
import cv2
from skimage import io
import numpy
from image_registration import chi2_shift

import getpass
import os
print(numpy.__version__)
USER = getpass.getuser()

BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE_NAME_1 = 'Osteosarcoma_01.tif'  # '2.jpg' 'lena.jpg'
IMAGE_NAME_2 = 'Osteosarcoma_01_transl.tif'
img_list = []

for (image) in os.listdir(BASE_FOLDER):  # iterate through each file to perform some action
    img_list.append(image)

img_num = 17
IMAGE = BASE_FOLDER + img_list[img_num]
IMAGE1 = BASE_FOLDER + IMAGE_NAME_1
IMAGE2 = BASE_FOLDER + IMAGE_NAME_2
print(IMAGE1)
 
 

image = io.imread(IMAGE_NAME_1 , as_gray=True)
offset_image = io.imread(IMAGE_NAME_2 , as_gray=True)
# offset image translated by (-17, 18.) in y and x 


#Method 1: chi squared shift
#Find the offsets between image 1 and image 2 using the DFT upsampling method
# 2D rigid

noise=0.1
xoff, yoff, exoff, eyoff = chi2_shift(image, offset_image, noise, 
                                      return_error=True, upsample_factor='auto')

print("Offset image was translated by: 18, -17")
print("Pixels shifted by: ", xoff, yoff)

from scipy.ndimage import shift
corrected_image = shift(offset_image, shift=(-xoff,-yoff), mode='constant')

from matplotlib import pyplot as plt
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(image, cmap='gray')
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(offset_image, cmap='gray')
ax2.title.set_text('Offset image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(corrected_image, cmap='gray')
ax3.title.set_text('Corrected')
plt.show()

###########################################################################

