"""
 57_Cell Nuclei analysis using watershed.py
 -----------------------------------------------------
 Measure properties of labeled image regions.
https://www.youtube.com/watch?v=M1mJsJ5M4iE&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=58
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial57_Cell%20Nuclei%20analysis%20using%20watershed.py

 image:
    python_for_image_processing_APEER/images/Osteosarcoma_01.tif.tif

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


# Threshold image is  binary using OTSU. ALl thresholded pixels will be set
# to 255
ret1, thresh = cv2.threshold(cells, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
print("ret1,_ = cv2.threshold(......) =  ", ret1)
#10:20

# Morphological operations to remove small noise - opening
#To remove holes we can use closing
kernel = np.ones((3,3),np.uint8)
opening1 = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

from skimage.segmentation import clear_border
opening2 = clear_border(opening1) #Remove edge touching grains
 


#                        STEP 1: Sure background 
#Now we know that the regions at the center of cells is for sure cells
#The region far away is background.
#We need to extract sure regions. For that erode a few times. 
#But we have cells touching, so erode alone will not work. 
#To separate touching objects, the best approach would be distance
# transform and then thresholding.

# let us start by identifying sure background area
# dilating pixes a few times increases cell boundary to background. 
# This way whatever is remaining for sure will be background. 
#The area in between sure background and foreground is our ambiguous area. 
#Watershed should find this area for us. 
sure_bg = cv2.dilate(opening2,kernel,iterations=10)

#plt.imshow(sure_bg, cmap='gray') #Dark region is our sure background


# Finding sure foreground area using distance transform and thresholding
#intensities of the points inside the foreground regions are changed to 
#distance their respective distances from the closest 0 value (boundary).
#https://www.tutorialspoint.com/opencv/opencv_distance_transformation.htm
dist_transform = cv2.distanceTransform(opening2,cv2.DIST_L2,5)
#plt.imshow(dist_transform, cmap='gray') #Dist transformed img. 
#15:00
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
ax5.imshow(opening1)#,cmap='gray')
ax5.title.set_text('opening1')



ax6 = fig.add_subplot(3,3,6)
ax6.imshow(opening2)#, cmap='gray')
ax6.title.set_text('opening2')

ax7 = fig.add_subplot(3,3,7)
ax7.imshow(sure_bg, cmap='gray')
ax7.title.set_text('surebackground')

 

ax8 = fig.add_subplot(3,3,8)
ax8.imshow(dist_transform, cmap='gray')
ax8.title.set_text('sureforground')


ax9 = fig.add_subplot(3,3,9)
ax9.imshow(dist_transform, cmap='gray')
ax9.title.set_text('sureforground')



plt.show()
 