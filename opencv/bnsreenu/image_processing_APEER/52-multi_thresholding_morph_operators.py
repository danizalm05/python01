"""
     52 -- Auto-thresholding for multiple regions ​using multi-otsu
 -----------------------------------------------------
https://www.youtube.com/watch?v=3fMgy7VTYH0&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=53
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial52_multi_thresholding_and_morph_operators.py
10:00
"""
 
import cv2
import matplotlib.pyplot as plt
import numpy as np
import getpass
import os


USER = getpass.getuser()

BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE_NAME_1 = 'BSE.tif'  # '2.jpg' 'lena.jpg'



IMAGE1 = BASE_FOLDER + IMAGE_NAME_1

print(IMAGE1)

img = cv2.imread(IMAGE1 , 0)#read as color image

#########################MANUAL##################

#Denoise for better results
from skimage.restoration import denoise_tv_chambolle
denoised_img = denoise_tv_chambolle(img, weight=0.1, eps=0.0002, n_iter_max=200, multichannel=False)

plt.imshow(img, cmap='gray')
plt.show()
plt.hist(img.flat, bins=100, range=(100,255))
plt.show()
#.flat returns the flattened numpy array (1D)
#Can perform manual segmentation but auto works fine
region1 = (img >= 0) & (img <75)
region2 = (img >= 75) & (img <140)
region3 = (img >= 140) & (img <200)
region4 = (img >= 200) & (img <=255)
all_regions = np.zeros((img.shape[0], img.shape[1], 3)) #Create 3 channel blank image of same size as original
all_regions[region1] = (1,0,0)
all_regions[region2] = (0,1,0)
all_regions[region3] = (0,0,1)
all_regions[region4] = (1,1,0)
plt.imshow(all_regions)
plt.show()


#################################################################### 
 

 
fig = plt.figure(figsize=(16, 16))

plt.subplots_adjust ( hspace=0.6)





ax1 = fig.add_subplot(3,3,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(3,3,2)
ax2.imshow(all_regions, cmap='gray')
ax2.title.set_text('all_regions')

ax3 = fig.add_subplot(3,3,3)

ax3.hist(img.flat, bins=100, range=(0,255))
ax3.title.set_text('hist color range 100,255')

ax4 = fig.add_subplot(3,3,4)
ax4.imshow(img, cmap='gray')
ax4.title.set_text('nuclei menual metod')


ax5 = fig.add_subplot(3,3,5)
ax5.imshow(img, cmap='gray')
ax5.title.set_text('nuclei cv2')



ax6 = fig.add_subplot(3,3,6)
ax6.imshow(img, cmap='gray')
ax6.title.set_text('AUTO using OTSU')



ax7 = fig.add_subplot(3,3,7)
ax7.imshow(img, cmap='gray')
ax7.title.set_text('regions1')
 
plt.show()