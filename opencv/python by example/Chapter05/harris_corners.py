import cv2 
import numpy as np
import getpass

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #
mimg = "b1.jpg"
path = BASE_FOLDER + mimg
scaling_factor =0.5
img   = cv2.imread(path)
img = cv2.resize(img, None, fx=scaling_factor,
                   fy=scaling_factor, interpolation=cv2.INTER_AREA)
cv2.imshow('Original', img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
gray = np.float32(gray) 
 
# To detect only sharp corners 
dst = cv2.cornerHarris(gray, blockSize=4, ksize=5, k=0.04)
# Result is dilated for marking the corners 
dst = cv2.dilate(dst, None) 
 
# Threshold for an optimal value, it may vary depending on the image
img[dst > 0.01*dst.max()] = [0,0,0]
cv2.imshow('Harris Corners(only sharp)',img) 

# to detect soft corners 
dst = cv2.cornerHarris(gray, blockSize=14, ksize=5, k=0.04)
dst = cv2.dilate(dst, None)
img[dst > 0.01*dst.max()] = [0,0,0] 
cv2.imshow('Harris Corners(also soft)',img) 

cv2.waitKey() 