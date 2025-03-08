"""
 tutorial56_simple_blob_detector.py
 -----------------------------------------------------
 Measure properties of labeled image regions.
https://www.youtube.com/watch?v=2puHfSKnG7c&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=57
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial56_simple_blob_detector.py
image:
    python_for_image_processing_APEER/images/cast_iron1.tif

https://www.learnopencv.com/blob-detection-using-opencv-python-c/

BLOB stands for Binary Large OBject and refers to a group of connected pixels 
in a binary image.
A Blob is a group of connected pixels in an image that share some common
property ( E.g grayscale value ). In the image above, the dark connected 
regions are blobs, 
and the goal of blob detection is to identify and mark these regions.

How it works:
    1. Threshold input images to binary.
    2. Grouping: connected white/black pixels are grouped together. 
    3. Merging: blobs located closer than minDistBetweenBlobs are merged.
    4. Center & Radius Calculation :  The centers and radii of the new merged blobs are computed and returned.
    
Can be filtered by color, size or shape
5:30
"""

 

import matplotlib.pyplot as plt
import numpy as np
import cv2


import getpass
from pathlib import Path
import sys
USER = getpass.getuser()

IMAGE_NAME = 'cast_iron1.tif'  # 'Osteosarcoma_01_transl.tif'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

# Check if the file exists
if not(Path(IMAGE).exists()):
    msg = "Error: file " + IMAGE +" does not exist"
    sys.exit(msg)
   




image = cv2.imread(IMAGE, 0)#Gray image
#img = io.imread(IMAGE1)
#image = img_as_ubyte(rgb2gray(img))
plt.imshow(image, cmap='gray')

#No need to pre-threshold as blob detector has build in threshold.
#We can supply a pre-thresholded image.

# Set up the SimpleBlobdetector with default parameters.
params = cv2.SimpleBlobDetector_Params()

# Define thresholds
#Can define thresholdStep. See documentation. 
params.minThreshold = 0
params.maxThreshold = 255

# Filter by Area.
params.filterByArea = True
params.minArea = 50
params.maxArea = 10000


# Filter by Color (black=0)
params.filterByColor = False  #Set true for cast_iron as we'll be detecting black regions
params.blobColor = 0

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.5
params.maxCircularity = 1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.5
params.maxConvexity = 1

# Filter by InertiaRatio
params.filterByInertia = True
params.minInertiaRatio = 0.1# 0   error: (-5:Bad argument) minDistBetweenBlobs>0 in function
params.maxInertiaRatio = 1

# Distance Between Blobs
params.minDistBetweenBlobs = 1 #0  error: (-5:Bad argument) minDistBetweenBlobs>0 in function

# Setup the detector with parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(image)

print("Number of blobs detected are : ", len(keypoints))
 

# Draw blobs
img_with_blobs = cv2.drawKeypoints(image, keypoints, np.array([]), (250,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img_with_blobs)
plt.show()


 
#============================   Output  ===============================   

fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

ax1 = fig.add_subplot(3,3,1)
ax1.imshow(image, cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(3,3,2)
ax2.imshow(image, cmap='gray')
ax2.title.set_text('thresholded_img')

ax3 = fig.add_subplot(3,3,3)
ax3.hist(image.flat, bins=100, range=(0,255))
ax3.title.set_text('hist color range 100,255')

ax4 = fig.add_subplot(3,3,4)
ax4.imshow(img_with_blobs, cmap='gray')
ax4.title.set_text('img_with_blobs')


ax5 = fig.add_subplot(3,3,5)
ax5.imshow(image)#,cmap='gray')
ax5.title.set_text('label_image')



ax6 = fig.add_subplot(3,3,6)
ax6.imshow(image)#, cmap='gray')
ax6.title.set_text('image_label_overlay')

ax7 = fig.add_subplot(3,3,7)
ax7.imshow(image, cmap='gray')
ax7.title.set_text('binarize entropy image')

plt.show()
 