from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import mediapipe as mp
import sys


print ("mp.__version__ = ",mp.__version__)
print(dir(mp))
print (mp.__file__)
print(sys.version) 
 
print(sys.executable)
'''
base_options = python.BaseOptions(model_asset_path='face_detection_short_range.tflite')
options = vision.FaceDetectorOptions(
    base_options=base_options
)

#detector = vision.FaceDetector.create_from_options(options)
'''

import urllib.request

url = "https://storage.googleapis.com/mediapipe-models/face_detector/face_detector_short_range/float16/1/face_detector_short_range.tflite"
filename = "face_detector_short_range.tflite"

urllib.request.urlretrieve(url, filename)

print("Downloaded:", filename)



import os
print(os.path.exists("face_detector_short_range.tflite"))