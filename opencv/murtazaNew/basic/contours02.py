"""
Contours & Masks using Python & OpenCV -
How to separate object from image background?
https://www.youtube.com/watch?v=JOxebvuRpyo
https://github.com/maksimKorzh/open-cv-tutorials/blob/main/src/contours/contours.py


"""
import cv2
import numpy as np

import getpass

BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #
mimg = "1.jpg"
path = BASE_FOLDER + mimg

img = cv2.imread(path)
cv2.imshow('Original', img)

cv2.waitKey(0)
