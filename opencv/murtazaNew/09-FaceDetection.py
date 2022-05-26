'''
09-FaceDetection.py
Load Inmages in one window
https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=549s   1:42:00
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter9.py
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%231%20-%20Basics/contours.py
'''

import getpass
import cv2

xml_file = "./Resources/haarcascade_frontalface_default.xml"
print(xml_file)
faceCascade = cv2.CascadeClassifier(xml_file)


BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'# faces/'

path = BASE_FOLDER +  'road.jpg' #'test3.jpg'  # 'bb.jpg' 'b1.jpg'
print(path)

img00 = cv2.imread(path)



imgGray = cv2.cvtColor(img00, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
print(faces)
for (x,y,w,h) in faces:
    cv2.rectangle(img00, (x, y), (x+w, y+h), (255, 0, 0), 2)


cv2.imshow("Result", img00)
cv2.waitKey(0)

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break