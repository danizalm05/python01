"""
 Faces0
 viola and  jones
Murtaza's Workshop - Robotics and AI  1:40:00   1:46:00
 https://www.youtube.com/watch?v=WQeoO7MI0Bs&list=PLMoSUbG1Q_r9p7iYBg6z6tZP002DAJ41H
 """

import cv2
import numpy as np

xml_file = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(xml_file)
BASE_FOLDER = "C:/Users/gilfm/Pictures/Saved Pictures/"
#BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
img_name = "lena.png"
path = BASE_FOLDER + img_name
print(path)
img = cv2.imread(path)
cv2.imshow("ImageStack",img)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("imgGray",imgGray)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result", img)
cv2.waitKey(0)