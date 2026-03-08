
import cv2
import numpy as np
import matplotlib.pyplot as plt
import getpass

def empty(a):
    pass

def inpTrackbar(winName):
    cv2.namedWindow(winName)
    cv2.createTrackbar("Blue", winName, 0, 255, empty)  # 100
    cv2.createTrackbar("Green", winName,255, 255, empty)  # 100
    cv2.createTrackbar("Red", winName, 255, 255, empty)  # 100
    cv2.createTrackbar("scale", winName, 3, 9, empty)
    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'

    cv2.createTrackbar(switch, winName, 0, 1, empty)
    cv2.createTrackbar("Contour ID", winName, 0, 100, empty)




 


def get_limits(color):

    c = np.uint8([[color]])  # here insert the bgr values which you want to convert to hsv
 
    
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    print ( color , hsvC)
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
   
    return lowerLimit, upperLimit

