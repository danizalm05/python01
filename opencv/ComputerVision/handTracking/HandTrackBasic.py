# Hand Tracking 30 FPS
# https://www.youtube.com/watch?v=NZde8Xt78Iw 20:00
#https://www.computervision.zone/courses/hand-tracking/
# Shift+F10  execute .
# Press Double Shift to search  for classes, files, tool windows,
#

import cv2
import mediapipe as mp
import time

webcamNumber =  0
cap = cv2.VideoCapture(webcamNumber)

mpHands = mp.solutions.hands
hands = mpHands.Hands()  # Click+Ctrl to view parameters
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()  # Get a frame
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # hands object only uses RGB
    results = hands.process(imgRGB)  # Process one frame
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # for every hand
            # Scan 21 landmarks points(lm)
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print("id = ", id, " (cx , cy) =  ", cx, cy)
                if id == 4:  # If this is the tip of the tomb
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                else:
                    cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
