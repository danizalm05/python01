"""
Drawing Convex Hull
https://colab.research.google.com/drive/1QeXAHV3-BNaIoidWhSK3MJyVElNv3FLN#scrollTo=SogGawKwXJR1
https://www.youtube.com/watch?v=JfaZNiEbreE&list=PLCeWwpzjQu9gc9C9-iZ9WTFNGhIq4-L1X
https://www.youtube.com/watch?v=JOxebvuRpyo

Drawing Convex Hull

Convex Hull a way to draw the contour onto the image.
 The function cv2.convexHull() checks a curve for convexity defects and
 corrects it.
 Convex curves  = curves which are bulged out.
 Concave curves = curves which are bulged inside


Function Syntax:

    hull = cv2.convexHull(points, hull, clockwise, returnPoints)

Parameters:
 points - Input 2D point set. This is a single contour.
 clockwise - Orientation flag. If it is true, the output convex hull is
 oriented clockwise. Otherwise, it is oriented counter-clockwise.
 The assumed coordinate system has its X axis pointing to the right,
 and its Y axis pointing upwards.
 returnPoints - Operation flag. In case of a matrix, when the flag is true,
  the function returns convex hull points. Otherwise, it returns indices of
  the convex hull points.
  By default it is True.

Returns:
 hull - Output convex hull.
 It is either an integer vector of indices or vector of points.
  In the first case, the hull elements are 0-based indices of the
  convex hull points in the original array
  (since the set of convex hull points is a subset of the original point set).
   In the second case,
 hull elements are the convex hull points themselves.
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
import getpass

def empty(a):
    pass
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #
mimg = "1.jpg" #"basketball.jpg"  "tree.jpg"#  "image.png"
path = BASE_FOLDER + mimg

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def PutTextOnImage(image,txt):
   im= cv2.putText (img = image,
       text = txt,
       org = (20 , 50 ),
       fontFace = cv2.FONT_HERSHEY_DUPLEX,
       fontScale = 2.0,
       color = (255, 226, 25),
       thickness = 2)
   return im


original_image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

cv2.namedWindow("ImageStack")
cv2.namedWindow("Input")


# Display the result
cv2.createTrackbar("T_lower", "Input", 3, 255, empty)#100
cv2.createTrackbar("T_upper", "Input", 150, 255, empty)#160
cv2.createTrackbar("scale", "Input", 5,9, empty)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'

cv2.createTrackbar(switch, 'Input',0,1,empty)
cv2.createTrackbar("Contour ID", "Input", 0,100, empty)


################## Main ####################

hull_img = original_image.copy()
contour_img = original_image.copy()
gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)
scale = 0.2
# Find the contours from the thresholded image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Since the image only has one contour, grab the first contour
cnt = contours[0]

# Get the required hull
hull = cv2.convexHull(cnt)

# draw the hull
cv2.drawContours(hull_img, [hull], 0 , (0,0,220), 3)


cv2.drawContours(contour_img, [cnt], 0, (0,0,220), 3)
hull_img = PutTextOnImage(hull_img,'hull_img')
contour_img = PutTextOnImage(contour_img,'contour_img')
image0_copy = PutTextOnImage(original_image,'Max contour')
gray = PutTextOnImage(gray,'Gray')
while True:
    scale = cv2.getTrackbarPos("scale","Input")/10
    #Store 4 images on 4X4  grid
    imgStack = stackImages( scale,
         (
            [image0_copy,gray],
            [hull_img,contour_img]
         )
                            )
    #Show the  grid
    cv2.imshow("ImageStack",imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
cv2.destroyAllWindows()