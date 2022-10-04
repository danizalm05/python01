'''
AI Virtual Keyboard using OpenCV  with  your nose.  Close your moush to chose
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
from cvzone.FaceMeshModule import FaceMeshDetector


# c:\users\rockman\appdata\local\programs\python\python310\lib\site-packages\pynput-1.7.6.dist-info\*

(img_w, img_h) = (1280 ,  620)
WHITE = (255, 255, 255)
RED =  (0,0, 255)
GREEN = (0,255, 0)
CLOSE_EYE =35
CLOSE_MOUTH =35
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1


cap = cv2.VideoCapture(0)
cap.set(3, img_w)
cap.set(4, img_h)

#detector = FaceMeshDetector(maxFaces=1)
detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
        ["ctr", "X", "C", "V", " ", "N", "M", ",", ".", "exe"]
        ]


finalText = ["1","2","3","4"]

def keyOp(key):

    if key == 'ex':
        print("exe pressed")

    elif key == "Suzuki":
        print("letter is Suzuki")

    else:
        finalText[0] += key


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
    def __init__(self, pos, text, size=[95, 75]):
        self.pos = pos  # [ i,j ]
        self.size = size  # [width ,height]
        self.text = text


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):  # Scan one line in  'keys[[]]'
        buttonList.append(Button([90 * j + 150, 90 * i + 150], key))


faceDetector = FaceMeshDetector(maxFaces=1)
while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    #img = rescaleFrame(img, 0.7)
    mask = np.zeros((img_h, img_w), dtype=np.uint8)

    img, faces = faceDetector.findFaceMesh(img, draw=False)
    img = drawAll(img, buttonList)
    if faces:
        nose = faces[0][1]# landMark number 1 in face number
        lipup = faces[0][11]  # landMark  of upper lips
        lipdown = faces[0][16]  # landMark
        #left eye
        leftUp = faces[0][159]  # 2 index  coordinate
        leftDown = faces[0][23]
        leftLeft = faces[0][130]
        leftRight = faces[0][243]
        eyeVer, _ = detector.findDistance(leftUp, leftDown)
        eyeHor, _ = detector.findDistance(leftLeft, leftRight)
        ratio = int((eyeVer / eyeHor) * 100)
        cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
        cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)


        cv2.circle(img, lipup, 12, [0, 250, 0], cv2.FILLED)
        cv2.circle(img, lipdown, 12, [0, 250, 0], cv2.FILLED)
        lpd, _, _ = detector.findDistance(lipup, lipdown, img)


    for button in buttonList: # Loop all  the buttons
        x, y = button.pos
        w, h = button.size
        (lmx, lmy) = nose
        # Change  background color of the specific button
        if ( x < lmx < x + w and y < lmy < y + h ):
            cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (75, 0, 75), cv2.FILLED)
            cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

            # If clicked  (distance between two lips is smaller )
            print("lpd ", lpd)
            cv2.putText(img, "lpd =" + str(int(lpd)) , (30, 100), font, 3, RED, 5)
            cv2.putText(img, "eye = "+ str(int(ratio)), (550, 100), font, 3, RED, 5)
            if ratio < CLOSE_EYE:
                cv2.putText(img, "eye = "+ str(int(ratio)), (550, 100), font, 3, GREEN, 5)

            if lpd < CLOSE_MOUTH:
                print("click lpd =  ", lpd)
                cv2.putText(img, "lpd =" + str(int(lpd)) , (30, 100), font, 3, GREEN, 5)


                cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                keyOp(button.text)
                sleep(0.35)


    cv2.circle(img, nose, 12, [255, 250, 0], cv2.FILLED)
    for i in range(4):
        cv2.putText(mask, finalText[i], (37, 160-i*40), font, 1, WHITE, 2)

    imgList = [img, mask]
    stackedImg = cvzone.stackImages(imgList, 1, 0.6)




    cv2.imshow("stackedImg", stackedImg)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
