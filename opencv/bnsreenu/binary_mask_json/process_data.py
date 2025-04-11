
'''
VGG-Image-Annotator: Parsing the JSON file
The code in this repository is used to parse the JSON file generated 
after annotating the images through the VGG Image Annotator tool designed by
 Visual Geometry Group.

https://github.com/nikhilroxtomar/VGG-Image-Annotator-Process-JSON-file


'''


import os
import numpy as np
import cv2
from glob import glob
from tqdm import tqdm
import json
 