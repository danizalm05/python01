'''
https://github.com/DAVIDNYARKO123/yolov8-silva/blob/main/yolov8_n_opencv.py
https://youtu.be/hg4oVgNq7Do?t=728


Results saved to D:\python02\opencv\yolo\object_id\runs\detect\predict-......
'''


import sys
import getpass
 
 

import random
import cv2
import numpy as np
from ultralytics import YOLO

vid= 'afriq1.MP4' # 'los_angeles.mp4'   'dog.mp4''afriq0.MP4'
BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Videos/'
#BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
video_name = BASE_FOLDER+vid
print("Image  = ",video_name ) 

# opening the file in read mode
# A list of objects
my_file = open("utils/coco.txt", "r")
# reading the file
data = my_file.read()
# replacing end splitting the text | when newline ('\n') is seen.
class_list = data.split("\n")
my_file.close()

#print("\n\n Class list\n============\n",class_list) 

# Generate random colors for class list
detection_colors = []
for i in range(len(class_list)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    detection_colors.append((b, g, r))

# load a pretrained YOLOv8n model.This file is not found it 
# will be downloaded from: 
# https://github.com/ultralytics/assets/releases/download
model = YOLO("weights/yolov8n.pt", "v8")

# Vals to resize video frames | small frame optimise the run
frame_wid = 640
frame_hyt = 480

# cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(video_name )

if not cap.isOpened():
    print("Cannot open video")
    exit()
#https://youtu.be/hg4oVgNq7Do?t=996
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
       print("Can't receive frame (stream end?). Exiting ...")
       break
    # Predict on image
    detect_params = model.predict(source=[frame], conf=0.45, save=False)

    # Convert tensor array to numpy
    DP = detect_params[0].numpy()
    print(DP)
    
    if len(DP) != 0:
        for i in range(len(detect_params[0])):
            print(i)

            boxes = detect_params[0].boxes
            box = boxes[i]  # returns one box
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]

            cv2.rectangle(
                frame,
                (int(bb[0]), int(bb[1])),
                (int(bb[2]), int(bb[3])),
                detection_colors[int(clsID)],
                3,
            )

            # Display class name and confidence
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(
                frame,
                class_list[int(clsID)] + " " + str(round(conf, 3)) + "%",
                (int(bb[0]), int(bb[1]) - 10),
                font,
                1,
                (255, 255, 255),
                2,
            )

    # Display the resulting frame
    cv2.imshow("ObjectDetection", frame)

    # Terminate run when "Q" pressed
    if cv2.waitKey(20) & 0xFF == ord('q'):
          break
cap.release() 

cv2.destroyAllWindows()  