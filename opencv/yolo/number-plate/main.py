
'''
 automatic-number-plate-recognition-python
 https://youtu.be/fyJB1t0o0ms?t=458
 https://github.com/computervisioneng/automatic-number-plate-recognition-python-yolov8/blob/main/main.py
''' 

from ultralytics import YOLO
import cv2
 
# load models
coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('./models/license_plate_detector.pt')


# load video
cap = cv2.VideoCapture('./sample.mp4')