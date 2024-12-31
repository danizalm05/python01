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
 
03:30

"""



from skimage import measure, io, img_as_ubyte
import matplotlib.pyplot as plt
from skimage.color import label2rgb, rgb2gray
import numpy as np
import cv2
import getpass



USER = getpass.getuser()
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE_NAME_1 = 'cast_iron1.tif'  # '2.jpg' 'lena.jpg' 'scratch0.tif'  'Osteosarcoma_01_transl.tif'
IMAGE1 = BASE_FOLDER + IMAGE_NAME_1

print(IMAGE1)

image = cv2.imread(IMAGE1, 0)#Gray image
#img = io.imread(IMAGE1)
#image = img_as_ubyte(rgb2gray(img))
plt.imshow(image, cmap='gray')
scale = 0.6 #microns/pixel

plt.hist(image.flat, bins=100, range=(0,150))  #.flat returns the flattened numpy array (1D)


img = image









 
 
fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

ax1 = fig.add_subplot(3,3,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(3,3,2)
ax2.imshow(img , cmap='gray')
ax2.title.set_text(' entropy_img')

ax3 = fig.add_subplot(3,3,3)

ax3.hist(img.flat, bins=100, range=(0,255))
ax3.title.set_text('hist color range 100,255')

ax4 = fig.add_subplot(3,3,4)
ax4.imshow(img, cmap='gray')
ax4.title.set_text('binary')


ax5 = fig.add_subplot(3,3,5)
ax5.imshow(img,cmap='gray')
ax5.title.set_text('Entropy')



ax6 = fig.add_subplot(3,3,6)
plt.hist(img.flat, bins=100, range=(0,5))
#ax6.imshow(img, cmap='gray')
ax6.title.set_text('entropy hist')

ax7 = fig.add_subplot(3,3,7)
ax7.imshow(img, cmap='gray')
ax7.title.set_text('binarize entropy image')

plt.show()
 