"""
29 - Key points, detectors and descriptors in openCV
 DigitalSreeni
10:37
https://www.youtube.com/watch?v=DZtUt4bKtmY&list=PLZsOBAyNTZwbIjGnolFydAN33gyyGP7lT&index=30
https://github.com/bnsreenu/python_for_microscopists
https://github.com/bnsreenu/python_for_microscopists/blob/master/029-keypoint%20detectors%20and%20descriptors%20in%20opencv.py
https://github.com/bnsreenu/python_for_microscopists/blob/master/images/grains.jpg

Features = unique regions that the computer can easily tell apart.
(Examples  Corners)
feature detection = Finding these unique features.
Once features are detected we need to find similar ones in a different image.
This means we need to describe the features.
Once you have the features and its description, you can find same features
in all images and align them, stitch them or do whatever you want.
Harris corner detector is a good example of feature detector.

Keypoints are the same thing as points of interest.
They are spatial locations, or points in the image that define what is
interesting or what stand out in the image.
The reason why keypoints are special is because no matter how the image
changes...
whether the image rotates, shrinks/expands, is translated, or distorted
you should be able to find the same keypoints in this modified image when comparing with the original image.
Harris corner detector detects corners.
FAST: Features from Accelerated Segment Test - also detects corners

Each keypoint that you detect has an associated descriptor that accompanies it.
SIFT, SURF and ORB all detect and describe the keypoints.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests

import getpass
 
def imreadURL(url, color):
 #Read image from url
 resp = requests.get(url, stream=True).raw
 image = np.asarray(bytearray(resp.read()), dtype="uint8")
 if color == 1 :
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 if color == 0:
        image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
 return image


u2 = "https://i.ytimg.com/vi/MrggzYPHjYA/maxresdefault.jpg" #monky

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
img_name = "grains.jpg"
path = BASE_FOLDER + img_name
print(path)
img0 = cv2.imread(path)
img = cv2.imread(path)

#############
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)  #Harris works on float32 images.

#Input parameters
# image, block size (size of neighborhood considered), ksize (aperture parameter for Sobel), k
harris = cv2.cornerHarris(gray,2,3,0.04)

# Threshold for an optimal value, it may vary depending on the image.
img[harris>0.01*harris.max()]=[0,0,230]    # replace these pixels with blue

cv2.imshow("Original Image", img0)
cv2.imshow('Harris Corners',img)
cv2.waitKey(0)
cv2.destroyAllWindows()