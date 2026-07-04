# -*- coding: utf-8 -*-
"""

YOLOv8 Object Segmentation With Only Three Lines of Python Code
https://www.youtube.com/watch?v=BuTbKfq2ZcA&list=PL4Cc4cDq3t9mCdZ3t0czemfz7VwPdSjj9&index=50
"""

from ultralytics import YOLO
model = YOLO("yolov8n-seg.pt")
result = model(0,show=True,save=True)
print(result)