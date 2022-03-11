"""
 virtualpaint: project1

Murtaza's Workshop - Robotics and AI   1:55:00  2:15:00
 https://www.youtube.com/watch?v=WQeoO7MI0Bs&list=PLMoSUbG1Q_r9p7iYBg6z6tZP002DAJ41H
 https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/project1.py
 """


# myColors:
# Each  item has 6 number that defines the (hue,sat, value) min and max values
# in the HSL model
# [h_min, s_min, v_min, h_max, s_max, v_max]
# To find the values Use the 'Resource/colorPicker.py' demo in 1:53:00 in
# the youtube film.


'''
day_colors
   blue      90, 118, 105, 114, 194, 255
   red      144, 126, 0,   179, 248, 255
   orange     0, 75,  201, 42,  233, 255
   yellow    17, 29,  243, 35,  162, 255

night_colors
   orange 0,70, 190, 76, 190,255
'''
import cv2
import numpy as np


frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
bright = 150
cap.set(10, bright)


night_colors = [
            [0, 70, 190, 76, 190, 255],
            [133,56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255],
            [90, 48, 0, 118, 255, 255]
          ]

day_colors = [
            [0, 75,  201, 42,  233, 255],
            [133,56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255],
            [90, 48, 0, 118, 255, 255]
          ]

myColorValues = [[51,153,255],          ## BGR
                 [0,0,255],
                 [0,255,0],
                 [255,0,0]]

myPoints =  []  ## [x , y , colorId ]


def findColor(img,myColors ,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
      lower = np.array(color[0:3])
      upper = np.array(color[3:6])
      mask = cv2.inRange(imgHSV, lower, upper)
      x, y = getContours(mask)
      cv2.circle(imgResult, (x, y), 15, myColorValues[count], cv2.FILLED)
      if x != 0 and y != 0:
          newPoints.append([x, y, count])
      count += 1
    return newPoints

def getContours(img):
  contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  x,y,w,h = 0,0,0,0
  for cnt in contours:

       area = cv2.contourArea(cnt)

       if area > 500:
        #cv2.drawContours(imgResult, cnt, -1, (23, 25, 230), 2)
        peri = cv2.arcLength(cnt, True)# closed shapes ==> True
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) # closed shapes ==> True
        x, y, w, h = cv2.boundingRect(approx)
  return x + w // 2, y  # return x center point and y point


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


#----------   Main   program -----------------
while True:
    success, img = cap.read()
    imgResult = img.copy()

    newPoints = findColor(img, day_colors, myColorValues)#night_colors

    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
       drawOnCanvas(myPoints, myColorValues)



    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break