"""
#45-Applying filters designed for grey scale to color images (in python)
7:00
#-----------------------------------------------------
 
#https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial45_applying_grey_scale_filters_to_color_images.py
#https://www.youtube.com/watch?v=GWylM5V9v_E&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=46

There are many filters that are designed to work with gray-scale
images but not with color images.
To simplify the process of creating functions that can adapt to RGB images,
scikit-image provides the adapt_rgb decorator.

NOTE: A decorator in Python is any callable Python object that is
used to modify a function or a class.
"""

from skimage.color.adapt_rgb import adapt_rgb, each_channel, hsv_value
from skimage import filters
from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2

import getpass
import os

USER = getpass.getuser()

BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE_NAME = '2.jpg'  # '2.jpg' 'lena.jpg'

img_list = []

for (image) in os.listdir(BASE_FOLDER):  # iterate through each file to perform some action
    img_list.append(image)

img_num = 22
IMAGE = BASE_FOLDER + img_list[img_num]
# IMAGE = BASE_FOLDER + IMAGE_NAME
print(IMAGE)
image = io.imread(IMAGE) #img = cv2.imread(IMAGE, 1)

try_to_apply_sobel = filters.sobel(image)
#Fails on color images as it is a grey filter

#Two ways to apply the filter on color images
#1. Separate R, G and B channels and apply the filter to each channel and put the channel back together.
#2. Convert RGB to HSV and then apply filter to V channel and put it back to HSV and convert to RGB.

#Too many lines of code to do these tasks but with adapt_rgb decorator the task becomes easy.


from skimage import exposure
@adapt_rgb(each_channel) # apply the sobel for each channel speratly and unit them
def eq_each(image):
    output_image = exposure.equalize_hist(image)
    return (output_image)

equ_RGB = eq_each(image)
plt.imshow(equ_RGB)



@adapt_rgb(hsv_value)
def eq_hsv(image):
    output_image = exposure.equalize_hist(image)
    return (output_image)
plt.imshow(image)
plt.show()
