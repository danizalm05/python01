"""
Thresholding/Binarizing Images.py
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/
 02:15:10  02:26:00
https://docs.opencv.org/3.4/db/d8e/tutorial_threshold.html

"""



import getpass
import cv2 as cv
import cvzone

GRAY = (100, 100, 100)
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 3



file_name = '1.jpg'
def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+file_name




max_value = 255
max_type = 4
max_binary_value = 255
trackbar_type = 'Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted'
trackbar_value = 'Value'
window_name = 'Threshold Demo'

file_path = readImagePath()
img0 = cv.imread(file_path)
src_gray = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)



def Threshold(val):
    #0: Binary
    #1: Binary Inverted
    #2: Threshold Truncated
    #3: Threshold to Zero
    #4: Threshold to Zero Inverted
    threshold_type = cv.getTrackbarPos(trackbar_type, window_name)

    threshold_value = cv.getTrackbarPos(trackbar_value, window_name)
    _, dst = cv.threshold(src_gray, threshold_value, max_binary_value, threshold_type )
    adaptive  = cv.adaptiveThreshold(src_gray, 255,
                                   cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 1+2*threshold_value, threshold_type)

    adaptiveGus = cv.adaptiveThreshold(src_gray, 255,
                                    cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 1 + 2 * threshold_value,
                                    threshold_type)

    _, bin = cv.threshold(src_gray, 91, max_binary_value, 0)
    cv.putText(bin, "0:binary ="+ '91' , (10, 40 ), font,2,GRAY, 2)
    cv.putText(img0, 'img0', (10, 40), font, 2, (250,0,0), 2)
    cv.putText(adaptive, 'adaptive', (10, 40), font, 2, GRAY, 2)
    imgList = [img0, src_gray, dst, bin, adaptive,adaptiveGus]
    stackedImg = cvzone.stackImages(imgList, 4, 0.5)
    cv.imshow(window_name, stackedImg)

cv.namedWindow(window_name)

cv.createTrackbar(trackbar_type, window_name , 3, max_type, Threshold)
# Create Trackbar to choose Threshold value
cv.createTrackbar(trackbar_value, window_name , 2, max_value, Threshold)

# Call the function to initialize
dst0 =Threshold(0)


adaptiveg = cv.adaptiveThreshold(src_gray, 255,
                                    cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 3)
cv.imshow('adaptiveg', adaptiveg)
# Wait until user finishes program
cv.waitKey()