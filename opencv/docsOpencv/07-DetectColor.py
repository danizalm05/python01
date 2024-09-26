'''
07-DetectColors.py

https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=549s  56:00 1:06:00   1:15:00
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter7.py'''

import numpy as np
import cv2
import getpass
import numpy as np
import sys
import os
from inpOpenCV import stackImages,PutTextOnImage, inpTrackbar, get_limits


image_name =  'lambo.png' #'lambo.png' 'cards.jpg'
BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
path = BASE_FOLDER + image_name

if not (os.path.isfile(path)):
    print("ERROR --> Missing File: " + path   )
    sys.exit(1)

inpWin = "TrackBars"
scale = 0.2
inpTrackbar(inpWin)

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


'''
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,320)
cv2.createTrackbar("Hue Min","TrackBars",9,255,empty)
cv2.createTrackbar("Hue Max","TrackBars",24,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",30,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
cv2.createTrackbar("Val Min","TrackBars",175,255,empty)
cv2.createTrackbar("Val Max","TrackBars",250,255,empty)
'''

img = cv2.imread(path)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

colRect = np.ones((212, 212, 3), np.uint8)
cv2.rectangle(colRect, (1,1), (212, 212), (0, 255, 0), -1)
while True:
    scale = cv2.getTrackbarPos("Scale", inpWin)/10 
    #        hue
    h_min = cv2.getTrackbarPos("Hue Min",inpWin)
    h_max = cv2.getTrackbarPos("Hue Max", inpWin)
    #        saturation
    s_min = cv2.getTrackbarPos("Sat Min", inpWin)
    s_max = cv2.getTrackbarPos("Sat Max", inpWin)
    #        value
    v_min = cv2.getTrackbarPos("Val Min", inpWin)
    v_max = cv2.getTrackbarPos("Val Max", inpWin)
    
   
    
    #print(h_min,h_max,s_min,s_max,v_min, v_max)
    lower = np.array([h_min,s_min,v_min])#array of 3 min values
    upper = np.array([h_max,s_max,v_max])
  
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    hue =(h_min + h_max)/2
    sat =(s_min +s_max)/2
    val =(v_min + v_max)/2
     
    print(scale)
    
    cv2.rectangle(colRect, (1,1), (212, 212),(hue,sat,val), -1)
    
     
    imgStack = stackImages(scale,([imgHSV,colRect,img],[mask,imgResult,colRect]))
    #all white values in mask will appear in the result
    cv2.imshow("Result", imgResult)
    cv2.imshow("Stacked Images", imgStack)
     
     
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#cap.release()
cv2.destroyAllWindows()