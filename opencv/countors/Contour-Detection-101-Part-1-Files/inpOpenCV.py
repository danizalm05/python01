"""
Find Nax Contours & sort -
https://www.youtube.com/watch?v=JfaZNiEbreE&list=PLCeWwpzjQu9gc9C9-iZ9WTFNGhIq4-L1X
https://www.youtube.com/watch?v=JOxebvuRpyo
https://github.com/maksimKorzh/open-cv-tutorials/blob/main/src/contours/contours.py
https://colab.research.google.com/drive/1QeXAHV3-BNaIoidWhSK3MJyVElNv3FLN#scrollTo=qF-0ptmAzxUv

"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import getpass

def empty(a):
    pass

def inpTrackbar(winName):
    cv2.namedWindow(winName)
    cv2.createTrackbar("T_lower", winName, 3, 255, empty)  # 100
    cv2.createTrackbar("T_upper", winName, 150, 255, empty)  # 160
    cv2.createTrackbar("scale", winName, 5, 9, empty)
    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'

    cv2.createTrackbar(switch, winName, 0, 1, empty)
    cv2.createTrackbar("Contour ID", winName, 0, 100, empty)






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
       org = (20 , 50 ),
       fontFace = cv2.FONT_HERSHEY_DUPLEX,
       fontScale = 2.0,
       color = (255, 226, 25),
       thickness = 2)
   return im

#-------------------------------

