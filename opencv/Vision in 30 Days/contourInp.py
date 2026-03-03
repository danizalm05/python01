"""
 
 inpTrackbar for edgeDetect.py
"""
import cv2


def empty(a):
    pass

def inpTrackbar(winName):
    cv2.namedWindow(winName)
    cv2.createTrackbar("trash", winName, 127, 255, empty)   
    cv2.createTrackbar("cnt_area", winName,100,400, empty)   
    cv2.createTrackbar("scale", winName, 3, 9, empty)
    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, winName, 0, 1, empty)
    


 