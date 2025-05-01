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
    TRAIN_FOLDER = "/home/"+USER +'/Pictures/ml/train/'
    TEST_FOLDER = "/home/"+USER +'/Pictures/ml/test/'
    print(TRAIN_FOLDER)
else: #this is a windows  system 
    TRAIN_FOLDER = 'C:/Users/' + USER + '/Pictures/ml/train/'
    TEST_FOLDER = 'C:/Users/' + USER + '/Pictures/ml/test/'

# Check if the file exists
if not(Path(TRAIN_FOLDER).exists()):
    msg = "Error: Train Dir " + TRAIN_FOLDER +" does not exist"
    sys.exit(msg)
if not(Path(TEST_FOLDER).exists()):
    msg = "Error: Test Dir " + TEST_FOLDER +" does not exist"
    sys.exit(msg)    
    
''
print("\n",TEST_FOLDER ," listdir  = " ,os.listdir(TEST_FOLDER),"\n")

#Resize images to
SIZE = 128

#Capture images and labels into arrays.
#Start by creating empty lists.
train_images = []
train_labels = [] 
for directory_path in glob.glob(TRAIN_FOLDER +"*"):
    label = directory_path.split("\\")[-1]
    #print(label)
    for img_path in glob.glob(os.path.join(directory_path, "*.jpg")):
      #print(img_path)
      img = cv2.imread(img_path, cv2.IMREAD_COLOR) #Reading color images
      img = cv2.resize(img, (SIZE, SIZE)) #Resize images
      #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) #Optional step. Change BGR to RGB
      train_images.append(img)
      train_labels.append(label) 
      
train_images = np.array(train_images)
train_labels = np.array(train_labels)    


#Do exactly the same for test/validation images
# test  09:46
test_images = []
test_labels = [] 
for directory_path in glob.glob(TEST_FOLDER +"*"):
    label = directory_path.split("\\")[-1]
    print(label)