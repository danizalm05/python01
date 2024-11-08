"""
43 - Shading correction using rolling ball 
              background subtraction
-----------------------------------------------------
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial43_shading_correction_using_rolling_ball.py
https://www.youtube.com/watch?v=BQ-YrAIl2GU&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=44

1st approach: Perform CLAHE
# Equalize light by performing CLAHE on the Luminance channel
# The equalize part alreay covered as aprt of previous tutorials about CLAHE
# This kind of works but you can still see shading after the correction.

2nd approach:
Apply rolling ball background subtraction
pip install opencv-rolling-ball

"""
import cv2
import numpy as np

 


 
import getpass
import os
 

USER = getpass.getuser()

IMAGE_NAME = '3.jpg' #'2.jpg' 'lena.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

print(IMAGE)

path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  # iterate through each file to perform some action
    print(image)

img = cv2.imread(IMAGE, 1) # load an image
 