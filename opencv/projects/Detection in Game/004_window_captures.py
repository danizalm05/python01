'''
 
https://www.youtube.com/watch?v=KecMlLUuiE4&list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI&index=3
https://github.com/learncodebygaming/opencv_tutorials/blob/master 
https://learncodebygaming.com/blog/grouping-rectangles-into-click-points
https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html
 
'''
import cv2 as cv
import numpy as np
import os
import getpass
from time import time
from windowcapture import WindowCapture 

frameWidth = 640
frameHeight = 480
path = 'C:/Users/' + getpass.getuser() + '/Pictures/opencv/'



# =================     MAIN   ===============
# initialize the WindowCapture class
wincap = WindowCapture('Program Manager')#('Albion Online Client') 

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    cv.imshow('Computer Vision', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')

 