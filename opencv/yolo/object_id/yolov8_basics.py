'''
https://github.com/DAVIDNYARKO123/yolov8-silva/blob/main/yolov8_basics.py
https://youtu.be/hg4oVgNq7Do?t=399
'''


from ultralytics import YOLO
import numpy

#   load a pretrained YOLOv8n   model
model = YOLO("yolov8n.pt", "v8")  

# predict on an image
detection_output = model.predict(source="inference/images/img0.JPG", conf=0.25, save=True)

# https://youtu.be/hg4oVgNq7Do?t=578
# Display tensor array
print(detection_output)

# Display numpy array
print(detection_output[0].numpy()) 
