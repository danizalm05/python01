"""
29 - Key points, detectors and descriptors in openCV
 DigitalSreeni
10: - 18:50
https://www.youtube.com/watch?v=DZtUt4bKtmY&list=PLZsOBAyNTZwbIjGnolFydAN33gyyGP7lT&index=30
https://github.com/bnsreenu/python_for_microscopists
https://github.com/bnsreenu/python_for_microscopists/blob/master/029-keypoint%20detectors%20and%20descriptors%20in%20opencv.py
https://github.com/bnsreenu/python_for_microscopists/blob/master/images/grains.jpg
https://docs.opencv.org/master/db/d27/tutorial_py_table_of_contents_feature2d.html
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
img_name = "p1.jpg"     # "modrain.jpg"#"grains.jpg" #
path = BASE_FOLDER + img_name
print(path)
img0 = cv2.imread(path)
img = cv2.imread(path)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#input image, #points, quality level (0-1), min euclidean dist. between detected points
#https://docs.opencv.org/master/d4/d8c/tutorial_py_shi_tomasi.html
corners = cv2.goodFeaturesToTrack(gray,55,0.01,10)
corners = np.int0(corners)   #np.int0 is int64

for i in corners:
    x,y = i.ravel()   # Ravel Returns a contiguous flattened array.
    print(x,y)
    cv2.circle(img,(x,y),3,255,-1)  #Draws circle (Img, center, radius, color, etc.)

cv2.imshow('Corners',img)
cv2.imshow("Original Image", img0)

cv2.waitKey(0)
cv2.destroyAllWindows()


#####################################
#SIFT and SURF - do not work in opencv 3
#SIFT stands for scale invariant feature transform
#####################################
# FAST
# Features from Accelerated Segment Test
# High speed corner detector
# FAST is only keypoint detector. Cannot get any descriptors.






# Initiate FAST object with default values
detector = cv2.FastFeatureDetector_create(50)   #Detects 50 points
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kp = detector.detect(gray, None)

img2 = cv2.drawKeypoints(img, kp, None, flags=0)

cv2.imshow('Corners',img2)
cv2.waitKey(0)

#ORB
# Oriented FAST and Rotated BRIEF
# An efficient alternative to SIFT or SURF
# ORB is basically a fusion of FAST keypoint detector and BRIEF descriptor




img = cv2.imread(path)

orb = cv2.ORB_create(100)


kp, des = orb.detectAndCompute(img, None)


# draw only keypoints location,not size and orientation
#img2 = cv2.drawKeypoints(img, kp, None, flags=None)
# Now, let us draw with rich key points, reflecting descriptors.
# Descriptors here show both the scale and the orientation of the keypoint.
img2 = cv2.drawKeypoints(img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("With keypoints", img2)
cv2.waitKey(0)

############################################################
#Next lecture. Use this information to register images.