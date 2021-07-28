'''
page  219
'''

import cv2
import numpy as np


import getpass

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" "fishing_house.jpg"#
mimg = "bb.jpg"
path = BASE_FOLDER + mimg
scaling_factor =0.9
img   = cv2.imread(path)
input_image = cv2.resize(img, None, fx=scaling_factor,
                 fy=scaling_factor, interpolation=cv2.INTER_AREA)

gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY) 
 
# For version opencv < 3.0.0, use cv2.SIFT()
sift = cv2.xfeatures2d.SIFT_create() 
keypoints = sift.detect(gray_image, None)
 
cv2.drawKeypoints(input_image, keypoints, input_image, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
 
cv2.imshow('SIFT features', input_image) 
cv2.waitKey() 