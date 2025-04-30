"""
83 - Image classification using traditional machine learning 
 -----------------------------------------------------
https://www.youtube.com/watch?v=nK-2k_ENgEc&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=85

https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial83_feature_extraction_RF_classification_V2.0.py

 

/Pictures/ml/train
/Pictures/ml/validation
E
ach set of images will be stored in separate folders with appropriate names
Folder names are taken as labels. 
You can have any number of classes. 
Usually works well with a handful of training images. 

Be mindful of memory for large images and large number of filters.
In this example for Gabor, only theta and sigma are changed. You can create infinite filters
by changing lambda, gamma, and kszie. 

"""


import numpy as np
import cv2
import pandas as pd
from matplotlib import pyplot as plt
import glob

 
import getpass
from pathlib import Path
import sys
import os


USER = getpass.getuser()

if (os.name == "posix"):  #this is a linux  system 
    BASE_FOLDER = "/home/"+USER +'/Pictures/ml/train/'
    print(BASE_FOLDER)
else: #this is a windows  system 
    BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/ml/train/'


# Check if the file exists
if not(Path(BASE_FOLDER).exists()):
    msg = "Error: Dir " + BASE_FOLDER +" does not exist"
    sys.exit(msg)

print(os.listdir(BASE_FOLDER))

#Resize images to
SIZE = 128

#Capture images and labels into arrays.
#Start by creating empty lists.
train_images = []
train_labels = [] 
for directory_path in glob.glob(BASE_FOLDER +"*"):
    label = directory_path.split("\\")[-1]
    print(label)
    for img_path in glob.glob(os.path.join(directory_path, "*.jpg")):
      print(img_path)