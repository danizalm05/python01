"""
Basic  function  32:00   43:16
OpenCV Course - Full Tutorial with Python
 https://www.youtube.com/watch?v=oXlwWbU8l2o
 https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/basic_functions.py

Murtaza's Workshop - Robotics and AI  17:14  27:34
 https://www.youtube.com/watch?v=WQeoO7MI0Bs&list=PLMoSUbG1Q_r9p7iYBg6z6tZP002DAJ41H
 """
import cv2  
import numpy as np
import matplotlib.pyplot as plt
import getpass

  

BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #
mimg ="1.jpg"#1.jpg"#"basketball.jpg"  "image.png"#
path = BASE_FOLDER + mimg
print(path)
original_image = cv2.imread(path)
image1_copy = original_image.copy()
image_gray = cv2.cvtColor(image1_copy, cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY)

# Find all contours in the image.
contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
print("Number of contours:" + str(len(contours)))
# Get the bounding rectangle
 
rect = cv2.minAreaRect(contours[4])

box =  cv2.boxPoints(rect).astype('int')
print(box)
# Draw a rectangle around the object
cv2.drawContours(image1_copy,[box],0,(0,255,0),3)
#cv2.rectangle(image1_copy,rect,(255,0,0),3)
cv2.imshow("result",image1_copy)
while True: 
   
   cv2.imshow("image_gray",image_gray)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
cv2.destroyAllWindows()