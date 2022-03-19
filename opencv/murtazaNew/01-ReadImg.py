'''
Read image camera  and  video
https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=549s  9:35
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter1.py
'''


import numpy as np
import cv2
from matplotlib import pyplot as plt
import getpass

frameWidth = 640
frameHeight = 480
BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
######################## READ IMAGE ############################
'''
BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/faces/'
path = BASE_FOLDER+'lena.png'  #'b1.jpg' 'lena.png' 'bb.jpg'
print(path)

img = cv2.imread(path)
cv2.imshow("Lena Soderberg", img)
cv2.waitKey(0)
'''

######################### READ VIDEO #############################
'''
BASE_FOLDER = BASE_FOLDER +'/Videos/Captures/'
path = BASE_FOLDER+'highway.mp4'
print(path)
cap = cv2.VideoCapture(path)
while True:
     success, img = cap.read()
     img = cv2.resize(img, (frameWidth, frameHeight))
     cv2.imshow("Result", img)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break

'''

######################### READ WEBCAM  ############################

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break