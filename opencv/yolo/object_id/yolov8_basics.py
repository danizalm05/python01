'''
https://github.com/DAVIDNYARKO123/yolov8-silva/blob/main/yolov8_basics.py
https://youtu.be/hg4oVgNq7Do?t=399


Results saved to D:\python02\opencv\yolo\object_id\runs\detect\predict-......
'''


import sys
import getpass
from ultralytics import YOLO
import numpy

img='cats.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
path = BASE_FOLDER+img
print("Image  = ",path) 



#   load a pretrained YOLOv8n   model
model = YOLO("yolov8n.pt", "v8")  

# predict on an image
#detection_output = model.predict(source="inference/images/img0.JPG", conf=0.25, save=True)
detection_output = model.predict(source=path, conf=0.25, save=True)

# https://youtu.be/hg4oVgNq7Do?t=578
# Display tensor array
print("\n\n detection_output\n========================\n",detection_output)

# Display numpy array
print("\n\n detection_output[0].numpy()\n==================\n",detection_output[0].numpy())
 
