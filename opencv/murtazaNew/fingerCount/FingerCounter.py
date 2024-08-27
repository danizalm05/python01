
"""
Finger Counter (using   HandTrackingModule.py)
  https://www.computervision.zone/lessons/code-files-13/
 https://www.youtube.com/watch?v=p5Z_GGRCI5s&t=1s
 
 32:00
"""
import cv2
import time
import os
import HandTrackingModule as htm
import getpass
 
BASE_FOLDER = 'C:/Users/'+ getpass.getuser() 
path = BASE_FOLDER +'/Pictures/Saved Pictures/'

wCam, hCam = 640, 480
cam_ID = 0

cap = cv2.VideoCapture(cam_ID)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0


detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)


    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)


        totalFingers = fingers.count(1)#count the number of 1 in the finger list
        print(totalFingers)



        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:
      cv2.destroyAllWindows()
      cap.release()
      break

   