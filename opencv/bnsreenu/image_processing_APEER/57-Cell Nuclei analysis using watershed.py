"""
 57_Cell Nuclei analysis using watershed.py
 -----------------------------------------------------
 Measure properties of labeled image regions.
https://www.youtube.com/watch?v=M1mJsJ5M4iE&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=58
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial57_Cell%20Nuclei%20analysis%20using%20watershed.py

 image:
    python_for_image_processing_APEER/images/Osteosarcoma_01.tif.tif


Cell counting and size distribution analysis and dumps results into
 a csv file.
It uses watershed segmentation for better segmentation, separating 
touching nuclei.


"""


import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure, color, io

import getpass
from pathlib import Path
import sys
USER = getpass.getuser()

IMAGE_NAME = 'Osteosarcoma_01.tif'  # 'Osteosarcoma_01_transl.tif'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

# Check if the file exists
if not(Path(IMAGE).exists()):
    msg = "Error: file " + IMAGE +" does not exist"
    sys.exit(msg)
   
image = cv2.imread(IMAGE)#Gray image
#Extract only blue channel as DAPI / nuclear (blue) staining is the best
#channel to perform cell count.
cells = image[:,:,0]  #Blue channel. Image equivalent to grey image. 


pixels_to_um = 0.454 # 1 pixel = 454 nm (got this from the metadata of original image)


# Threshold image to binary using OTSU. ALl thresholded pixels will be set
# to 255
ret1, thresh = cv2.threshold(cells, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
print("ret1,_ = cv2.threshold(......) =  ", ret1)
#10:20
#============================   Output  ===============================   

fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

ax1 = fig.add_subplot(3,3,1)
ax1.imshow(image, cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(3,3,2)
ax2.imshow(cells, cmap='gray')
ax2.title.set_text('cells - blue channel')

ax3 = fig.add_subplot(3,3,3)
ax3.hist(image.flat, bins=100, range=(0,255))
ax3.title.set_text('hist color range')

ax4 = fig.add_subplot(3,3,4)
ax4.imshow(thresh, cmap='gray')
ax4.title.set_text('thresh')


ax5 = fig.add_subplot(3,3,5)
ax5.imshow(image)#,cmap='gray')
ax5.title.set_text('label_image')



ax6 = fig.add_subplot(3,3,6)
ax6.imshow(image)#, cmap='gray')
ax6.title.set_text('image_label_overlay')

ax7 = fig.add_subplot(3,3,7)
ax7.imshow(image, cmap='gray')
ax7.title.set_text('binarize entropy image')

plt.show()
 