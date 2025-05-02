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

import seaborn as sns
from skimage.filters import sobel


 
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
    #print(label)
    fruit_label = directory_path.split("\\")[-1]
    for img_path in glob.glob(os.path.join(directory_path, "*.jpg")):
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (SIZE, SIZE))
        #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) #Optional
        test_images.append(img)
        test_labels.append(fruit_label)
        #print(img_path)
test_images = np.array(test_images)
test_labels = np.array(test_labels)
    


#Encode labels from text (folder names) to integers.
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(test_labels)
test_labels_encoded = le.transform(test_labels) # [0,1,2,3]
le.fit(train_labels)
train_labels_encoded = le.transform(train_labels)    

#Split data into test and train datasets (already split but assigning to meaningful convention)
#If you only have one dataset then split here
x_train, y_train, x_test, y_test = train_images, train_labels_encoded, test_images, test_labels_encoded

# Normalize pixel values to between 0 and 1
max_color = 255.0
x_train, x_test = x_train / max_color, x_test / max_color    


###################################################################
# FEATURE EXTRACTOR function
# input shape is (n, x, y, c) - number of images, x, y, and channels
def feature_extractor(dataset):
    x_train = dataset
    image_dataset = pd.DataFrame()#Create df for each image
  
    for image in range(x_train.shape[0]):  #iterate through each file 
       print(image, "\n-----\n")
       df = pd.DataFrame()  #Temporary data frame to capture information for each loop.
       #Reset dataframe to blank after each loop.
       
       input_img = x_train[image, :,:,:]# image is  the number of the image file
       img = input_img
             
       #START ADDING DATA TO THE DATAFRAME
       #Add feature extractors, e.g. edge detection, smoothing, etc. 
           
        # FEATURE 1 - Pixel values
        #Add pixel values to the data frame
       pixel_values = img.reshape(-1)#Reshape image to a vector
       df['Pixel_Value'] = pixel_values   #Pixel value itself as a feature
       #df['Image_Name'] = image   #Capture image name as we read multiple images
       
       ######### FEATURE 2 - Bunch of Gabor filter responses 20:00
       num = 1         #To count numbers up in order to give Gabor features 
                       #a lable in the data frame
       kernels = [] 
       for theta in range(2):   #Define number of thetas
           theta = theta / 4. * np.pi               
          
           for sigma in (1, 3):  #Sigma with 1 and 3
               lamda = np.pi/4
               gamma = 0.5
               gabor_label = 'Gabor' + str(num)  #Label Gabor columns as Gabor1, Gabor2, etc.
               ksize=9
               kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, 0, ktype=cv2.CV_32F)    
               kernels.append(kernel)
               #Now filter the image and add values to a new column 
               fimg = cv2.filter2D(img, cv2.CV_8UC3, kernel)
               filtered_img = fimg.reshape(-1)
               df[gabor_label] = filtered_img  #Labels columns as Gabor1, Gabor2, etc.
               print(gabor_label, ': theta=', theta, ': sigma=', sigma, ': lamda=', lamda, ': gamma=', gamma)
               num += 1  #Increment for gabor column label
               
             # FEATURE 3 Sobel
       '''
       edge_sobel = sobel(img)   
       edge_sobel1 = edge_sobel.reshape(-1)
       df['Sobel'] = edge_sobel1
       '''
        #Add more filters as needed        
     #Append features from current image to the dataset
       #image_dataset = image_dataset.append(df) #this command  is an error
       image_dataset = pd.concat([image_dataset, df])#, ignore_index=True)
      
    return image_dataset

####################################################################
#21:00





 
image_features = feature_extractor(x_train)

 