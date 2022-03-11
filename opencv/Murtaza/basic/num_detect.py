
"""
 Locating car licence plate: project3

Murtaza's Workshop - Robotics and AI   2:56:20 3:00:00
 https://www.youtube.com/watch?v=WQeoO7MI0Bs&list=PLMoSUbG1Q_r9p7iYBg6z6tZP002DAJ41H
 https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/project3.py
 """
import cv2
import numpy as np

image_source = "image"
#image_source = "camera"

################################
frameWidth = 640
frameHeight = 480
####################################################

if image_source == "image":

   mimg = "p1.JPG"
   path = BASE_FOLDER +  mimg
   img = cv2.imread(path)
   print(path)
   cv2.imshow("imgimg", path)

if image_source == "camera":
   cap = cv2.VideoCapture(0)
   cap.set(3, frameWidth)
   cap.set(4, frameHeight)
   cap.set(10, 150)


while True:
    if image_source == "camera":
             success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1,10)
    #numberPlates is a list of 4 integers (x, y, w, h) of the ractengle
    for (x, y, w, h) in numberPlates:
        area = w * h

        if area > minArea:

           cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
           cv2.putText(img, "Number Plate", (x, y - 5),
                       cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
           imgRoi = img[y:y + h, x:x + w]
           cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        file_path = BASE_FOLDER + str(count) + ".jpg"
        print ( file_path)
        cv2.imwrite( file_path, imgRoi)
        #Save message
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1



