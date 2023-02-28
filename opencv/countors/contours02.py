"""
Contours & Masks using Python & OpenCV -
How to separate object from image background?
https://www.youtube.com/watch?v=JOxebvuRpyo
https://github.com/maksimKorzh/open-cv-tutorials/blob/main/src/contours/contours.py

10:00
"""
import cv2
import numpy as np

import getpass



def empty(a):
    pass
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #
mimg = "tree.jpg"
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
       color = (255, 26, 25),
       thickness = 3)
   return im

cv2.namedWindow("ImageStack")
cv2.namedWindow("Input")

cv2.createTrackbar("thold", "Input", 3, 255, empty)
cv2.createTrackbar("highthold", "Input", 150, 255, empty)
cv2.createTrackbar("scale", "Input", 5,9, empty)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'

cv2.createTrackbar(switch, 'Input',0,1,empty)
cv2.createTrackbar("Contour ID", "Input", 0,100, empty)

original_image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
image_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
gray_inverted = cv2.bitwise_not(image_gray)

inpImage = np.zeros((50,200,3), np.uint8)
inpImage = PutTextOnImage(inpImage,'Coountor2')


image_gray = PutTextOnImage(image_gray,'Gray')
scale = 0.2

while True:
   thold = cv2.getTrackbarPos("thold","Input")
   hthold = cv2.getTrackbarPos("highthold","Input")
   scale = cv2.getTrackbarPos("scale","Input")/10
   on = cv2.getTrackbarPos(switch,"Input")

   ContourID = cv2.getTrackbarPos("Contour ID","Input")
   #print(ContourID)
   thresh, image_edges = cv2.threshold(image_gray, thold,  hthold, cv2.THRESH_BINARY)
   contours_draw, hierachy = cv2.findContours(image_edges , cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

   original_copy = original_image.copy()
   if (on==0):
    cv2.drawContours(original_copy, contours_draw, -1, (250, 0, 0), 3)
   else:
       CID = int((ContourID /100) * len( contours_draw))-1
       print(f'{len( contours_draw)} contour(s) found!',' CID = ',CID)
       cv2.drawContours(original_copy, contours_draw, CID, (0, 0, 255), 3)
   image_gray = PutTextOnImage(image_gray,'Gray')
   image_edges  = PutTextOnImage( image_edges,'threshold')




   imgStack = stackImages(scale, 
        (
         [original_image,image_gray,gray_inverted , gray_inverted],
         [image_edges , original_copy,  original_copy, original_copy]
        )
       
       )

   cv2.imshow("ImageStack",imgStack)

   cv2.imshow("Input",inpImage)



   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
cv2.destroyAllWindows()