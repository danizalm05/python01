import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()  # class

while cv2.waitKey(1) != 27:

    success, img = cap.read()
    img = detector.findHands(img , draw=False) # (Default values handNo=0, draw=Tr
    lmList = detector.findPosition(img, draw=True) # (Default values handNo=0, draw=True)
    lmId = 4
    if len(lmList) != 0: # lmList contains 21 landmark points ([id, cx, cy])
        print(lmList[lmId]) # Output position of this LandMark ( 4 is tip of tomb)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
