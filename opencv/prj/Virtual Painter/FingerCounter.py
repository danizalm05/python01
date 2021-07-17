 
"""
 Finger Counter

Murtaza's Workshop
https://www.youtube.com/watch?v=p5Z_GGRCI5s
https://www.computervision.zone/courses/finger-counter/lesson/finger-counter-lesson-2/   
https://www.computervision.zone/courses/finger-counter/lesson/finger-counter-code/
https://google.github.io/mediapipe/solutions/hands.html
30:00

"""

import cv2
import numpy as np
import time
import os
import HandTrackingModuleN as htm

camera_number = 0
pTime = 0
cTime = 0
cap = cv2.VideoCapture(camera_number)
# Create object 'detector'   from 'handDetector()' defined  in 'HandTracingModuleN'
detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)#draw the lines on the hand
    lmList = detector.findPosition(img, draw=False)#Find position onn  the hand
    totalFingers = 0
    if len(lmList) != 0:

         fingers = detector.fingersUp()  #
         print("fingers =", fingers)

         totalFingers = fingers.count(1)#Count the values of '1'  in the list
         cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
         cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                     10, (255, 0, 0), 25)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                 (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
