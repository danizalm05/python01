'''
Examples of cv,goodFeaturesToTrack

'''

import getpass
import cv2 as cv
import numpy as np


image_name = 'a1.jpg'
video_name = 'dog.mp4'





def goodFeatures(value):
    print(value)

cv.namedWindow("Parmeters")
cv.resizeWindow("Parmeters",640,240)
cv.createTrackbar("maxCorner","Parmeters",0,400,goodFeatures)



def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    return BASE_FOLDER+image_name

def readVideoPath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Videos/Captures/'
    return BASE_FOLDER + video_name


# Read in an image
image_path = readImagePath()
print("readImagePath  ", image_path)
img00 = cv.imread(image_path)
img01 = img00

qualityLevel = 0.001
minDistance = 15
blockSize = 9
maxCorner =20

gray = cv.cvtColor(img00, cv.COLOR_BGR2GRAY)
# Find the top  corners using the cv2.goodFeaturesToTrack()
corners = cv.goodFeaturesToTrack(gray, maxCorner, qualityLevel, minDistance, blockSize)
corners = np.int0(corners)
for i in corners:
          x, y = i.ravel()
          cv.circle(img01, (x, y), 5, (0, 0, 255), -1)


          print( x, y,i)

cv.namedWindow("img", cv.WINDOW_NORMAL)

# Using resizeWindow()
cv.resizeWindow("img", 900, 750)

# Displaying the image
cv.imshow("img", img01)

cv.waitKey(0)

'''
# Reading Videos
video_path = readVideoPath()
print(video_path)
capture = cv.VideoCapture(video_path)



while True:
    isTrue, frame = capture.read()

    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could
    # not be read, or we're at the end of the video), we immediately
    # break from the loop.
    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
'''
cv.destroyAllWindows()