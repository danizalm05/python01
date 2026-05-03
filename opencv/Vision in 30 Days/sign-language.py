
'''

https://github.com/computervisioneng/sign-language-detector-python
https://www.youtube.com/watch?v=MJCSjXepaAM&list=PLb49csYFtO2HGELdc-RLRCNVNy0g2UMwc&index=3

'''
import pickle

import cv2 

from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision import hand_landmarker
 
from mediapipe.tasks.python.vision import RunningMode
import cv2
import numpy as np

print(mp.__version__)  