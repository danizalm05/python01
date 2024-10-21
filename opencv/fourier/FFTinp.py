"""
 

 
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import getpass

def empty(a):
    pass
def getTrackVal(inpWin):
    radius = cv2.getTrackbarPos("radius", inpWin)
    h_max = cv2.getTrackbarPos("Hue Max", inpWin)
    #        saturation
    s_min = cv2.getTrackbarPos("Sat Min", inpWin)
    s_max = cv2.getTrackbarPos("Sat Max", inpWin)
    #        value
    v_min = cv2.getTrackbarPos("Val Min", inpWin)
    v_max = cv2.getTrackbarPos("Val Max", inpWin)

    scale = cv2.getTrackbarPos("Scale", inpWin) / 10
    if scale < 1: scale =1
    vid_on = cv2.getTrackbarPos("switch", inpWin)
    return (radius,h_max,s_min,s_max,v_min,v_max,scale,vid_on)

def inpTrackbar(win):
    cv2.namedWindow(win)

    cv2.resizeWindow(win, 600,400)

    #0 96 97 250 139 255
    cv2.createTrackbar("radius", win, 30, 179, empty)  # 100
    cv2.createTrackbar("Hue Max", win, 99, 179, empty)  # 100
    cv2.createTrackbar("Sat Min", win, 97, 255, empty)  # 100
    cv2.createTrackbar("Sat Max", win, 255, 255, empty)
    cv2.createTrackbar("Val Min", win, 139, 255, empty)  # 100
    cv2.createTrackbar("Val Max", win, 255, 255, empty)
    
    cv2.createTrackbar("Scale", win, 3, 10, empty)
    # create switch for ON/OFF functionality
    #switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar("switch", win, 0, 1, empty)
    





#Display Group of images in one window
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

def PutTextOnImage(image,txt):
   im= cv2.putText (img = image,
       text = txt,
       org = (5 , 50 ),
       fontFace = cv2.FONT_HERSHEY_DUPLEX,
       fontScale = 1.1,
       color = (255, 226, 25),
       thickness = 2)
   return im

#-------------------------------


def get_limits(color):

    c = np.uint8([[color]])  # here insert the bgr values which you want to convert to hsv
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    print(hsvC)
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
    #print(color, lowerLimit, upperLimit)
    return lowerLimit, upperLimit

