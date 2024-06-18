'''
Read   and display image
https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=549s  9:35
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter1.py
'''


import numpy as np
import cv2
from matplotlib import pyplot as plt
import getpass
import os

frameWidth = 640
frameHeight = 480
BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
######################## READ IMAGE ############################
 

BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
path = BASE_FOLDER+'2.jpg'  #'b1.jpg' 'lena.png' 'bb.jpg'

if os.path.isfile(path):
    img = cv2.imread(path)
    cv2.imshow("my image", img)
    cv2.waitKey(0)

else:
    print("ERROR --> Missing File: " + path   )

