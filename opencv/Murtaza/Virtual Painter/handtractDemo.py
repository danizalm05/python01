"""
Hand Tracing Module
Hand Tracking 30 FPS using CPU | OpenCV Python (2021) | Computer Vision
   
Murtaza's Workshop Website: https://www.computervision.zone

https://www.youtube.com/watch?v=NZde8Xt78Iw
https://www.computervision.zone/courses/hand-tracking/lesson

26:40
"""

"""
Hand Tracing Module
By: Murtaza Hassan
Youtube: http://www.youtube.com/c/MurtazasWorkshopRoboticsandAI
Website: https://www.computervision.zone
"""
import cv2
import mediapipe as mp
import time
import HandTrackingModuleN as htm

camera_number = 0
pTime = 0
cTime = 0
cap = cv2.VideoCapture(camera_number)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True )
    lmList = detector.findPosition(img, draw=True)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
     #           (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


