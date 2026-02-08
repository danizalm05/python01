'''
Basic operations 
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=1711
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=2155
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter2.py

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

# Resize
resized = cv.resize(img, (700,200))#, interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Cropping [lines , cloumn ]
cropped = img[30:360, 230:630]
cv.imshow('Cropped', cropped)

cv.waitKey(0)

cv.destroyAllWindows() 