'''
AI Virtual Keyboard using OpenCV  with  two   fingers
https://www.youtube.com/watch?v=jzXZVFqEE2I&t=26s
https://www.computervision.zone/lessons/code-files-18/
https://google.github.io/mediapipe/solutions/solutions.html
https://google.github.io/mediapipe/solutions/hands.html
42:00
'''

import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone


# c:\users\rockman\appdata\local\programs\python\python310\lib\site-packages\pynput-1.7.6.dist-info\*


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
        ["ctr", "X", "C", "V", "spc", "N", "M", ",", ".", "/"]
        ]
finalText = ""




def drawAll(img, buttonList):
    for button in buttonList:  # Scan all the button in the keyboard
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                          20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img


class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos  # [ i,j ]
        self.size = size  # [width ,height]
        self.text = text


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):  # Scan one line in  'keys[[]]'
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

###################################


while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        #bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        #centerPoint1 = hand1["center"]  # center of the hand cx,cy
        #handType1 = hand1["type"]  # Hand Type Left or Right

        img = drawAll(img, buttonList)

        if lmList1: # If we can see   a hand
            for button in buttonList: # Loop all  the buttons
                x, y = button.pos
                w, h = button.size
                # Change  background color of the specific button

                lmx, lmy, _ = (hand1["lmList"][8])
                lm8 = (lmx, lmy)

                if ( x < lmx < x + w and y < lmy < y + h ):
                    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)


                    lmx, lmy, _ = (hand1["lmList"][12])
                    lm12 = (lmx, lmy)

                    print(lm8,' ',button.text)
                    l, _, _ = detector.findDistance(lm8, lm12, img)  # , draw=False)


                    # If clicked  (distance between two fingers is smaller )
                    if l < 80:

                        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 20, y + 65),
                                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        finalText += button.text
                        sleep(0.45)
        y1 = 550
        y2 = y1 + 60
        y3 = y1 + 52
        cv2.rectangle(img, (50, y1), (700, y2), (175, 0, 175), cv2.FILLED)
        cv2.putText(img, finalText, (60, y3),
                    cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

        cv2.imshow("Image", img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
