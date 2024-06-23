'''
Shapes and Text
https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=549s  34:00  37:54
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter4.py
'''


import numpy as np
import cv2
import getpass
import os

frameWidth = 640
frameHeight = 480


img = np.zeros((512,512,3),np.uint8)
print(img)
cv2.imshow("Image",img) #black screen
cv2.waitKey(0)
img[200:300,200:300]= 255,0,0#blue squre on black  background
cv2.imshow("Image",img)
cv2.waitKey(0)
print(img)

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
file_name = '22.jpg'
path = BASE_FOLDER + file_name   


print(path)
if os.path.isfile(path):
     img = cv2.imread(path)
     print(img.shape)
     cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
     cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
     cv2.circle(img,(400,50),30,(255,255,0),5)
     cv2.putText(img,"OPENCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)
     cv2.imshow("Image",img)
     cv2.waitKey(0)
else:
    print("ERROR --> Missing File: " + path   ) 


