"""
46 - Useful image registration libraries in python 
#-----------------------------------------------------
https://www.youtube.com/watch?v=F4AV6SsUxXE&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=47
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial46_img_registration_libraries_in_python.py

https://github.com/bnsreenu/python_for_image_processing_APEER/tree/master/images

A couple of ways to perform image registration
https://image-registration.readthedocs.io/en/latest/image_registration.html

pip install image_registration
 
Osteosarcoma_01.tif
Osteosarcoma_01_transl
 

image = io.imread("images/Osteosarcoma_01.tif", as_gray=True)
offset_image = io.imread("images/Osteosarcoma_01_transl.tif", as_gray=True)
"""
import cv2
from skimage import io
import numpy
#from image_registration import chi2_shift

import getpass
import os
print(numpy.__version__)
USER = getpass.getuser()

BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE_NAME_1 = 'Osteosarcoma_01_25Sigma_noise.tif'  # '2.jpg' 'lena.jpg'
IMAGE_NAME_2 = 'Osteosarcoma_01_transl'
img_list = []

for (image) in os.listdir(BASE_FOLDER):  # iterate through each file to perform some action
    img_list.append(image)

img_num = 17
# IMAGE = BASE_FOLDER + img_list[img_num]
IMAGE1 = BASE_FOLDER + IMAGE_NAME_1
IMAGE2 = BASE_FOLDER + IMAGE_NAME_2
print(IMAGE1)