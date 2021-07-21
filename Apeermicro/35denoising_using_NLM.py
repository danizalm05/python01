# -*- coding: utf-8 -*-
"""
35 denoising_using_nlm.py
Apeer_micro
 www.youtube.com/watch?v=3-53P4zUkZQ&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=36

Works well for random gaussian noise but not as good for salt
and pepper

The non-local means algorithm replaces the value of a pixel by
an average  of a selection of other pixels values: small patches
centered on the other  pixels are compared to the patch centered on
the pixel of interest, and the  average is performed only for
pixels that have patches close to the current patch.
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


cv2.imshow("Original", img)


cv2.waitKey(0)
cv2.destroyAllWindows()