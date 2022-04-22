import cv2
import time
import PoseEstimate as pm

cameraNum = 0  # -1 : image     0: video
frameWidth = 640
frameHeight = 480
scaling_factor = 0.3
slowMotion = 1
cap = cv2.VideoCapture('4.mp4')


cap.set(3, frameWidth)
cap.set(4, frameHeight)
pTime = 0
detector = pm.poseDetector()

while True:
    success, img = cap.read()
    img = cv2.resize(img, None, fx=scaling_factor,
                     fy=scaling_factor, interpolation=cv2.INTER_AREA)
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) !=0:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("Image", img)
    key = cv2.waitKey(slowMotion)

    if key == ord('q'):
        break
