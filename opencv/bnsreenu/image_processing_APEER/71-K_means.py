"""
71-K_means.py
71a-K_means_demo.py

The KMeans algorithm clusters data by trying to separate samples
in n groups of equal variance, minimizing a criterion known as 
the inertia or within-cluster sum-of-squares 
 -------------------------------------------
https://www.youtube.com/watch?v=H_L7V_BH9pc&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=73

1. https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial71-K_means.py
2. https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial71a-K_means_demo.py
data file url
 https://github.com/bnsreenu/python_for_microscopists/blob/master/other_files/K_Means.xlsx

image url:
https://github.com/bnsreenu/python_for_microscopists/blob/master/images/BSE_Image.jpg
"""


import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_excel('data/K_Means.xlsx')
print(df.head())

import seaborn as sns
sns.regplot(x=df['X'], y=df['Y'], fit_reg=False) 
plt.show()



from sklearn.cluster import KMeans

#https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

num_of_clusters = 3
kmeans = KMeans(n_clusters=num_of_clusters, init='k-means++', max_iter=300, n_init=10, random_state=42)

model = kmeans.fit(df)

predicted_values = kmeans.predict(df)


plt.scatter(df['X'], df['Y'], c=predicted_values, s=50, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='black', alpha=0.5)
plt.show()

#9:00
###########################  using photo  ##############
IMAGE_NAME = 'BSE_Image.jpg'  # 'Osteosarcoma_01_transl.tif'
import cv2
import sys
import os
import getpass
from pathlib import Path
IMAGE_NAME =  '2.jpg'# 'BSE.tif'  BSE_Image.jpg  'Osteosarcoma_01_transl.tif'
USER = getpass.getuser()


if (os.name == "posix"):  #this is a linux  system 
    BASE_FOLDER = "/home/"+USER +'/Pictures/'
    print(BASE_FOLDER)
else: # this is a windows  system 
    BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

# Check if the file exists
if not(Path(IMAGE).exists()):
    msg = "Error: file " + IMAGE +" does not exist"
    sys.exit(msg)
   






#################################
#Image segmentation using K-means
from skimage import io
import numpy as np
from matplotlib import pyplot as plt

img = io.imread(IMAGE, as_gray=False)#Gray image
 
plt.imshow(img, cmap='gray')
plt.show()

# Convert MxNx3 image into Kx3 where K=MxN
# instad ofv 3 matrix we will have 3 vectors size of MxN
img2 = img.reshape((-1, 3))  #-1 reshape means, in this case MxN

#We convert the unit8 values to float as it is a requirement 
# of the k-means method of OpenCV
#img2 = np.float32(img2)

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=82)
model = kmeans.fit(img2)
predicted_values = kmeans.predict(img2)

#res = center[label.flatten()]

#  reshape to the size of the  original image
segm_image = predicted_values.reshape((img.shape[0], img.shape[1]))
plt.imshow(segm_image)#, cmap='gray')
plt.show() 



