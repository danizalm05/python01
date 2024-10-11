"""
 
Tutorial 27 - Using glob to read multiple files in python 
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial27_using_glob_to_read_multiple_images.py
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial27_using_glob_to_read_multiple_images.py

"""
#
import matplotlib.pyplot as plt
import numpy as np
import cv2
import getpass

USER = getpass.getuser()

IMAGE_NAME = '1.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

 