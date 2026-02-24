'''
                 edge detection (canny, dilate, erode )
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=4933
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=5493

https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/thresh.py

https://docs.opencv.org/4.x/
https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
'''

import cv2 as cv
import getpass
import numpy as np

img=  '2.jpg'  #'2.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
path = BASE_FOLDER+img
print("Image  = ",path) 
print("Image  shape  = ",path) 

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 


img = cv.imread(path)
assert img is not None, "file could not be read, check with os.path.exists()"

canny = cv.Canny(img, 150, 175) 

kernel = np.ones((5, 5), dtype = np.uint8)

#dilate: thickens white regions or objects and fills small holes.
img_dilation = cv.dilate(canny, kernel, iterations=1)
img_erode = cv.erode(img_dilation , kernel, iterations=1)
 
#canny2 = cv.Canny(img, 100, 200)  
#canny3 = cv.Canny(img, 50, 300)  
scl = .7
cv.imshow("Source", rescaleFrame(img,  scale = scl))
cv.imshow('Canny',  rescaleFrame(canny,  scale = scl))  

cv.imshow('img_dilation',  rescaleFrame(img_dilation,  scale = scl))
cv.imshow('img_erode',  rescaleFrame(img_erode,  scale = scl))

#cv.imshow('Canny2',  rescaleFrame(canny2,  scale = scl))  
#cv.imshow('Canny3',  rescaleFrame(canny3,  scale = scl))

cv.waitKey(0)
cv.destroyAllWindows() 
 
 
