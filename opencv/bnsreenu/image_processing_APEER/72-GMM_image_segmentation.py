"""
 72-GMM_image_segmentation.py
 -----------------------------------------------------
What is Gaussian Mixture Model (GMM) 
 Unsuprvised tecnich
 use it for image segmentation?
https://www.youtube.com/watch?v=__UcukytHuc&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=74
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial72-GMM_image_segmentation.py

image:
   https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/images/BSE.tif

NOTE:
Both BIC and AIC are included as built in methods as part of Scikit-Learn's  GaussianMixture. 
Therefore we do not need to import any other libraries to compute these. 
The way you compute them (for example BIC) is by fitting a GMM model and then calling the method BIC. 

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
#from scipy import ndimage
#from skimage import measure, color, io
import getpass
from pathlib import Path
import sys
import os
 

IMAGE_NAME = 'BSE.tif'  # 'Osteosarcoma_01_transl.tif'
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
   
image = cv2.imread(IMAGE)#Gray image
 

plt.imshow(image)
#06:00
#============================   Output  ===============================   

fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

ax1 = fig.add_subplot(4,3,1)
ax1.imshow(image, cmap='gray')
ax1.title.set_text('Input Image')
'''
ax2 = fig.add_subplot(4,3,2)
ax2.imshow(cells, cmap='gray')
ax2.title.set_text('cells - blue channel')

ax3 = fig.add_subplot(4,3,3)
ax3.hist(image.flat, bins=100, range=(0,255))
ax3.title.set_text('hist color range')

ax4 = fig.add_subplot(4,3,4)
ax4.imshow(thresh, cmap='gray')
ax4.title.set_text('thresh')


ax5 = fig.add_subplot(4,3,5)
ax5.imshow(opening1)#,cmap='gray')
ax5.title.set_text('opening1')



ax6 = fig.add_subplot(4,3,6)
ax6.imshow(opening2)#, cmap='gray')
ax6.title.set_text('opening2')

ax7 = fig.add_subplot(4,3,7)
ax7.imshow(sure_bg, cmap='gray')
ax7.title.set_text('surebackground')

 

ax8 = fig.add_subplot(4,3,8)
ax8.imshow( sure_fg , cmap='gray')
ax8.title.set_text(' sure_fg ')


ax9 = fig.add_subplot(4,3,9)
ax9.imshow(unknown, cmap='gray')
ax9.title.set_text('unknown')

#
ax10 = fig.add_subplot(4,3,10)
ax10.imshow(markers)#, cmap='gray')
ax10.title.set_text('markers')

 

ax11 = fig.add_subplot(4,3,11)
ax11.imshow(markers10,cmap='gray')
ax11.title.set_text('markers10')

 

ax12 = fig.add_subplot(4,3,12)
ax12.imshow(img2,cmap='gray')
ax12.title.set_text('labels are painted over the image.')

'''
plt.show()
 