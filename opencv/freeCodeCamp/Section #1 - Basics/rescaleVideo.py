"""
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course
18:36
"""
#pylint:disable=no-member
import getpass

import cv2 as cv

file_name = 'dog.mp4'


def readVideoPath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Videos/Captures/'
    path = BASE_FOLDER

    return path+file_name

def rescaleFrame(frame, scale = 0.75):
    width  = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    resiz = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    return resiz


input_video_file = readVideoPath()
cap = cv.VideoCapture(input_video_file)
while True:
    isTrue, frame = cap.read()
    frame_resized = rescaleFrame(frame,0.5)
    cv.imshow('video',frame)
    cv.imshow('video  resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break