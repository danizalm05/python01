'''
Eye Blink Counter using OpenCV Python | Computer Vision
https://www.youtube.com/watch?v=-TVUwH1PgBs
https://www.computervision.zone/lessons/code-and-files-12/
https://www.youtube.com/watch?v=-TVUwH1PgBs&feature=emb_imp_woyt
36:00
'''

import cv2
import cvzone
import numpy as np
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import KeyBoardModule as Kb

FRAME_WIDTH = 640
FRAME_HEIGHT = 480
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

keybrd = Kb.KeyBoard(Kb.keyboard_keys, '')# Initialize the virtual keyboard
buttonL = keybrd.CreateBtnlList()


detector = FaceMeshDetector(maxFaces=1)

maxlim = 50
minlim = 20
plotY = LivePlot(FRAME_WIDTH, FRAME_HEIGHT, [minlim, maxlim], invert=True)
'''
//To run the LivePlot run the next  commands:
 1. ratio = int((lenghtVer / lenghtHor) * 100)
 2. ratioList.append(ratio)
 3. ratioAvg = sum(ratioList) / len(ratioList)
 4. imgPlot = plotY.update(ratioAvg, color)
'''
idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
ratioList = []
blinkCounter = 0
counter = 0
color = (255, 0, 255)

while True:

    # if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
    #    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    img = cv2.flip(img, 1)
    img, faces = detector.findFaceMesh(img, draw=False)
    img_h, img_w = img.shape[:2]
    mask = np.zeros((img_h, img_w), dtype=np.uint8)
    mask = keybrd.DrawKeyBoard(mask, buttonL)


    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img, face[id], 2, color, cv2.FILLED)

        nose = face[1]

        cv2.circle(mask, nose, 5, [255, 255, 255], cv2.FILLED)
        leftUp = face[159]  # 2 index  coordinate
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]
        lenghtVer, _ = detector.findDistance(leftUp, leftDown)
        lenghtHor, _ = detector.findDistance(leftLeft, leftRight)

        cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
        cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)

        ratio = int((lenghtVer / lenghtHor) * 100)
        ratioList.append(ratio)
        if len(ratioList) > 3:  # The ratioList will hold only 3 elements
            ratioList.pop(0)  # remove the first element(the last added element)
        ratioAvg = sum(ratioList) / len(ratioList)
        print ("ratioAvg = ",ratioAvg)
        if ratioAvg < 39 and counter == 0:
            print(nose)
            blinkCounter += 1
            color = (0, 200, 0)  # Change  color to green when blink is detected
            counter = 1
        if counter != 0:
            counter += 1
            if counter > 10:  # don't count blinks in the next 10 frame
                counter = 0
                color = (255, 0, 255)

        cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (50, 100),
                           colorR=color)

        #imgPlot = plotY.update(ratioAvg, color)
        img = cv2.resize(img, (FRAME_WIDTH, FRAME_HEIGHT))
        imgStack = cvzone.stackImages([img, mask], 2, 1)
    else:  # There is no face so we can't plot the graph so we draw the image twice
        img = cv2.resize(img, (FRAME_WIDTH, FRAME_HEIGHT))
        imgStack = cvzone.stackImages([img, img], 2, 1)

    cv2.imshow("Image", imgStack)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
