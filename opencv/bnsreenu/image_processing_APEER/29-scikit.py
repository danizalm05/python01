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
import matplotlib.pyplot as plt

from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean
import getpass
import os


USER = getpass.getuser()

IMAGE_NAME = '1.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  #iterate through each file to perform some action
    print(image)
img = io.imread(IMAGE, as_gray=True) 