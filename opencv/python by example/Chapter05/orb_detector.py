'''
Oriented FAST and Rotated BRIEF (ORB)
page 234
The best combination out of all the combinations that we have
discussed so far. This algorithm came out of the OpenCV Labs.
It’s fast, robust, and opensource!
Both SIFT and SURF algorithms are patented and you can’t use them for
commercial purposes. This is why ORB is good in many ways.

'''

import cv2
import numpy as np
import getpass

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" "fishing_house.jpg"#
mimg = "bb.jpg"
path = BASE_FOLDER + mimg
scaling_factor = 1.1
img   = cv2.imread(path)
input_image = cv2.resize(img, None, fx=scaling_factor,
                         fy=scaling_factor, interpolation=cv2.INTER_AREA)
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY) 
 
# Initiate ORB object, before opencv 3.0.0 use cv2.ORB()
orb = cv2.ORB_create() 
 
# find the keypoints with ORB 
keypoints = orb.detect(gray_image, None) 
 
# compute the descriptors with ORB 
keypoints, descriptors = orb.compute(gray_image, keypoints) 
 
# draw only the location of the keypoints without size or orientation 
cv2.drawKeypoints(input_image, keypoints, input_image, color=(0,255,0)) 
 
cv2.imshow('ORB keypoints', input_image) 
cv2.waitKey() 