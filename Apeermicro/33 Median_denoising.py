# -*- coding: utf-8 -*-
"""
 
https://github.com/bnsreenu/python_for_image_processing_APEER
https://www.youtube.com/watch?v=g-1bTTNOZa0&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=33 
Osteosarcoma_01_25Sigma_noise.tif
Osteosarcoma_01_8bit_salt_pepper.tif
########
v2.medianBlur - https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
skimage.filters.median - https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.median
See how median is much better at cleaning salt and pepper noise compared to Gaussian 
"""

import getpass 
from skimage.filters import median
import cv2
from skimage import io, img_as_float
 
 
BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
path1 = BASE_FOLDER + "Osteosarcoma_01_25Sigma_noise.tif"
path2 = BASE_FOLDER +"Osteosarcoma_01_8bit_salt_pepper.tif"


#Needs 8 bit, not float.
img_gaussian_noise = cv2.imread(path1, 0)# 0 gray color
img_salt_pepper_noise = cv2.imread(path2, 0)

img = img_salt_pepper_noise

median_using_cv2 = cv2.medianBlur(img, 3) 


from skimage.morphology import disk  
#Disk creates a circular structuring element, similar to a mask with specific radius
median_using_skimage = median(img, disk(3), mode='constant', cval=0.0)
  
cv2.imshow("Original", img)
cv2.imshow("cv2 median", median_using_cv2)
cv2.imshow("Using skimage median", median_using_skimage)

cv2.waitKey(0)
cv2.destroyAllWindows()