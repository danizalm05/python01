import cv2
import numpy as np
"""
 document scan: project2

Murtaza's Workshop - Robotics and AI  2:15:00  2:56:20
 https://www.youtube.com/watch?v=WQeoO7MI0Bs&list=PLMoSUbG1Q_r9p7iYBg6z6tZP002DAJ41H
 https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/project2.py
 """

import cv2
import numpy as np

###################################
widthImg =  480
heightImg = 640
#####################################
camera_num = 0
cap = cv2.VideoCapture(camera_num)

cap.set(3, 640)#widthImg)
cap.set(4, 480)#heightImg)

cap.set(10,150)

def empty(a):
    pass
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


def preProcessing (img):

    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #GaussianBlur
    kerX = cv2.getTrackbarPos("kernel X", "HSV")
    kerY = cv2.getTrackbarPos("kernel Y", "HSV")
    bordType = cv2.getTrackbarPos("BorderType", "HSV")

    if kerX <= 0: kerX = 1
    if kerY <= 0: kerX = 1
    if kerX % 2 == 0:
        kerX -= 1
    if kerY % 2 == 0:
        kerY -= 1
    imgBlur = cv2.GaussianBlur(imgGray, (kerX, kerY), bordType)

    # Canny - find edges
    thld1 = cv2.getTrackbarPos("thld1", "HSV")
    thld2 = cv2.getTrackbarPos("thld2", "HSV")
    imgCanny = cv2.Canny(imgBlur, thld1, thld2)  # find edges

    kernel = np.ones((5, 5))
    dilateIter = cv2.getTrackbarPos("dilateIter", "HSV")
    imgDial = cv2.dilate(imgCanny, kernel, iterations=dilateIter)

    thresIter = cv2.getTrackbarPos("thresIter", "HSV")
    imgThres = cv2.erode(imgDial, kernel, iterations= thresIter)

    print("kerX = ", kerX, "kerY = ", kerY, "bordType = ", bordType)
    print("thld1 =", thld1, "thld2 =", thld2)
    print("dilateIter =", dilateIter, " thresIter", thresIter)

    scale = 0.6
    img_array = ([img, imgGray, imgBlur], [imgCanny , imgDial , imgThres])
    imgStack = stackImages(scale, img_array)
    cv2.imshow("ImageStack", imgStack)


    return   imgThres


def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    i = 0
    for cnt in contours:
        i += 1
        area = cv2.contourArea(cnt)
        area_limit = cv2.getTrackbarPos("AreaLimit", "HSV")
        print("AreaLimit =", area_limit)
        if area >  area_limit:#5000:
            #cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 1)
            peri = cv2.arcLength(cnt, True)  # closed shapes ==> True
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)  # closed shapes ==> True
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)#print only  the biggest
    return biggest

title = "Contour"
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,340)
cv2.createTrackbar("kernel X", "HSV", 3, 50, empty)
cv2.createTrackbar("kernel Y", "HSV", 3, 50, empty)
cv2.createTrackbar("BorderType", "HSV", 16, 50, empty)

cv2.createTrackbar("thld1","HSV",65,200,empty)
cv2.createTrackbar("thld2","HSV",65,200,empty)

cv2.createTrackbar("dilateIter","HSV",2,8,empty)
cv2.createTrackbar("thresIter","HSV",1,10,empty)

cv2.createTrackbar("AreaLimit","HSV",100,7000,empty)

def reorder (myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    #print("add", add)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1]= myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    #print("NewPoints",myPointsNew)
    return myPointsNew



def getWarp(img,biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    imgCropped = imgOutput[20:imgOutput.shape[0] - 20, 20:imgOutput.shape[1] - 20]
    imgCropped = cv2.resize(imgCropped, (widthImg, heightImg))

    return imgOutput
    #return imgCropped





while True:
    _, img = cap.read()

    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getContours(imgThres)
    if biggest.size != 0:
        imgWarped = getWarp(img, biggest)
        # imageArray = ([img,imgThres],
        #           [imgContour,imgWarped])
        imageArray = ([imgContour, imgWarped])
        cv2.imshow("ImageWarped", imgWarped)
    else:
        # imageArray = ([img, imgThres],
        #               [img, img])
        imageArray = ([imgContour, img])

    #cv2.imshow("Result", imgWarped)
    #cv2.imshow('imgBlur', imgThres)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()