"""
 
 inpTrackbar for edgeDetect.py
"""
import cv2


def empty(a):
    pass

def inpTrackbar(winName):
    cv2.namedWindow(winName)
    cv2.createTrackbar("x1", winName, 10, 500, empty)   
    cv2.createTrackbar("y1", winName, 10, 500, empty)   
    cv2.createTrackbar("x2", winName, 20, 500, empty)   
    cv2.createTrackbar("y2", winName, 20, 500, empty)   
   
    cv2.createTrackbar("angle", winName, 180, 360, empty) 
    cv2.createTrackbar("startAngle", winName, 0, 360, empty)
  
    cv2.createTrackbar("endAngle", winName, 0, 360, empty) 
    cv2.createTrackbar("scale", winName, 3, 9, empty)
    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, winName, 0, 1, empty)
    


 