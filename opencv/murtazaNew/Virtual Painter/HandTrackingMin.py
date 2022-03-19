"""
Hand Tracking 30 FPS using CPU | OpenCV Python (2021) | Computer Vision
   
Murtaza's Workshop

https://www.youtube.com/watch?v=NZde8Xt78Iw
https://www.computervision.zone/courses/hand-tracking/lesson/basics-py-2/   
18:40 
"""
import cv2
import mediapipe as mp
import time

frameWidth = 940
frameHeight = 480
camera_number = 0

cap = cv2.VideoCapture(camera_number)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0  # previous time
cTime = 0  # current time

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:  # if there is at least one hand
        for handLms in results.multi_hand_landmarks:  # for each hand
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark):# [0:20] landmarks each has 3d coordinate
                 print(id, lm)#  id =11       lm = (x: 0.77  y: 0.26  z: -0.36 )
                 h, w, c = img.shape# (480, 640, 3)
                 cx, cy = int(lm.x * w), int(lm.y * h)
                 print("int   = ",id, cx, cy) #cx= 435 cy = 440
                 if id ==  0:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, "fps =" + str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
