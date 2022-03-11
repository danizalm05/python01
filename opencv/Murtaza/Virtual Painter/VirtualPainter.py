 
"""
  
AI Virtual Painter | OpenCV Python | Computer Vision

Murtaza's Workshop
https://www.computervision.zone/courses/ai-virtual-painter/lesson/ai-virtual-painter-virtualpainter-py/
https://www.computervision.zone/courses/ai-virtual-painter/lesson/ai-virtual-painter-lesson/  
https://www.youtube.com/watch?v=ZiwZaAVbXQo   
58:00

"""
import cv2
import numpy as np
import time
import os
import HandTrackingModuleN as htm
#######################
camera_number = 0
brushThickness = 25
eraserThickness = 50
folderPath = "pic" # name of picture directory
drawColor = (100, 20,  180)#   default  color
########################


myList = os.listdir(folderPath)

#load header picture in a list
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

header = overlayList[0]

cap = cv2.VideoCapture(camera_number)
(frame_width, frame_hight) = (1280,720)
cap.set(3, frame_width)
cap.set(4, frame_hight)

detector = htm.handDetector(detectionCon=0.65, maxHands=1)
xp, yp = 0, 0
imgCanvas = np.zeros((frame_hight, frame_width, 3), np.uint8)
while True:

    # 1. Import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:

       # tip of index and middle fingers
       x1, y1 = lmList[8][1:]  # x,y of id=8 index finger (move cursor)
       x2, y2 = lmList[12][1:] # x,y of id=12 middle finger (move cursor+left button)


       # 3. Check which fingers are up
       fingers = detector.fingersUp()


       # 4. If Selection Mode - Two finger are up
       if fingers[1] and fingers[2]:
           xp, yp = 0, 0
           spoint,  epoint, color = (x1, y1-25), (x2, y2+25), drawColor
           image = cv2.rectangle(img, spoint, epoint, color,cv2.FILLED)
           # # Checking for the click location
           if y1 < 125:
               if 50 < x1 < 250: #left most option
                   header = overlayList[0]
                   drawColor = (80, 20,  80)
               elif 250 < x1 < 450: #first color
                   header = overlayList[1]
                   drawColor = (255, 0, 255)
               elif 550 < x1 < 750:
                   header = overlayList[2]
                   drawColor = (255, 0, 0)
               elif 800 < x1 < 950:
                   header = overlayList[3]
                   drawColor = (0, 255, 0)
               elif 1050 < x1 < 1200:
                   header = overlayList[4]
                   drawColor = (0, 0, 0)
           cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

       # 5. If Drawing Mode - Index finger is up
       if fingers[1] and fingers[2] == False:
           cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)

           if xp == 0 and yp == 0:
               xp, yp = x1, y1


           if drawColor == (0, 0, 0):#We are erasing so make line Thicker
             cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
             cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)

           else:
             cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
             cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

           xp, yp = x1, y1
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img,imgInv)
    img = cv2.bitwise_or(img,imgCanvas)

    img[0:125, 0:1280] = header
    #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Image", img)
    cv2.imshow("Canvas", imgCanvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break