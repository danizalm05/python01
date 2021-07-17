import cv2
import numpy as np
import getpass

frontalface ="D:/a/python/openCV with python by example/Chapter04/haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(frontalface)

if face_cascade.empty():
	raise IOError('Unable to load the face cascade classifier xml file')


img_name = "PianoChords.mp4"
BASE_FOLDER = 'C:/Users/' + getpass.getuser() +'/Videos/Captures/'
path = BASE_FOLDER + img_name
print(path)

cap = cv2.VideoCapture(path)
#cap = cv2.VideoCapture(0)# use  video   camera
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


scaling_factor = 0.5

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor,
                             fy=scaling_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    scaling_factor = 1.3 #next size to check will be, 1.3 times bigger than the current size.
    threshold =5 #   number of adjacent rectangles needed to keep  the current rectangle
    face_rects = face_cascade.detectMultiScale(gray, scaling_factor, threshold)

    for (x,y,w,h) in face_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255, 0), 5)

    cv2.imshow('Face Detector', frame)

    c = cv2.waitKey(1)
    if c == 27: # esc
        break

cap.release()
cv2.destroyAllWindows()
