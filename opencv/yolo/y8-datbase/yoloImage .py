# -*- coding: utf-8 -*-
"""
  yolo_detect   images (not vidoe)
 https://github.com/EdjeElectronics/Train-and-Deploy-YOLO-Models/blob/main/yolo_detect.py 

"""

import os
import getpass
import sys
import glob
import cv2

from ultralytics import YOLO



#                   Load image file
img = 'lambo.PNG' #'p3.jpg'#'lambo.PNG' # 'p1.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
file_name = BASE_FOLDER+img


model_path ='my_model.pt'
img_source =  file_name
min_thresh = float(0.6) #Minimum confidence threshold for displaying detected 
user_res = "640x480"
resize = True
resW, resH = int(user_res.split('x')[0]), int(user_res.split('x')[1])

print(resW, resH )


# Check if model file exists and is valid
if (not os.path.exists(model_path)):
    print('ERROR:  Model was not found.')
    sys.exit(0)
    
    
# Load the model into memory and get labemap
model = YOLO(model_path, task='detect')
labels = model.names    

# Parse input to determine if image source is a file, folder, video, or USB camera
img_ext_list = ['.jpg','.JPG','.jpeg','.JPEG','.png','.PNG','.bmp','.BMP']
 


if not(os.path.exists(img_source)):
   print(f' Error - {img_source}  - does not exists.')
   sys.exit(0)

if os.path.isdir(img_source):
     source_type = 'folder'
     imgs_list = []
     filelist = glob.glob(img_source + '/*')
     for file in filelist:
       _, file_ext = os.path.splitext(file)
       if file_ext in img_ext_list:
           imgs_list.append(file)
           
elif os.path.isfile(img_source):
     _, ext = os.path.splitext(img_source)     
     if ext in img_ext_list:
          source_type = 'image'
   
         
     else:
         print(f'File extension {ext} is not supported.')
         sys.exit(0)

print(img_source,'  ',source_type)          

if source_type == 'image':
    imgs_list = [img_source]
    


# Set bounding box colors (using the Tableu 10 color scheme)
bbox_colors = [(164,120,87), (68,148,228), (93,97,209), (178,182,133), (88,159,106), 
              (96,202,231), (159,124,168), (169,162,241), (98,118,150), (172,176,184)] 

# Initialize control and status variables

img_count = 0

 

while True:
  # Load frame from image source
  if source_type == 'image' or source_type == 'folder':
        #load the image using its filename
        if img_count >= len(imgs_list):
            print('All images have been processed. Exiting program.')
            break
            sys.exit(0)
        img_filename = imgs_list[img_count]
        frame = cv2.imread(img_filename)
        img_count = img_count + 1

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

  # Display detection results
  cv2.putText(frame, f'Number of objects: {object_count}', (10,40), cv2.FONT_HERSHEY_SIMPLEX, .7, (0,255,255), 2) # Draw total number of detected objects
  cv2.imshow('YOLO detection results',frame) # Display image

    
  if  source_type == 'folder':
        key = cv2.waitKey()  
          
  if source_type == 'image':
         key = cv2.waitKey()  
         break    
      
# Clean up

cv2.destroyAllWindows()        