'''
                                 Color Spaces
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=3099 

https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/blurring.py
'''

import cv2 as cv
import sys
import getpass

img='cat.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
path = BASE_FOLDER+img
print("Image  = ",path) 
print("Image  shape  = ",path) 
img = cv.imread(path)
if img is None:
    sys.exit("Could not read the image.")
print("Image  shape  = ",img.shape) 
cv.imshow("Display window", img)

 
cv.waitKey(0)

cv.destroyAllWindows() 

 
