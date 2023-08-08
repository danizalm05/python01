"""
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/read.py
https://www.youtube.com/watch?v=oXlwWbU8l2o
 5:03
"""
#pylint:disable=no-member
import getpass

import cv2 as cv

image_name = 'a1.jpg'
video_name = 'dog.mp4'

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
img = cv.imread(image_path)
cv.imshow('bird', img)
cv.waitKey(0)


# Reading Video  file
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
cv.destroyAllWindows()