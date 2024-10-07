#!/usr/bin/env python
'''
17 - Read and  count only images files in a directory
Apeer_micro

######################################################################################
### Reading multiple images from a folder
#The glob module finds all the path names
#matching a specified pattern according to the rules used by the Unix shell
#The glob.glob returns the list of files with their full path

https://www.youtube.com/watch?v=52pMFnkDU-4
https://github.com/bnsreenu/python_for_microscopists/blob/master/017-Reading_Images_in_Python.py

'''
import cv2 as cv
import glob
import os
from PIL import Image

from matplotlib import pyplot as plt

# C:\Users\rockman\Anaconda3\envs\tensorflow
USER1 = 'gilfm'
USER2 = 'rockman'
IMAGE_NAME = '1.jpg'
BASE_FOLDER = 'C:/Users/' + USER1 + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME
# Video Playlist: https://www.youtube.com/playlist?list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG
print(IMAGE)

"""
Introductory python tutorials for image processing

Tutorial 3: Appreciating the simplicity of Python code

"""

img = io.imread(IMAGE)
gaussian_img = filters.gaussian(img, sigma=1)

plt.imshow(gaussian_img)
