# -*- coding: utf-8 -*-
"""
OpenCV Python Tutorial #5 - Colors and Color Detection
https://www.youtube.com/watch?v=ddSo8Nb0mTw&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn&index=5
 
Detect blue  objects
"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    #Convert frame from BGR  to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])# One pixel image
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('hsv', hsv)
    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


   