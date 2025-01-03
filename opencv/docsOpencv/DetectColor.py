'''
      DetectColors.py

https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=549s  56:00 1:06:00   1:15:00
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter7.py'''

import numpy as np
import cv2
import getpass
 
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


CameraID = 0

cap = cv2.VideoCapture(CameraID)

inpWin = "TrackBars"
scale = 0.2


inpTrackbar(inpWin)
vid_on = cv2.getTrackbarPos("switch", inpWin)
if (vid_on):
          ret, img = cap.read() 
else: 
          img = cv2.imread(path)
          
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
rect =  np.ones((312, 312, 3), np.uint8)
colRectLow =  cv2.cvtColor(rect,cv2.COLOR_BGR2HSV)
colRectHigh =  cv2.cvtColor(rect,cv2.COLOR_BGR2HSV)
#colRect_copy = colRect.copy()

while True:
    
    #        hue
    h_min = cv2.getTrackbarPos("Hue Min",inpWin)
    h_max = cv2.getTrackbarPos("Hue Max", inpWin)
    #        saturation
    s_min = cv2.getTrackbarPos("Sat Min", inpWin)
    s_max = cv2.getTrackbarPos("Sat Max", inpWin)
    #        value
    v_min = cv2.getTrackbarPos("Val Min", inpWin)
    v_max = cv2.getTrackbarPos("Val Max", inpWin)

    
    scale = cv2.getTrackbarPos("Scale", inpWin)/10 
    vid_on = cv2.getTrackbarPos("switch", inpWin)
    
      
    #print(h_min,h_max,s_min,s_max,v_min, v_max)
    #For HSV, hue range is [0,179], saturation range is [0,255], 
    # and value range is [0,255
    lower = np.array([h_min,s_min,v_min])#array of 3 min values
    upper = np.array([h_max,s_max,v_max])
   
    # Threshold the HSV image to get only the target colors
    if (vid_on):
          _ , img = cap.read() 
          imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
           
          
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    
    
    cv2.rectangle(colRectLow, (1,1), (312, 312),(h_min,s_min,v_min), -1)
    cv2.rectangle(colRectHigh, (1,1), (312, 312),(h_max,s_max,v_max), -1)
    
    stext = str(h_min) + " " +str(s_min) +" " + str(v_min)
    colRectLow =PutTextOnImage(colRectLow ,"Low Color")
    stext = str(h_max) + " " +str(s_max) +" " + str(v_max)
    colRectHigh =PutTextOnImage(colRectHigh ,"High Color") 
    imgStack = stackImages(scale,([imgHSV,colRectLow ,img],  [mask,imgResult,colRectHigh]))
    #All white values in mask window will appear in the result
    imgResult =PutTextOnImage(imgResult ,"Result")
    cv2.imshow("Result", imgResult)
    cv2.imshow("Stacked Images", imgStack)
     
     
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
print(h_min,h_max,s_min ,s_max,v_min , v_max)
cv2.destroyAllWindows()