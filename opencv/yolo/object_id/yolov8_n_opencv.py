'''
https://github.com/DAVIDNYARKO123/yolov8-silva/blob/main/yolov8_n_opencv.py
https://youtu.be/hg4oVgNq7Do?t=728


Results saved to D:\python02\opencv\yolo\object_id\runs\detect\predict-......
'''


import sys
import getpass
 
 

import random
import cv2
import numpy as np
from ultralytics import YOLO

img='cats.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
path = BASE_FOLDER+img
print("Image  = ",path) 

 