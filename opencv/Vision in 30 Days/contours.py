'''
                  contours 
 https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=6319
 
'''

import cv2 as cv
import numpy as np
from outputCV import stackImages,PutTextOnImage
from drawInp import   inpTrackbar 


inpWinName = "Input"
inpTrackbar(inpWinName)


# creating array using np.zeroes()
array = np.zeros([500, 500, 3],
                 dtype = np.uint8)

# setting RGB color values as 255,255,255
array[:, :] = [255, 255, 255] 

# displaying the image
cv.imshow("image", array)

#img =array.copy()

while True:

    scl = cv.getTrackbarPos("scale", inpWinName) / 10
    x1 = cv.getTrackbarPos("x1", inpWinName)
    y1 = cv.getTrackbarPos("y1", inpWinName)
    x2 = cv.getTrackbarPos("x2", inpWinName)
    y2 = cv.getTrackbarPos("y2", inpWinName)
    angle = cv.getTrackbarPos("angle", inpWinName)
    startAngle = cv.getTrackbarPos("startAngle", inpWinName)
    endAngle = cv.getTrackbarPos("endAngle", inpWinName)
    imglin =array.copy()
    imglin = cv.line( imglin, (x1, y1), (x2, y2), (255, 0, 0), 3)
    
    title = "line("+ str(x1)+',' + str(y1)+"),(" +str(x2)+',' + str(y2)+"))"
    PutTextOnImage(imglin,  title)
    
    
    imgrec =array.copy()  
    cv.rectangle(imgrec, (x1,y1), (x2, y2), (255, 0, 0), -1)
    
    title = "rectangle("+ str(x1)+',' + str(y1)+"),(" +str(x2)+',' + str(y2)+"))"
    PutTextOnImage(imgrec,  title)

    imgcirc =array.copy()  
    cv.circle(imgcirc,((x1,y1)), x2, (0,0,255), -1)
    title = "circle("+ str(x1)+',' + str(y1)+")," +str(x2)+")"
    PutTextOnImage(imgcirc,  title)
    '''
   Drawing Ellipse
cv2.ellipse(image, center, axes, angle, startAngle, endAngle, color, thickness)
To draw the ellipse, we need to pass several arguments.
x1,y1   center location (x,y). 
x2,y2  axes lengths (semi-major axis length, semi-minor axis length).
 angle is the angle of rotation of ellipse in anti-clockwise direction. 
 startAngle and endAngle denotes the starting and ending of ellipse arc measured in 
 clockwise direction from major axis. i.e. giving values 0 and 360 gives the full ellipse. For more details, check the documentation of cv.ellipse(). Below example draws a half ellipse at the center of the image.
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

    
'''  
    imgcelli =array.copy() 
    cv.ellipse(imgcelli,(x1,y1),(x2,y2),startAngle,endAngle,angle,(255,0,0),-1) 
   

 # Polygon corner points coordinates
    pts = np.array([[x1, y1], [x2, y2], 
                [110, 200], [200, 160], 
                [200, 70], [110, 20]],
               np.int32)
    pts = pts.reshape((-1, 1, 2))
    color = (255, 0, 0)

# Line thickness of 2 px
    thickness = 2
    isClosed = True
    imagPoly  =array.copy() 
    imagPoly = cv.polylines(imagPoly, [pts], 
                      isClosed, color, thickness)

   
    imgStack = stackImages(scl,
           ( [imglin, imgrec,imgcirc], [imgcelli, imagPoly, imglin]   )    )
 

    cv.imshow("ImageStack", imgStack)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows() 
 
 
