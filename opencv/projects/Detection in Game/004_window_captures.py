"""
Real-time Object Detection
https://www.youtube.com/watch?v=WymCpVUPWQ4&source_ve_path=Mjg2NjY
https://learncodebygaming.com/blog/fast-window-capture
https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html



"""

import cv2 as cv
import numpy as np
import os
import getpass
from time import time
#from windowcapture import WindowCapture
from grabb import capture_win_alt
frameWidth = 640
frameHeight = 480
path = 'C:/Users/' + getpass.getuser() + '/Pictures/opencv/'



# =================     MAIN   ===============
# initialize the WindowCapture class
#'Albion Online Client' 'Program Manager' 'objectTracking' 'Mozilla Firefox'
#Spyder (Python 3.9) 'Windows Media Player'
#wincap = WindowCapture('Program Manager')
loop_time = time()

WINDOW_NAME ='Settings'

hwnd = 0
while(True):

    # get an updated image of the game
    #screenshot = wincap.get_screenshot()       #  windowcapture
    screenshot = capture_win_alt(WINDOW_NAME,hwnd)#grabb.py
    cv.imshow('Computer Vision', screenshot)

    # debug the loop rate
    if (not (time() == loop_time)):
        print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')

