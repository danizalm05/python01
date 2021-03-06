"""
21:00
30 - Image registration using homography in openCV
 DigitalSreeni
https://www.youtube.com/watch?v=cA8K8dl-E6k
https://www.youtube.com/watch?v=X_pCiVQ4c4E&list=PLZsOBAyNTZwbIjGnolFydAN33gyyGP7lT
https://github.com/bnsreenu/python_for_microscopists
https://github.com/bnsreenu/python_for_microscopists/blob/master/030-keypoints_homography_for_registration%20in%20opencv.py

images:
https://github.com/bnsreenu/python_for_microscopists/blob/master/images/monkey.jpg
https://raw.githubusercontent.com/bnsreenu/python_for_microscopists/master/images/monkey_distorted.jpg

opencv docs
https://docs.opencv.org/master/db/d27/tutorial_py_table_of_contents_feature2d.html
Brute-Force Matching with ORB Descriptors
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests

import getpass
BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
     # "modrain.jpg"#"grains.jpg" #

path1 = BASE_FOLDER + "p1.jpg"#"monkey_distorted.jpg"
path2 = BASE_FOLDER + "p2.jpg"#"monkey.jpg"

im1 = cv2.imread(path1)  # Image that needs registered
im2 = cv2.imread(path2)  # train Image

img1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

# Initiate ORB detector
orb = cv2.ORB_create(50)  #Registration works with at least 50 points


# find the key points and descriptors with orb
kp1, des1 = orb.detectAndCompute(img1, None)  #kp1 --> list of KeyPoints
kp2, des2 = orb.detectAndCompute(img2, None)

#Brute-Force matcher takes the descriptor of one feature in first set and is
#matched with all other features in second set using some distance calculation.
# create Matcher object

matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)

# Match descriptors.
matches = matcher.match(des1, des2, None)  #Creates a list of all matches, just like keypoints

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
#cv2.drawMatches() helps us to draw the matches.
#https://docs.opencv.org/3.0-beta/modules/features2d/doc/drawing_function_of_keypoints_and_matches.html
# Draw first 10 matches.
img3 = cv2.drawMatches(im1,kp1, im2, kp2, matches[:10], None)

#Now let us use these key points to register two images.
#For this task we will use homography.
# https://docs.opencv.org/3.4.1/d9/dab/tutorial_homography.html

# Extract location of good matches.
# For this we will use RANSAC.
#RANSAC is abbreviation of RANdom SAmple Consensus,
#in summary it can be considered as outlier rejection method for keypoints.
#http://eric-yuan.me/ransac/
#RANSAC needs all key points indexed, first set indexed to queryIdx
#Second set to #trainIdx.

points1 = np.zeros((len(matches), 2), dtype=np.float32)  #empty array of size  (matches, 2)
points2 = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches):
    points1[i, :] = kp1[match.queryIdx].pt    #gives index of the descriptor in the list of query descriptors
    points2[i, :] = kp2[match.trainIdx].pt    #gives index of the descriptor in the list of train descriptors

#Now we have all good key points so we are ready for homography.
# Find homography
#https://en.wikipedia.org/wiki/Homography_(computer_vision)

h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

# Use homography
height, width, channels = im2.shape
im1Reg = cv2.warpPerspective(im1, h, (width, height))  #Applies a perspective transformation to an image.

print("Estimated homography : \n",  h)




cv2.imshow("Matches image", img3)


img11 = cv2.drawKeypoints(img1, kp1, None, flags=0)
img22 = cv2.drawKeypoints(img2, kp2, None, flags=0)
cv2.imshow("img11", img11)
cv2.imshow("img22", img22)

cv2.imshow("Registered image", im1Reg)
cv2.waitKey(0)
