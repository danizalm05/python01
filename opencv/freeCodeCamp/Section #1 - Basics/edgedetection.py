"""
gradients and  edge detections
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/gradients.py

  02:26:00 02:35:00
"""



import getpass
import cv2 as cv
import cvzone
import numpy as np


GRAY = (100, 100, 100)
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 3



file_name = 'p3.jpg'
def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    #
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path




max_value = 255
max_type = 4
max_binary_value = 255
trackbar_type = 'Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted'
trackbar_value = 'Value'
window_name = 'Threshold Demo'

file_path = readImagePath()+file_name
img0 = cv.imread(file_path)
gray = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)



def Threshold(val):

    threshold_type = cv.getTrackbarPos(trackbar_type, window_name)

    threshold_value = cv.getTrackbarPos(trackbar_value, window_name)
    _, dst = cv.threshold(gray, threshold_value, max_binary_value, threshold_type )
    adaptive  = cv.adaptiveThreshold(gray, 255,
                                   cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 1+2*threshold_value, threshold_type)

    adaptiveGus = cv.adaptiveThreshold(gray, 255,
                                    cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 1 + 2 * threshold_value,
                                    threshold_type)



    lap = cv.Laplacian(gray, cv.CV_64F)
    lap = np.uint8(np.absolute(lap))
    cv.putText(lap, "laplaciatn  "  , (10, 40 ), font,2,(250,250,250), 2)

    cv.putText(img0, 'img0', (10, 40), font, 2, (250,0,0), 2)
    cv.putText(adaptive, 'adaptive', (10, 40), font, 2, GRAY, 2)

    canny = cv.Canny(gray, 150, threshold_value)
    cv.putText(canny, 'Canny', (10, 40), font, 2, (250,250,250), 2)

    imgList = [img0, gray, lap,canny, adaptive,adaptiveGus]
    stackedImg = cvzone.stackImages(imgList, 3, 0.5)
    cv.imshow(window_name, stackedImg)

cv.namedWindow(window_name)

cv.createTrackbar(trackbar_type, window_name , 3, max_type, Threshold)
cv.createTrackbar(trackbar_value, window_name , 2, max_value, Threshold)

# Call the function to initialize
#dst0 =Threshold(0)
# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.putText(combined_sobel, "combined_sobel  ", (10, 40), font, 2, (250, 250, 250), 2)
cv.imshow("combined_sobel", combined_sobel)


# Wait until user finishes program
cv.waitKey()