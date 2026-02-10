'''
                                 Color Spaces
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=2338
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=2846 

'''

import cv2 as cv
import sys
import getpass

img='cat.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
path = BASE_FOLDER+img
#print("Image  = ",path) 

img = cv.imread(path)
if img is None:
    sys.exit("Could not read the image.")
print("Image  shape  = ",img.shape) 
cv.imshow("Display", img)
 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray) 

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# BGR to   HSV (hue, saturation, value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)



cv.waitKey(0)

cv.destroyAllWindows() 