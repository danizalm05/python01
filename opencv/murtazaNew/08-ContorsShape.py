'''
08-ContorsShape.py

https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=549s   1:15:00  1:21
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter8.py
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/contours.py
'''


import numpy as np
import cv2
import getpass
import numpy as np
import sys
import os


file_name = 'shapes01.png'  # 'cards.jpg'
BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
path = BASE_FOLDER +  file_name
img00 = cv2.imread(path)

if not (os.path.isfile(path)):
    print("ERROR --> Missing File: " + path   )
    sys.exit(1)


def empty(a):
    pass
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


######################## getContours  ######################

def getContours(img):
    contours,hierarchy = cv2.findContours(img,
                                          cv2.RETR_EXTERNAL,
                                          cv2.CHAIN_APPROX_NONE)
    i = 0
    for cnt in contours:
        i += 1
        area = cv2.contourArea(cnt)

        if area >100:   #  'img00copy' ==> copy of the original image
            cv2.drawContours(img00copy, cnt, -1, (0, 0, 255), 1)
            peri = cv2.arcLength(cnt, True)# closed shapes ==> True
            approx = cv2.approxPolyDP(cnt, 0.03 * peri, True) # closed shapes ==> True
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            print(i, ' : ', area,' peri =  ',peri,'len(approx) = ', objCor)
            print(approx)  #  approx ===> corner   points.
                           #  3 is trinagle 4 rect and >4  circle
            print('cv2.boundingRect(approx) =', cv2.boundingRect(approx))

            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.98 and aspRatio < 1.03:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "None"

            cv2.rectangle(img00copy, (x, y), (x+w, y+h),(0, 220, 0),1)
            cv2.putText(img00copy, objectType ,
                        (x + (w // 2) - 10, y + (h // 2) - 10),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        (0, 0, 0), 2)
#############



img00copy = img00.copy()
gray = cv2.cvtColor(img00, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_DEFAULT)
canny = cv2.Canny(blur, 200, 200)

imgBlank = np.zeros_like(canny)
getContours(canny)
imgStack = stackImages(0.8,([img00,gray,blur],[canny,imgBlank,img00copy]))

cv2.imshow("Stacked Images", imgStack)
cv2.imshow('img00copy', img00copy)
cv2.waitKey(0)