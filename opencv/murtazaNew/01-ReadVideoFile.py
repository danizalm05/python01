'''
Read   video  file
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
 
 
 
BASE_FOLDER = BASE_FOLDER +'/Videos/Captures/'
 
path = BASE_FOLDER+'dog.mp4'
print(path)

if os.path.isfile(path):
   cap = cv2.VideoCapture(path)
   while True:
     success, img = cap.read()
     img = cv2.resize(img, (frameWidth, frameHeight))
     cv2.imshow("Result", img)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
else:
    print("ERROR --> Missing File: " + path   )
