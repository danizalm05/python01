"""
     51 - What is image thresholding and segmentation?
 -----------------------------------------------------
https://www.youtube.com/watch?v=8TkligJJCAQ&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=52
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial51_what_is_image_segmentation_and_thresholding.py
 

 Manual and auto thresholding
 20:38
"""
 
import cv2
import matplotlib.pyplot as plt
 
import getpass
import os


USER = getpass.getuser()

BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE_NAME_1 = 'Osteosarcoma_01.tif'  # '2.jpg' 'lena.jpg'
IMAGE_NAME_2 = 'Osteosarcoma_01_transl.tif'


IMAGE1 = BASE_FOLDER + IMAGE_NAME_1
IMAGE2 = BASE_FOLDER + IMAGE_NAME_2
print(IMAGE1)

img = cv2.imread(IMAGE1 , 1)#read as color image

#########################MANUAL##################
#Separate blue channels as they contain nuclei pixels (DAPI). 
blue_channel = img[:,:,0]
plt.imshow(blue_channel, cmap='gray')

 
#hist(blue_channel.flat, bins=100, range=(0,70))  #.flat returns the flattened numpy array (1D)
 
 

#Manual thresholding by setting threshold value to numpy array
#After thresholding we will get a binary image.
background = (blue_channel <= 40)
nuclei = (blue_channel > 40)# An array of boolean values
#plt.imshow(nuclei, cmap='gray')

#Using opencv to perform manual threshold
#All pixels above 40 will have pixel value 255
#Should be exactly same as the above method. 
ret1, thresh1 = cv2.threshold(blue_channel, 40, 255, cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap='gray')

######################################################

############# AUTO using OTSU ##########################
#Using opencv for otsu based automatic thresholding
ret2, thresh2 = cv2.threshold(blue_channel,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#Reports a value of 50 as threshold for the nuclei.
 
#Now, let us segment the image, meaning assign values of 0, 1, 2, ... to pixels
import numpy as np 
#np.digitize needs bins to be defined as an array
#So let us convert the threshold value to an array
# #np.digitize assign values 0, 1, 2, 3, ... to pixels in each class.
#For binary it wold be 0 and 1. 
regions1=np.digitize(blue_channel, bins=np.array([ret2]))

plt.imshow(regions1)

plt.title( 'bins=np.array([ret2])')
plt.axis("off") 
#################################################################### 
 

 
fig = plt.figure(figsize=(16, 16))

plt.subplots_adjust ( hspace=0.6)





ax1 = fig.add_subplot(3,3,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(3,3,2)
ax2.imshow(blue_channel, cmap='gray')
ax2.title.set_text('blue_channel')

ax3 = fig.add_subplot(3,3,3)
ax3.hist(blue_channel.flat, bins=100, range=(0,50))
ax3.title.set_text('hist color range 0- 50')

ax4 = fig.add_subplot(3,3,4)
ax4.imshow(nuclei, cmap='gray')
ax4.title.set_text('nuclei menual metod')


ax5 = fig.add_subplot(3,3,5)
ax5.imshow(thresh1, cmap='gray')
ax5.title.set_text('nuclei cv2')



ax6 = fig.add_subplot(3,3,6)
ax6.imshow(thresh2, cmap='gray')
ax6.title.set_text('AUTO using OTSU')



ax7 = fig.add_subplot(3,3,7)
ax7.imshow(regions1, cmap='gray')
ax7.title.set_text('regions1')
 
plt.show()