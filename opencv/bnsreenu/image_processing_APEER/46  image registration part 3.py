"""
46 part 3- Useful image registration libraries in python p

#Method 4: Optical flow based shift. Best for warped images.
#takes two images and returns a vector field.
#For every pixel in image 1 you get a vector showing where it moved to in image 2.

#-----------------------------------------------------
https://www.youtube.com/watch?v=F4AV6SsUxXE&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=47
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial46_img_registration_libraries_in_python.py

https://github.com/bnsreenu/python_for_image_processing_APEER/tree/master/images

A couple of ways to perform image registration
https://image-registration.readthedocs.io/en/latest/image_registration.html
input photos:   Osteosarcoma_01.tif Osteosarcoma_01_transl.tif
 
07:00
"""
import cv2
from skimage import io
import numpy
from skimage.feature import register_translation
from scipy.ndimage import shift
import getpass
import os

print(numpy.__version__)
USER = getpass.getuser()

BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE_NAME_1 = 'Osteosarcoma_01.tif'  # '2.jpg' 'lena.jpg'
IMAGE_NAME_2 = 'Osteosarcoma_01_transl.tif'
img_list = []

for (image) in os.listdir(BASE_FOLDER):  # iterate through each file to perform some action
    img_list.append(image)

img_num = 17
IMAGE = BASE_FOLDER + img_list[img_num]
IMAGE1 = BASE_FOLDER + IMAGE_NAME_1
IMAGE2 = BASE_FOLDER + IMAGE_NAME_2
print(IMAGE1)


image = io.imread(IMAGE_NAME_1 , as_gray=True)
offset_image = io.imread(IMAGE_NAME_2 , as_gray=True)
# offset image translated by (-17, 18.) in y and x

from skimage import io


# offset image translated by (-17, 18) in y and x
from skimage import registration
flow = registration.optical_flow_tvl1(image, offset_image)

# display dense optical flow
flow_x = flow[1, :, :]  #Along width
flow_y = flow[0, :, :]  #Along height


#Example 1: Simple application by just taking mean of flow in x and y
#Let us find the mean of all pixels in x and y and shift image by that amount
#ideally, you need to move each pixel by the amount from flow
import numpy as np
xoff = np.mean(flow_x)
yoff = np.mean(flow_y)


print("Offset image was translated by: 18, -17")
print("Pixels shifted by: ", xoff, yoff)

from scipy.ndimage import shift
corrected_image = shift(offset_image, shift=(-xoff,-yoff), mode='constant')

#Example 2: Applying flow vectors to each pixel

height, width = image.shape

#Use meshgrid to Return coordinate matrices from coordinate vectors.
#Extract row and column coordinates to which flow vector values will be added.
row_coords, col_coords = np.meshgrid(np.arange(height), np.arange(width),
                                     indexing='ij')   #Matrix indexing

#For each pixel coordinate add respective flow vector to transform
from skimage.transform import warp
image1_warp = warp(offset_image, np.array([(row_coords + flow_y), (col_coords + flow_x)]),
                   mode='nearest')


from matplotlib import pyplot as plt
fig = plt.figure(figsize=(16, 16))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(image, cmap='gray')
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(offset_image, cmap='gray')
ax2.title.set_text('Offset image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(corrected_image, cmap='gray')
ax3.title.set_text('Pixel Corrected')
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(image1_warp, cmap='gray')
ax4.title.set_text('Flow Corrected')
plt.show()


##################################################