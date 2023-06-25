"""
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/draw.py
https://github.com/jasmcaus/opencv-course
20:22   31:38
"""

import getpass
import numpy as np
import cv2 as cv

file_name = 'cat.jpg'


def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+file_name

def rescaleFrame(frame, scale = 0.75):
    width  = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    resiz = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    return resiz

file_path = readImagePath()
print("readImagePath  ", file_path)


blank = np.zeros((500,500,3), dtype='uint8')
# 1. Paint the image a certain colour
blank[200:300, 300:400] = 0,0,255

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=6)

# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,126,255), thickness=-1)

# 4. Draw a line
cv.line(blank, ( 0,250), (300,400), (255,255,255), thickness=3)


# 5. Write text
cv.putText(blank, 'Hello, my name is Jason!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)


cv.imshow("Blank",blank)
img = cv.imread(file_path)
cv.imshow("cat",img)
cv.waitKey(0)