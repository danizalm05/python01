'''
read image with 'skimage'
 filters.gaussian
 
 
 https://www.youtube.com/watch?v=wLYdpcOxyWA&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=4
 https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial04_appreciating%20the%20simplicity%20of%20python.py
'''
import cv2 as cv
import glob
import os
from PIL import Image
from skimage import io, filters
from matplotlib import pyplot as plt
 

# C:\Users\rockman\Anaconda3\envs\tensorflow
USER1 = 'gilfm'
USER2 = 'rockman'
IMAGE_NAME = '1.jpg'
BASE_FOLDER = 'C:/Users/' + USER2 + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME
# Video Playlist: https://www.youtube.com/playlist?list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG

img = io.imread(IMAGE)

gaussian_img = filters.gaussian(img, sigma=1)
plt.imshow(gaussian_img)
plt.show()
print("image = ",IMAGE)