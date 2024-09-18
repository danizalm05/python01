import cv2 as cv
import numpy as np
import os
from time import time

from vision import Vision
import sys
from windowcapture import WindowCapture
from grabb import capture_win_alt,list_window_names


os.chdir(os.path.dirname(os.path.abspath(__file__)))

#
# initialize the WindowCapture class
WindowCapture.list_window_names()
# sys.exit()
win_name = 'Program Manager'  # 'Windows Media Player'
wincap = WindowCapture(win_name)
# initialize the Vision class
vision_limestone = Vision('albion_limestone.jpg')

'''
# https://www.crazygames.com/game/guns-and-bottle
wincap = WindowCapture()
vision_gunsnbottle = Vision('gunsnbottle.jpg')
'''
# =================     MAIN   ===============
WINDOW_NAME = 'Settings'
hwnd = 0x3047c #0x1012  # Number of window handler in Hex. Put 0 to use WINDOW_NAME

loop_time = time()

while (True):

    # get an updated image of the game
    # screenshot = wincap.get_screenshot()
    screenshot = capture_win_alt(WINDOW_NAME, hwnd)# grabb.py
    # display the processed image
    points = vision_limestone.find(screenshot, 0.5, 'rectangles')
    # points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
