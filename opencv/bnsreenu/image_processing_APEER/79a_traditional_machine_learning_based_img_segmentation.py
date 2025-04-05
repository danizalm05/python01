"""
l79_part1_traditional_machine_learning_based_img_segmentation.py
 -----------------------------------------------------
https://www.youtube.com/watch?v=uWTzkUD3V9g&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=81
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial79_part1_traditional_machine_learning_based_img_segmentation.py

image url
 https://github.com/anukash/Image_segmentation_with_ML/blob/main/Sandstone_Versa0050_test.tif

Gabor and traditional filters for feature generation and 
Random Forest, SVM for classification. 

'images/sandstone/Train_images/Sandstone_Versa0000.tif'
"""

import numpy as np
import cv2
import pandas as pd
from matplotlib import pyplot as plt


 
import getpass
from pathlib import Path
import sys
import os


IMAGE_NAME =  'Sandstone_Versa0000_train.tif' # 'BSE.tif'   'Osteosarcoma_01_transl.tif'  '2.jpg'
USER = getpass.getuser()

if (os.name == "posix"):  #this is a linux  system 
    BASE_FOLDER = "/home/"+USER +'/Pictures/'
    print(BASE_FOLDER)
else: #this is a windows  system 
    BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

# Check if the file exists
if not(Path(IMAGE).exists()):
    msg = "Error: file " + IMAGE +" does not exist"
    sys.exit(msg)
   
img = cv2.imread(IMAGE)
plt.imshow(img) 
plt.show()



img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  