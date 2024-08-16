# -*- coding: utf-8 -*-
"""
 '''Demo of using thr HandTrackingModule.py 
 https://www.youtube.com/watch?v=NZde8Xt78Iw&t=0s  36:01
 hand gesture https://www.youtube.com/watch?v=9iEPzbG-xLE
 '''
"""
import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

camID =0 
pTime = 0
cTime = 0
cap = cv2.VideoCapture(camID)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True )#draw=False no lines
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
     #           (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:
      cv2.destroyAllWindows()
      cap.release()
      break