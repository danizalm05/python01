import cv2
import numpy as np
import getpass

#image = np.zeros((250, 250, 3), dtype=np.uint8)
blue = 0
green = 0
red = 0
maxCorner = 1
qualityLevel = 0.01
image_name = 'a1.jpg'


def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    return BASE_FOLDER+image_name

def  goodFeaturesToTrack():
    global qualityLevel, maxCorner, image
    imageCopy = image.copy()

    print(qualityLevel)
    minDistance = 15
    blockSize = 9
    #maxCorner = 20

    gray = cv2.cvtColor(imageCopy, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, maxCorner, qualityLevel, minDistance, blockSize)
    corners = np.int0(corners)

    for i in corners:
       x, y = i.ravel()
       cv2.circle(imageCopy, (x, y), 5, (0, 0, 255), -1)

       #print(x, y, i)
    cv2.imshow("Image", imageCopy)
    imageCopy = image.copy()


def update_qualityLevel(value):
    global qualityLevel, image
    qualityLevel = value /100000
    goodFeaturesToTrack()

def update_maxCorner (value):
     global maxCorner, image
     maxCorner = value
     goodFeaturesToTrack()


def update_blue(value):
    global blue, image

    # set color and image
    blue = value
    color = np.array([blue, green, red], dtype=np.uint8)
    image = np.full(image.shape, fill_value=color, dtype=np.uint8)
    cv2.imshow("Image", image)


def update_green(value):
    global green, image

    # set color and image
    green = value
    color = np.array([blue, green, red], dtype=np.uint8)
    image = np.full(image.shape, fill_value=color, dtype=np.uint8)
    cv2.imshow("Image", image)


def update_red(value):
    global red, image

    # set color and image
    red = value
    color = np.array([blue, green, red], dtype=np.uint8)
    image = np.full(image.shape, fill_value=color, dtype=np.uint8)
    cv2.imshow("Image", image)

cv2.namedWindow("Parmeters")
cv2.createTrackbar("Blue",  "Parmeters", 0,  255, update_blue, )
cv2.createTrackbar("Green", "Parmeters", 0, 255, update_green, )
cv2.createTrackbar("Red", "Parmeters",  0, 255, update_red, )
cv2.createTrackbar("Corners","Parmeters",0,400,update_maxCorner)
cv2.createTrackbar("qualityLevel","Parmeters",0,100,update_qualityLevel)
qualityLevel

image_path = readImagePath()
image = cv2.imread(image_path)
#cv2.namedWindow("Image")


#cv2.resizeWindow("Image",640,240)
cv2.waitKey(0)