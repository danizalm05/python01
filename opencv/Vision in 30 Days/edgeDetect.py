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
from outputCV import stackImages,PutTextOnImage
from inpCV import   inpTrackbar 


inpWinName = "Input"
inpTrackbar(inpWinName)
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


while True:
    #scl = .4
    scl = cv.getTrackbarPos("scale", inpWinName) / 10
    minVal = cv.getTrackbarPos("minVal", inpWinName)
    maxVal = cv.getTrackbarPos("maxVal", inpWinName)
    #minVal = 150
    #maxVal = 175

    canny = cv.Canny(img, minVal, maxVal) 
    kernel = np.ones((5, 5), dtype = np.uint8)

#dilate: thickens white regions or objects and fills small holes.
    img_dilation = cv.dilate(canny, kernel, iterations=1)
    img_erode = cv.erode(img_dilation , kernel, iterations=1)
 
    

    PutTextOnImage(img,"Source")
    PutTextOnImage(canny,"canny")
    imgStack = stackImages(scl,
                          ( [img, canny, img_dilation],
                            [img_erode, img_erode, img_erode]
                          )    )
 
    cv.imshow("ImageStack", imgStack)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows() 
 
 
