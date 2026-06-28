# -*- coding: utf-8 -*-
"""
  yolo_detect   using camera
 https://github.com/EdjeElectronics/Train-and-Deploy-YOLO-Models/blob/main/yolo_detect.py 


"""
import os
import sys
import time

import cv2
import numpy as np
from ultralytics import YOLO


model_path ='my_model.pt'

min_thresh = float(0.6) #Minimum confidence threshold for displaying detected objects (example: "0.4")' 
user_res = "640x480"
resize = True
resW, resH = int(user_res.split('x')[0]), int(user_res.split('x')[1])

usb_idx = 0
cap = cv2.VideoCapture(usb_idx)
 
cap.set(3, resW)
cap.set(4, resH)
cap.set(10,150)

# Check if model file exists and is valid
if (not os.path.exists(model_path)):
    print('ERROR:  Model was not found.')
    sys.exit(0)
    
    
# Load the model into memory and get labemap
model = YOLO(model_path, task='detect')
labels = model.names    

#source_type = 'usb'


    # Set camera or video resolution if specified by user
if user_res:
        ret = cap.set(3, resW)
        ret = cap.set(4, resH)


# Set bounding box colors (using the Tableu 10 color scheme)
bbox_colors = [(164,120,87), (68,148,228), (93,97,209), (178,182,133), (88,159,106), 
              (96,202,231), (159,124,168), (169,162,241), (98,118,150), (172,176,184)] 

# Initialize control and status variables
avg_frame_rate = 0
frame_rate_buffer = []
fps_avg_len = 200
img_count = 0


# Begin inference loop
while True:
  t_start = time.perf_counter()

  # Load frame from  source
  ret, frame = cap.read()
  if (frame is None) or (not ret):
            print('Unable to read frames from the camera. This indicates the camera is disconnected or not working. Exiting program.')
            break

  
  # Resize frame to desired display resolution
  if resize == True:
       frame = cv2.resize(frame,(resW,resH))

    # Run inference on frame
  results = model(frame, verbose=False)

    # Extract results
  detections = results[0].boxes    
  object_count = 0

    # Go through each detection and get bbox coords, confidence, and class
  for i in range(len(detections)):

        # Get bounding box coordinates
        # Ultralytics returns results in Tensor format, which have to be converted to a regular Python array
        xyxy_tensor = detections[i].xyxy.cpu() # Detections in Tensor format in CPU memory
        xyxy = xyxy_tensor.numpy().squeeze() # Convert tensors to Numpy array
        xmin, ymin, xmax, ymax = xyxy.astype(int) # Extract individual coordinates and convert to int

        # Get bounding box class ID and name
        classidx = int(detections[i].cls.item())
        classname = labels[classidx]

        # Get bounding box confidence
        conf = detections[i].conf.item()

        # Draw box if confidence threshold is high enough
        if conf > min_thresh:

            color = bbox_colors[classidx % 10]
            cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), color, 2)

            label = f'{classname}: {int(conf*100)}%'
            labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1) # Get font size
            label_ymin = max(ymin, labelSize[1] + 10) # Make sure not to draw label too close to top of window
            cv2.rectangle(frame, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), color, cv2.FILLED) # Draw white box to put label text in
            cv2.putText(frame, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1) # Draw label text

            # Basic example: count the number of objects in the image
            object_count = object_count + 1
  cv2.putText(frame, f'FPS: {avg_frame_rate:0.2f}', (10,20), cv2.FONT_HERSHEY_SIMPLEX, .7, (0,255,255), 2) # Draw framerate
    
  # Display detection results
  cv2.putText(frame, f'Number of objects: {object_count}', (10,40), cv2.FONT_HERSHEY_SIMPLEX, .7, (0,255,255), 2) # Draw total number of detected objects
  cv2.imshow('YOLO detection results',frame) # Display image

    # Calculate and draw framerate (if using video, USB, or Picamera source)
  key = cv2.waitKey(1)
    
  if key == ord('q') or key == ord('Q'): # Press 'q' to quit
        break
  elif key == ord('p') or key == ord('P'): # Press 'p' to pause inference
        cv2.waitKey()
  elif key == ord('s') or key == ord('S'): # Press 's' to save a picture of results on this frame
        cv2.imwrite('capture.png',frame) 


   # Calculate FPS for this frame
  t_stop = time.perf_counter()
  frame_rate_calc = float(1/(t_stop - t_start))

    # Append FPS result to frame_rate_buffer (for finding average FPS over multiple frames)
  if len(frame_rate_buffer) >= fps_avg_len:
        temp = frame_rate_buffer.pop(0)
        frame_rate_buffer.append(frame_rate_calc)
  else:
        frame_rate_buffer.append(frame_rate_calc)

    # Calculate average FPS for past frames
  avg_frame_rate = np.mean(frame_rate_buffer)


# Clean up
print(f'Average pipeline FPS: {avg_frame_rate:.2f}')
print('video  camera index  ', usb_idx)
cap.release()

cv2.destroyAllWindows()        