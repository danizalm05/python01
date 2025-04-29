"""
83 - Image classification using traditional machine learning 
 -----------------------------------------------------
https://www.youtube.com/watch?v=nK-2k_ENgEc&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=85

https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial83_feature_extraction_RF_classification_V2.0.py
image url
 


"""

import numpy as np
import cv2
import pandas as pd
from matplotlib import pyplot as plt


 
import getpass
from pathlib import Path
import sys
import os


IMAGE_NAME =  'train_imgs_cropped_768.tif'#'Sandstone_Versa0050_test.tif' # 'BSE.tif'   'Osteosarcoma_01_transl.tif'  '2.jpg'
MASK= 'train_masks_grey_cropped_768.tif'# 'mask01.tif'  


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