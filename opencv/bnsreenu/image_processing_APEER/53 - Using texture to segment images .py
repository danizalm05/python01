"""
  53 - Using texture to segment images (demo in python)
 -----------------------------------------------------
https://www.youtube.com/watch?v=QmozYygPbZA&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=54https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial52_multi_thresholding_and_morph_operators.py
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial53-using_texture_to_segment_images.py
Scratch Assay single image segmentation
8:00
"""
import cv2
import numpy as np
import getpass
import os
import matplotlib.pyplot as plt
from skimage import io

import numpy as np
from skimage.filters import threshold_otsu


USER = getpass.getuser()

BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE_NAME_1 = 'Osteosarcoma_01_transl.tif'  # '2.jpg' 'lena.jpg' 'scratch0.tif'



IMAGE1 = BASE_FOLDER + IMAGE_NAME_1

print(IMAGE1)

#img = cv2.imread(IMAGE1 , 1)#read as color image

img = io.imread(IMAGE1 , as_gray=True)


plt.imshow(img, cmap='gray')
plt.show()
#plt.hist(img.flat, bins=100, range=(100,255))
#plt.show()

##################################################
#Variance - not a great way to quantify texture
from scipy import ndimage
k = 7
img_mean = ndimage.uniform_filter(img, (k, k))
img_sqr_mean = ndimage.uniform_filter(img**2, (k, k))
img_var = img_sqr_mean - img_mean**2
plt.imshow(img_var, cmap='gray')
plt.show()
#######################################################


#######################################################################

'''
fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

ax1 = fig.add_subplot(3,3,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(3,3,2)
ax2.imshow(img, cmap='gray')
ax2.title.set_text('all_regions')

ax3 = fig.add_subplot(3,3,3)

ax3.hist(img.flat, bins=100, range=(0,255))
ax3.title.set_text('hist color range 100,255')

ax4 = fig.add_subplot(3,3,4)
ax4.imshow(img, cmap='gray')
ax4.title.set_text(' multi-Otsu threshold ')


ax5 = fig.add_subplot(3,3,5)
ax5.imshow(img, cmap='gray')
ax5.title.set_text('all_segments_cleaned')



ax6 = fig.add_subplot(3,3,6)
ax6.imshow(img, cmap='gray')
ax6.title.set_text('AUTO using OTSU')



ax7 = fig.add_subplot(3,3,7)
ax7.imshow(img, cmap='gray')
ax7.title.set_text('regions1')

plt.show()
'''