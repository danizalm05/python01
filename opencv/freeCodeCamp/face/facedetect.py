"""

https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%233%20-%20Faces/face_detect.py
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

  02:39:00  2:49:00
"""



import getpass
import cv2 as cv
import cvzone
import numpy as np


GRAY = (100, 100, 100)
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 3



file_name = 'g1.jpg'
def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    # /Pictures/22
    #/Pictures/faces
    #C:\Users\gilfm\Pictures\Saved Pictures
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+file_name

trackbar_name = 'scaleFactor'
max_value = 255
max_type = 4
max_binary_value = 255

window_name = 'Faces'


def on_trackbar (val):
    threshold_type = cv.getTrackbarPos(trackbar_name, window_name)




file_path = readImagePath()
print(file_path)
img0 = cv.imread(file_path)
gray = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')
cv.namedWindow(window_name)


cv.createTrackbar(trackbar_name, window_name, 0, 3, on_trackbar)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img0, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img0)

cv.waitKey()