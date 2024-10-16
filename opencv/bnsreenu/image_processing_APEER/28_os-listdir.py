"""
Tutorial 29 - image_processing using scikit image

https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial29_image_processing_using_scikit-image.py
https://www.youtube.com/watch?v=mQkcf8kgit8&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=30

 resize and rescale.
 edge detection.
 sharpening using deconvolution method
 scratch assay analysis.
#Resize, rescale
"""

import getpass
import os


USER = getpass.getuser()

IMAGE_NAME = '1.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

path = BASE_FOLDER
file_list = os.listdir(path)
print(file_list)  #Very similar to glob, prints a list of all files in the directory

for (image) in os.listdir(path):  #iterate through each file to perform some action
    print(image)
 