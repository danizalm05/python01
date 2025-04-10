"""
79_part1_traditional_machine_learning_based_img_segmentation.py
 -----------------------------------------------------
https://www.youtube.com/watch?v=uWTzkUD3V9g&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=81
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial79_part1_traditional_machine_learning_based_img_segmentation.py

image url
 https://github.com/anukash/Image_segmentation_with_ML/blob/main/Sandstone_Versa0050_test.tif

Gabor and traditional filters for feature generation and 
Random Forest, SVM for classification. 

'images/sandstone/Train_images/Sandstone_Versa0000.tif'
Sandstone_Versa0000_mask.tif
 

Image Labeling   Annotation Tools
https://medevel.com/image-annotation-tools-1831/
====================================================	  
https://www.makesense.ai/ 


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
#Here, if you have multichannel image then extract the right channel instead of converting the image to grey. 
#For example, if DAPI contains nuclei information, extract the DAPI channel image first. 

#Multiple images can be used for training. For that, you need to concatenate the data

#Save original image pixels into a data frame. This is our Feature #1.
#Save original image pixels into a data frame. This is our Feature #1.
img2 = img.reshape(-1)
df = pd.DataFrame()
df['Original Image'] = img2

#Generate Gabor features
num = 1  #To count numbers up in order to give Gabor features a lable in the data frame
kernels = []

for theta in range(2):   #Define number of thetas
    theta = theta / 4. * np.pi
    for sigma in (1, 3):  #Sigma with 1 and 3
        for lamda in np.arange(0, np.pi, np.pi / 4):   #Range of wavelengths
            for gamma in (0.05, 0.5):   #Gamma values of 0.05 and 0.5
            
                
                gabor_label = 'Gabor' + str(num)  #Label Gabor columns as Gabor1, Gabor2, etc.
                #print(gabor_label)
                ksize=9
                kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, 0, ktype=cv2.CV_32F)    
                kernels.append(kernel)
                #Now filter the image and add values to a new column 
                fimg = cv2.filter2D(img, cv2.CV_8UC3, kernel)
                filtered_img = fimg.reshape(-1)
                df[gabor_label] = filtered_img  #Labels columns as Gabor1, Gabor2, etc.
                print(gabor_label, ': theta=', theta, ': sigma=', sigma, ': lamda=', lamda, ': gamma=', gamma)
                num += 1  #Increment for gabor column label
                
########################################

########################################
#Gerate OTHER FEATURES and add them to the data frame
                
#CANNY EDGE
edges = cv2.Canny(img, 100,200)   #Image, min and max values
edges1 = edges.reshape(-1)
df['Canny Edge'] = edges1 #Add column to original dataframe

from skimage.filters import roberts, sobel, scharr, prewitt

#ROBERTS EDGE
edge_roberts = roberts(img)
edge_roberts1 = edge_roberts.reshape(-1)
df['Roberts'] = edge_roberts1

#SOBEL
edge_sobel = sobel(img)
edge_sobel1 = edge_sobel.reshape(-1)
df['Sobel'] = edge_sobel1

#SCHARR
edge_scharr = scharr(img)
edge_scharr1 = edge_scharr.reshape(-1)
df['Scharr'] = edge_scharr1

#PREWITT
edge_prewitt = prewitt(img)
edge_prewitt1 = edge_prewitt.reshape(-1)
df['Prewitt'] = edge_prewitt1

#GAUSSIAN with sigma=3
from scipy import ndimage as nd
gaussian_img = nd.gaussian_filter(img, sigma=3)
gaussian_img1 = gaussian_img.reshape(-1)
df['Gaussian s3'] = gaussian_img1

#GAUSSIAN with sigma=7
gaussian_img2 = nd.gaussian_filter(img, sigma=7)
gaussian_img3 = gaussian_img2.reshape(-1)
df['Gaussian s7'] = gaussian_img3

#MEDIAN with sigma=3
median_img = nd.median_filter(img, size=3)
median_img1 = median_img.reshape(-1)
df['Median s3'] = median_img1

#VARIANCE with size=3
#variance_img = nd.generic_filter(img, np.var, size=3)
#variance_img1 = variance_img.reshape(-1)
#df['Variance s3'] = variance_img1  #Add column to original dataframe


######################################  
IMAGE2 = BASE_FOLDER +'Sandstone_Versa0000_mask.tif'  
#Now, add a column in the data frame for the Labels
#For this, we need to import the labeled image

labeled_img = cv2.imread(IMAGE2)
#Remember that you can load an image with partial labels 
#But, drop the rows with unlabeled data  

 
plt.imshow(labeled_img) 
plt.show()   

 
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_BGR2GRAY)
 
plt.imshow(labeled_img) 
plt.show()
labeled_img1 = labeled_img.reshape(-1)
df['Labels'] = labeled_img1

print(df.head())      

original_img_data = df.drop(labels = ["Labels"], axis=1) #Use for prediction
#df.to_csv("Gabor.csv")
df = df[df.Labels != 0]# copy only Label non zero  values
