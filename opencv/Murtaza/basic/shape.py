"""
 Shapes
Murtaza's Workshop - Robotics and AI  34:50  45:00
 https://www.youtube.com/watch?v=WQeoO7MI0Bs&list=PLMoSUbG1Q_r9p7iYBg6z6tZP002DAJ41H
 """

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
img[100:290,30:180]= 200, 140, 140#Blue  ractangle
cv2.imshow("img[:]= 200,140,140",img)
img[:] = 0, 0, 0
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0,0,255),2)
cv2.circle(img, (400, 50), 30, (255, 255,0),5)
cv2.putText(img, "cv2.putText", (100,100),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)


cv2.imshow("Image",img)

cv2.waitKey(0)