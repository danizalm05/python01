'''
AI Virtual Keyboard using OpenCV
https://www.youtube.com/watch?v=jzXZVFqEE2I&t=26s
https://www.computervision.zone/lessons/code-files-18/

Multiple Hand Gesture Control with OpenCV Python | CVZone
How to use the updated version
https://www.youtube.com/watch?v=3xfOa4yeOb0

'''


import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller

cap_height = 670  #720
cap_width = 1180 #1280

detector = HandDetector(detectionCon=0.8, maxHands=2)

cap = cv2.VideoCapture(0)
cap.set(3, cap_width)
cap.set(4, cap_height)

while True:
    success, img = cap.read()
    img= cv2.flip(img,1)
    #  hands= detector.findHands(img,draw = false) #do not draw flipetype false
    hands, img = detector.findHands(img,flipType =False)
    '''each hand in the hands list is a dictionary  that  contains 
               hand = dic (lmlist , bbox, center, type)
       '''
    #lmList, bboxInfo = detector.findPosition(img)
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right





    cv2.imshow("Image", img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break