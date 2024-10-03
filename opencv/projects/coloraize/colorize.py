"""
Black and white image colorization using Python, OpenCV and Deep Learning
https://www.youtube.com/watch?v=gAmskBNz_Vc
https://github.com/balajisrinivas/Colorizing-black-and-white-images-using-Python/blob/master/colorize.py
"""

# Import statements
import numpy as np
import argparse
import cv2
import os
import getpass
"""
Download the model files: 
1. colorization_deploy_v2.prototxt:    https://github.com/richzhang/colorization/tree/caffe/colorization/models
2. pts_in_hull.npy:					   https://github.com/richzhang/colorization/blob/caffe/colorization/resources/pts_in_hull.npy
3. colorization_release_v2.caffemodel: https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1

"""

# Paths to load the model
DIR = r"C:\Users\Balaji\Documents\colorize"

 
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
mimg = "pic3.jpg"# 'pic2.jpg'
img_path  = BASE_FOLDER + mimg
print(img_path) 