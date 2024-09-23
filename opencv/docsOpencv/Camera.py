"""
Display Image

https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html 
https://docs.opencv.org/4.x/db/deb/tutorial_display_image.html 
"""
import numpy as np
import cv2 as cv
import getpass


vid = '1.mp4'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Videos/Captures/'
path = BASE_FOLDER+vid
print("Image  = ", path)


CameraID = 0

cap1 = cv.VideoCapture(CameraID)
cap2 = cv.VideoCapture(path)

if not cap1.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap1.read()
    ret2, frame2 = cap2.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    if not ret2:
        print("Can't receive video frame (stream end?). ")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame0', frame)
    cv.imshow('frame2', frame2)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap1.release()
cap2.release()
cv.destroyAllWindows()