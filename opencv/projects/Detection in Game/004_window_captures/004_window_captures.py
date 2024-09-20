"""
Real-time Object Detection
https://www.youtube.com/watch?v=WymCpVUPWQ4&source_ve_path=Mjg2NjY
https://learncodebygaming.com/blog/fast-window-capture
https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html

"""

import cv2 as cv
import numpy as np
import os
#import getpass
from time import time
#from windowcapture import WindowCapture
from grabb import capture_win_alt,list_window_names
frameWidth = 640
frameHeight = 480
#path = 'C:/Users/' + getpass.getuser() + '/Pictures/opencv/'



# =================     MAIN   ===============
WINDOW_NAME ='Settings'
hwnd = 0x40436   #Number of window handler in Hex. Put 0 to use WINDOW_NAME

list_window_names()# Get the nanes and handlevnubers (grabb.py) 
loop_time = time()

while(True):
    #screenshot = wincap.get_screenshot()       #  windowcapture
    screenshot = capture_win_alt(WINDOW_NAME,hwnd)# grabb.py
    cv.imshow('004-window capture', screenshot)
  
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
print('Done.')

