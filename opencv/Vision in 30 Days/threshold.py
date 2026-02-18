'''
                                Threshold
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=4017
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=4933

https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/thresh.py

https://docs.opencv.org/4.x/
https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

'''

import cv2 as cv
import getpass
 

img=  'sudoku.png'  #'2.jpg'
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
 
# Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
 

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 80, 255, cv.THRESH_BINARY )

# Addaptive  Thresholding 
th3 = cv.adaptiveThreshold(gray, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,29,30)
 
scl = .7
cv.imshow("Source", rescaleFrame(img,  scale = scl))
cv.imshow(" gray" , rescaleFrame(gray,  scale = scl) )
cv.imshow(" global thresh" , rescaleFrame(thresh,  scale = scl) )
cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", rescaleFrame(th3,  scale = scl ))
 

cv.waitKey(0)
cv.destroyAllWindows() 
 
 
