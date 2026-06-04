'''
   yolo 8 frame by frame
https://github.com/DAVIDNYARKO123/yolov8-silva/blob/main/yolov8_n_opencv.py
https://youtu.be/hg4oVgNq7Do?t=728


 

 

'b'   98    backward 1 frame
'd'  100    backward 'frame_jump' frames
'f'  102    forward 1 frame
's'  115    save
'u'  117    forward 'frame_jump' frames
'''





import sys
import getpass
 
 

import random
import cv2
import numpy as np
from ultralytics import YOLO

vid= 'afriq1.MP4' #    'los_angeles.mp4'   'dog.mp4''afriq0.MP4'
BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Videos/'
#BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
video_name = BASE_FOLDER+vid
#print("Image  = ",video_name ) 

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
totalframecount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_jump = 100
frame_no = 1
frame_name = 'frame_%d.jpg'
while True:
    # Capture frame-by-frame
    cap.set(1, frame_no )
    ret, frame = cap.read()
    
    if not ret:
       print("Can't receive frame (stream end?). Exiting ...")
       break
    # Predict on image
    detect_params = model.predict(source=[frame], conf=0.45, save=False)

    # Convert tensor array to numpy
    DP = detect_params[0].numpy()
    #print(DP)
    
    if len(DP) != 0:
        for i in range(len(detect_params[0])):
            #print(i)

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
    c =  cv2.waitKey(20)
    if c & 0xFF == ord('q'):
          break
    elif c == 115:# 's' save
       name = BASE_FOLDER+(frame_name) % frame_no
       print("Save image to  " + name)
       #cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)
       # save frame as JPEG file
       frame01 = cv2.resize(frame, None, fx=2,
                          fy=2, interpolation=cv2.INTER_AREA)
       cv2.imwrite(name+(frame_name) % frame_no, frame01)

        

    elif c==117: #  ('u')  move up
       frame_no += frame_jump
       if frame_no > totalframecount : frame_no =0
       print("Move to frame number[{:d}]".format(frame_no))
    elif c==102:#   'f'   forward 1 frame
       frame_no += 1
       if frame_no > totalframecount : frame_no =0
       print("Move to frame number[{:d}]".format(frame_no)) 
    elif c==98:#   'b''   backward 1 frame
       frame_no -= 1
       if frame_no < 0 : frame_no = totalframecount -1
       print("Move to frame number[{:d}]".format(frame_no))
    elif c==100: #  ('d')  move down
       frame_no -= frame_jump
       if frame_no < 0 : frame_no =  totalframecount -1
       print("Move to frame number[{:d}]".format(frame_no))

cap.release() 

cv2.destroyAllWindows()  