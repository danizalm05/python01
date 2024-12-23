"""
Object Tracking with Opencv and Python
https://www.youtube.com/watch?v=O3b8lVF93jU

next course:
    https://www.youtube.com/watch?v=GgGro5IV-cs
    https://pysource.com/2021/10/05/object-tracking-from-scratch-opencv-and-python/

python 3.10
conda install numpy
"""
import cv2
from tracker import *
import getpass

BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Videos/Captures/'
# "modrain.jpg"#"grains.jpg" #
vid = "1.mp4"
path = BASE_FOLDER + vid
#print(path)
frameWidth = 640
frameHeight = 480
# Create tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture(path)#("highway.mp4")

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2 \
                              (history=100, varThreshold=40)

while True:
    ret, frame = cap.read()
    if (not ret):
         print("End of video")
         break
    height, width, _ = frame.shape
    # Extract Region of interest
    roi = frame[340: 720,500: 800]

    # 1. Object Detection
    mask = object_detector.apply(roi) 
    
    #Ignore the shdows ,consider only colors above 254
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []#all the cars currently on screen
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
          #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
          x, y, w, h = cv2.boundingRect(cnt)
          detections.append([x, y, w, h])
          #print(detections)
          #cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
 
    # 2. Object Tracking
    boxes_ids = tracker.update(detections)
    #print(boxes_ids)#[[ x,y,width,hight,ID]]
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)


    cv2.imshow("roi", roi)
    cv2.imshow("Mask", mask)
    img = cv2.resize(frame, (frameWidth, frameHeight))
    cv2.imshow("Frame", img)
    
   
    key = cv2.waitKey(10)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()