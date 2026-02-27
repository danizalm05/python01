"""
 
 inpTrackbar for edgeDetect.py
"""
import cv2


def empty(a):
    pass

def inpTrackbar(winName):
    cv2.namedWindow(winName)
    cv2.createTrackbar("minVal", winName, 10, 200, empty)   
    cv2.createTrackbar("maxVal", winName, 30, 255, empty)  # 100
    cv2.createTrackbar("scale", winName, 5, 9, empty)
    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, winName, 0, 1, empty)
    


 