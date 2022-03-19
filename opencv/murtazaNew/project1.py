#https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=549s    01:47:00

import cv2
import numpy as np



frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break