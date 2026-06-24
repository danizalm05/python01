# -*- coding: utf-8 -*-
"""
  yolo_detect  
 https://github.com/EdjeElectronics/Train-and-Deploy-YOLO-Models/blob/main/yolo_detect.py 


"""


 
'''

yolo = YOLO("my_model.pt")


vid= 'los_angeles.mp4' #    'los_angeles.mp4'   'dog.mp4''afriq0.MP4'
BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Videos/'
#BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
video_name = BASE_FOLDER+vid
print("Image  = ",video_name )
 
videoCap = cv2.VideoCapture(video_name )

'''

import os
import getpass
import sys
import argparse
import glob
import time

import cv2
import numpy as np
from ultralytics import YOLO

img = 'p1.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'

file_name = BASE_FOLDER+img

model_path ='my_model.pt'
img_source =  file_name

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
vid_ext_list = ['.avi','.mov','.mp4','.mkv','.wmv']


if not(os.path.exists(img_source)):
   print(f' Error - {img_source}  - does not exists.')
   sys.exit(0)

if os.path.isdir(img_source):
     source_type = 'folder'
      
elif os.path.isfile(img_source):
     _, ext = os.path.splitext(img_source)     
     if ext in img_ext_list:
          source_type = 'image'
          print(img_source,'  ',source_type) 
     elif ext in vid_ext_list:   
          source_type = 'video'
     else:
         print(f'File extension {ext} is not supported.')
         sys.exit(0)
         