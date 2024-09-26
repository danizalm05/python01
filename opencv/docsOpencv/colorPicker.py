'''
https://www.selecolor.com/en/hsv-color-picker/

'''


import cv2
import numpy as np
import getpass
from inpOpenCV import stackImages,PutTextOnImage, inpTrackbar
#image_source = "image"
image_source = "camera"
frameWidth = 640
frameHeight = 480
camera_num = 0



if image_source == "image":
    BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
    BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
    path = BASE_FOLDER +  '1.jpg'  # 'cards.jpg'
    img = cv2.imread(path)

if image_source == "camera":
   camera_num = 0
   cap = cv2.VideoCapture(0)
   cap.set(3, frameWidth)
   cap.set(4, frameHeight)
   cap.set(10, 150)

def empty(a):
    pass
inpWinName = "Input"
inpTrackbar(inpWinName)
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




cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",45,255,empty)
cv2.createTrackbar("HUE Max","HSV",45,255,empty)
cv2.createTrackbar("SAT Min","HSV",100,255,empty)
cv2.createTrackbar("SAT Max","HSV",100,255,empty)
cv2.createTrackbar("VALUE Min","HSV",90,255,empty)
cv2.createTrackbar("VALUE Max","HSV",90,255,empty)


colRect = np.ones((212, 212, 3), np.uint8) 
cv2.rectangle(colRect, (1,1), (212, 212), (0, 255, 0), -1)
while True:

    _, img = cap.read()
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min","HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv,lower,upper)
    result = cv2.bitwise_and(img,img, mask = mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    #hStack = np.hstack([img,mask])
    print("HUE Min = ", h_min, "HUE Max  =", h_max)
    print("SAT Min =" ,  s_min ,"SAT Max = ",  s_max)
    print( "VALUE Min",  v_min, "VALUE Max",   v_max)
    
    hue =(h_min + h_max)/2
    sat =(s_min +s_max)/2
    val =(v_min + v_max)/2
    
    print(hue,sat,val)
    cv2.rectangle(colRect, (1,1), (212, 212),(hue,sat,val), -1)

    scale = 0.4
    img_array = ([img,mask], [result , colRect])
    imgStack = stackImages(scale, img_array)
   
    cv2.imshow('Horizontal Stacking', imgStack)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



  
    
  
 
 
  