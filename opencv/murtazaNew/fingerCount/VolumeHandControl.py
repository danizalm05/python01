# -*- coding: utf-8 -*-
"""
  volumne hand control using   HandTrackingModule.py
  www.computervision.zone/topic/gesture-volume-control-part-1-volumehandcontrol-py/
  https://www.youtube.com/watch?v=9iEPzbG-xLE&list=PLMoSUbG1Q_r8jFS04rot-3NzidnV54Z2q
  25:00
  
  pip install pycaw
"""

import cv2
import time
import numpy as np

# The file 'HandTrackingModule.py' must be in the same folder
import HandTrackingModule as htm

import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

camId = 0
wCam, hCam = 640, 480
MinDist, MaxDist = 20, 30
cap = cv2.VideoCapture(camId)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

'''
 handDetector is a class locatd in  HandTrackingModule
 which is loaded as 'htm'
'''
detector = htm.handDetector(detectionCon=0.7)
#

devices = AudioUtilities.GetSpeakers()

interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
print('volRange = ',volRange)#(-96.0, 0.0, 1.5)
volume.SetMasterVolumeLevel(-20.0,None)# 0 is max level


minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        #print(lmList[4], lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 7, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 7, (25, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 7, (25, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        if length < MinDist: MinDist = length
        if length > MaxDist: MaxDist = length
        
        if length < MinDist:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

        print(MinDist,MaxDist)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    msg = f'FPS: {int(fps)}'+ ' ' + str(int(MinDist))+ '  '  + str(int(MaxDist))
    cv2.putText(img, msg, (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (0, 0, 255), 1)
    cv2.imshow("Img", img)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
'''


    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)

        # Hand range 50 - 300
        # Volume Range -65 - 0

        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
 
'''
