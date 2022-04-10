
"""
 Locating car licence plate: project3

Murtaza's Workshop - Robotics and AI   2:56:20 3:00:00
 https://www.youtube.com/watch?v=WQeoO7MI0Bs&list=PLMoSUbG1Q_r9p7iYBg6z6tZP002DAJ41H
 https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/project3.py
 """
import cv2
import numpy as np
import getpass
image_source = "image"
##image_source = "video"
#image_source = "camera"
minArea = 200
color = (255,0,255)
count =0
xml_file = "./Resources/haarcascade_russian_plate_number.xml"
plateNnumberCascade = cv2.CascadeClassifier(xml_file)


################################
frameWidth = 640
frameHeight = 480
####################################################



if image_source == "camera":
   cap = cv2.VideoCapture(0)
   cap.set(3, frameWidth)
   cap.set(4, frameHeight)
   cap.set(10, 150)

if image_source == "video":
   mimg = "cars.mp4"
   BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Videos/Captures/'
   path = BASE_FOLDER + mimg
   cap = cv2.VideoCapture(path)
   cap.set(3, frameWidth)
   cap.set(4, frameHeight)
   cap.set(10, 150)

if image_source == "image":
   mimg = "p2.JPG"
   BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
   path = BASE_FOLDER + mimg
   print(path)
   img = cv2.imread(path)
   cv2.imshow("imgimg",img)



while True:
    if image_source == "camera":
             success, img = cap.read()

    if image_source == "video":
             success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateNnumberCascade.detectMultiScale(imgGray, 1.1,10)
    #numberPlates is a list of 4 integers (x, y, w, h) of the ractengle
    for (x, y, w, h) in numberPlates:
        area = w * h

        if area > minArea:

           cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
           cv2.putText(img, "Number Plate", (x, y - 5),
                       cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
           imgRoi = img[y:y + h, x:x + w]
           cv2.imshow("ROI", imgRoi)#Image of the plate

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        file_path = BASE_FOLDER + str(count) + ".jpg"
        #print ( file_path)
        cv2.imwrite( file_path, imgRoi)
        #Save message
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1



