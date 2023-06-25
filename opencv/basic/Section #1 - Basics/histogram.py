"""
bitwise.py    masking.py
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/histogram.py
 02:02:10   02:15:10

"""



import getpass
import cv2 as cv
import numpy as np
import cvzone
import matplotlib.pyplot as plt

file_name = '1.jpg'
def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+file_name

def nothing(x):
    pass


cv.namedWindow('image')
cv.createTrackbar('radios', 'image', 150, 550, nothing)
cv.createTrackbar('x', 'image', 150, 500, nothing)
cv.createTrackbar('y', 'image', 150, 500, nothing)

file_path = readImagePath()
img0 = cv.imread(file_path)
gray = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

while (True):

    r = cv.getTrackbarPos('radios', 'image')
    xx = cv.getTrackbarPos('x', 'image')
    yy = cv.getTrackbarPos('y', 'image')


    blank = np.zeros(img0.shape[:2], dtype='uint8')
    mask = cv.circle(blank, (xx + img0.shape[1] // 2, yy + img0.shape[0] // 2), r, 255, -1)
    masked = cv.bitwise_and(img0,img0, mask=mask)
    # GRayscale histogram
    hist_size = [256]
    ranges = [0, 256]
    #gray_hist = cv.calcHist([img0], [0], masked, hist_size, ranges)

    imgList = [gray, mask, masked, masked, masked,  gray]
    stackedImg = cvzone.stackImages(imgList, 3, 0.5)
    cv.imshow("Result", stackedImg)
    #####
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv.calcHist([img0], [i], mask, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    ########
    #plt.plot(gray_hist)
    #plt.xlim([0,256])
    plt.show()

    cv.imshow('image',masked)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

   
    