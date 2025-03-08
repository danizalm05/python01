"""
  55_image_segmentation_followed_by_measurements.py
 -----------------------------------------------------
 Measure properties of labeled image regions.
https://www.youtube.com/watch?v=qfUJHY3ku9k&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=56
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial55_image_segmentation_followed_by_measurements.py

image:
    python_for_image_processing_APEER/images/cast_iron1.tif

https://scikit-image.org/docs/stable/api/skimage.measure.html#skimage.measure.regionprops
https://github.com/scikit-image/scikit-image/blob/v0.17.2/skimage/measure/_regionprops.py#L643
 
14:00

"""



from skimage import measure, io, img_as_ubyte
import matplotlib.pyplot as plt
from skimage.color import label2rgb, rgb2gray
import numpy as np
import cv2
import getpass
from pathlib import Path
import sys


USER = getpass.getuser()
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE_NAME_1 = 'cast_iron1.tif'  # '2.jpg' 'lena.jpg' 'scratch0.tif'  'Osteosarcoma_01_transl.tif'
IMAGE1 = BASE_FOLDER + IMAGE_NAME_1

# Check if the file exists
if not(Path(IMAGE1).exists()):
    msg = "Error: file " + IMAGE1 +" does not exist"
    sys.exit(msg)
   




image = cv2.imread(IMAGE1, 0)#Gray image
#img = io.imread(IMAGE1)
#image = img_as_ubyte(rgb2gray(img))
plt.imshow(image, cmap='gray')
scale = 0.6 #microns/pixel

#plt.hist(image.flat, bins=100, range=(0,170))  #.flat returns the flattened numpy array (1D)

from skimage.filters import threshold_otsu
threshold = threshold_otsu(image)

#Generate thresholded image
thresholded_img = image < threshold
plt.imshow(thresholded_img)


#Remove edge touching regions
from skimage.segmentation import clear_border
edge_touching_removed = clear_border(thresholded_img)
plt.imshow(edge_touching_removed)


#Label connected regions of an integer array using measure.label
#Labels each connected entity as one object
#Connectivity = Maximum number of orthogonal hops to consider a pixel/voxel as a neighbor. 
#If None, a full connectivity of input.ndim is used, number of dimensions of the image
#For 2D image it would be 2

label_image = measure.label(edge_touching_removed, connectivity=image.ndim)

plt.imshow(label_image)
#Return an RGB image where color-coded labels are painted over the image.
#Using label2rgb
plt.show()

image_label_overlay = label2rgb(label_image, image=image)
plt.imshow(image_label_overlay) 
plt.show()

#Calculate properties
#Using regionprops or regionprops_table
all_props=measure.regionprops(label_image, image)
#Can print various parameters for all objects
for prop in all_props:
    print('Label: {} Area: {}'.format(prop.label, prop.area))

#Compute image properties and return them as a pandas-compatible table.
#Available regionprops: area, bbox, centroid, convex_area, coords, eccentricity,
# equivalent diameter, euler number, label, intensity image, major axis length, 
#max intensity, mean intensity, moments, orientation, perimeter, solidity, and many more


props = measure.regionprops_table(label_image, image, 
                          properties=['label',
                                      'area', 'equivalent_diameter',
                                      'mean_intensity', 'solidity'])

import pandas as pd
df = pd.DataFrame(props)
#print(df.head())

#To delete small regions...
df = df[df['area'] > 50]
#print(df.head()) 

#Convert to micron scale
df['area_sq_microns'] = df['area'] * (scale**2)
df['equivalent_diameter_microns'] = df['equivalent_diameter'] * (scale)
print(df.head())
print(df['area_sq_microns'])
#df.to_csv('cast_iron_measurements.csv')
img = image









 
 
fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

ax1 = fig.add_subplot(3,3,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(3,3,2)
ax2.imshow(thresholded_img, cmap='gray')
ax2.title.set_text('thresholded_img')

ax3 = fig.add_subplot(3,3,3)
ax3.hist(img.flat, bins=100, range=(0,255))
ax3.title.set_text('hist color range 100,255')

ax4 = fig.add_subplot(3,3,4)
ax4.imshow(edge_touching_removed, cmap='gray')
ax4.title.set_text('edge_touching_removed')


ax5 = fig.add_subplot(3,3,5)
ax5.imshow(label_image)#,cmap='gray')
ax5.title.set_text('label_image')



ax6 = fig.add_subplot(3,3,6)
ax6.imshow(image_label_overlay)#, cmap='gray')
ax6.title.set_text('image_label_overlay')

ax7 = fig.add_subplot(3,3,7)
ax7.imshow(img, cmap='gray')
ax7.title.set_text('binarize entropy image')

plt.show()
 