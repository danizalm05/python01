
'''
               Ultralytics YOLO . 
https://youtu.be/m9fH9OWn8YM?t=1931
https://youtu.be/m9fH9OWn8YM?t=2095
https://github.com/computervisioneng/train-yolov8-custom-dataset-step-by-step-guide

code:
https://github.com/computervisioneng/train-yolov8-custom-dataset-step-by-step-guide/blob/master/local_env/train.py


https://github.com/ultralytics/ultralytics

pip install ultralytics
'''


from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
#You need to create "config.yaml" https://github.com/computervisioneng/train-yolov8-custom-dataset-step-by-step-guide/blob/master/local_env/config.yaml
'''
path: /home/........./code/data  # dataset root dir
train: images/train  # train images (relative to 'path')
val: images/train  # val images (relative to 'path')
'''
# Classes
names:
  0: alpaca
'''
results = model.train(data="config.yaml", epochs=1)  # train the model