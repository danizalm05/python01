'''
               Draw line rectangel circle text
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=4933
 

 
'''

import cv2 as cv
import getpass
import numpy as np
from outputCV import stackImages,PutTextOnImage
from edgeDetectInp import   inpTrackbar 


inpWinName = "Input"
inpTrackbar(inpWinName)
img=  '2.jpg'  #'2.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
path = BASE_FOLDER+img
print("Image  = ",path) 
print("Image  shape  = ",path) 




img = cv.imread(path)
assert img is not None, "file could not be read, check with os.path.exists()"


while True:

    scl = cv.getTrackbarPos("scale", inpWinName) / 10
    minVal = cv.getTrackbarPos("minVal", inpWinName)
    maxVal = cv.getTrackbarPos("maxVal", inpWinName)
 

    canny = cv.Canny(img, minVal, maxVal) 
    kernel = np.ones((5, 5), dtype = np.uint8)

#dilate: thickens white regions or objects and fills small holes.
    img_dilation = cv.dilate(canny, kernel, iterations=1)
    img_erode = cv.erode(img_dilation , kernel, iterations=1)
 
    
    source_copy = img.copy()
    PutTextOnImage(source_copy,"Source")
    
    PutTextOnImage(canny,"canny")
    PutTextOnImage( img_dilation,"Dilation")
    PutTextOnImage( img_erode,"Erode")
    imgStack = stackImages(scl,
                          ( [source_copy, canny, img_dilation],
                            [img_erode, img_erode, img_erode]
                          )    )
 
    cv.imshow("ImageStack", imgStack)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows() 
 
 
