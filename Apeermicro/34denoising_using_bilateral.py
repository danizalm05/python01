# -*- coding: utf-8 -*-
"""
34denoising_using_bilateral.py
https://www.youtube.com/watch?v=CQPZhAVHsXg&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=35

Apeer_micro
list: https://www.youtube.com/playlist?list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG
https://people.csail.mit.edu/sparis/bf_course/course_notes.pdf
Bilateral is  good at preserving  edges
"""

import getpass 
from skimage.filters import median
import cv2
from skimage import io, img_as_float
from skimage.restoration import denoise_bilateral
 
BASE_FOLDER = 'C:/Users/' + getpass.getuser() +'/Pictures/Saved Pictures/'
path1 = BASE_FOLDER + "Osteosarcoma_01_25Sigma_noise.tif"
path2 = BASE_FOLDER + "Osteosarcoma_01_8bit_salt_pepper.tif"


img_gaussian_noise = cv2.imread(path1, 0)# 0 gray color
img_salt_pepper_noise = cv2.imread(path2, 0)

img = img_salt_pepper_noise
#3:44

d =5 # diameter of the pixel neighborhood.
sigmaColor = 20 #Sigma of grey/color space.
sigmaSpace = 100 #Large value means farther pixels influence
borderType=cv2.BORDER_CONSTANT

bilateral_using_cv2 =  cv2.bilateralFilter(img,
                            d, sigmaColor, sigmaSpace, borderType)

# Same thing  with skimage
# This process  is very long up to 5  mints
#bilateral_using_skimage = denoise_bilateral(img,
 #        sigma_color=0.05, sigma_spatial=15, multichannel=False)

#sigma_color = float - Sigma for grey or color value.
#For large sigma_color values the filter becomes closer to gaussian blur.
#sigma_spatial: float. Standard ev. for range distance. Increasing this smooths larger features.



cv2.imshow("Original", img)
cv2.imshow("cv2 bilateral", bilateral_using_cv2)

cv2.waitKey(0)
cv2.destroyAllWindows()