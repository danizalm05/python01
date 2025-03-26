"""
 75-Extracting features for machine learning using Gabor filter banks.py
 -----------------------------------------------------
 
https://www.youtube.com/watch?v=ywyomOyXpxg&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=77 
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial75-Extracting_features_using_Gabor_Filter.py 


image:
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/images/synthetic.jpg

 
Gabor filters are generally  used in texture analysis, 
edge detection, feature extraction, etc. 
Gabor filters are special classes of bandpass filters,


ksize Size of the filter returned.
sigma Standard deviation of the gaussian envelope.
theta Orientation of the normal to the parallel stripes of a 
Gabor function.
lambda Wavelength of the sinusoidal factor.
gamma Spatial aspect ratio.
psi Phase offset.
ktype Type of filter coefficients. It can be CV_32F or CV_64F.
indicates the type and range of values that each pixel in the Gabor kernel can hold.
Basically float32 or float64
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import pandas as pd 


import getpass
from pathlib import Path
import sys
import os
 

IMAGE_NAME =  'synthetic.jpg' # 'BSE.tif'   'Osteosarcoma_01_transl.tif'  '2.jpg'
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

img = cv2.imread(IMAGE)#Gray image 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    

#Here, if you have multichannel image then extract the right channel 
# instead of converting the image to grey. 
#For example, if DAPI contains nuclei information, extract the DAPI 
#channel image first. 

#Multiple images can be used for training. For that, you need to 
#concatenate the data

plt.imshow(img)

#Feature #1: Save original image pixels into a data frame. 
img2 = img.reshape(-1)
df = pd.DataFrame()
df['Original Image'] = img2

#Generate Gabor features
num = 1  #To count numbers up in order to give Gabor features a lable in the data frame
kernels = []  #Create empty list to hold all kernels that we will generate in a loop
for theta in range(8):   #Define number of thetas. Here only 2 theta values 0 and 1/4 . pi 
    theta = theta / 4. * np.pi
    for sigma in (1, 3, 5, 7):  #Sigma with values of 1 and 3
        for lamda in np.arange(0, np.pi, np.pi / 4):   #Range of wavelengths
            for gamma in (0.05, 0.5):   #Gamma values of 0.05 and 0.5
                           
                gabor_label = 'Gabor' + str(num)  #Label Gabor columns as Gabor1, Gabor2, etc.
#                print(gabor_label)
                ksize=5  #Try 15 for hidden image. Or 9 for others
                phi = 0  #0.8 for hidden image. Otherwise leave it to 0
                kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)    
                kernels.append(kernel)
                #Now filter the image and add values to a new column 
                fimg = cv2.filter2D(img2, cv2.CV_8UC3, kernel)                
                filtered_img = fimg.reshape(-1)
                
                #write image to a file. The directory must created
                cv2.imwrite(BASE_FOLDER+'/gabor_filtered/'+gabor_label+'.jpg', filtered_img.reshape(img.shape))

                df[gabor_label] = filtered_img  #Labels columns as Gabor1, Gabor2, etc.
                print(gabor_label, ': theta=', theta, ': sigma=', sigma, ': lamda=', lamda, ': gamma=', gamma)
                
                num += 1  #Increment for gabor column label
                
print(df.head())

#df.to_csv("Gabor.csv")

 