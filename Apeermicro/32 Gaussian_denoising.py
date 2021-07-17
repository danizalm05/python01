'''
Tutorial 32 - Image filtering in python - Gaussian denoising for noise reduction
https://www.youtube.com/playlist?list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG
https://www.youtube.com/watch?v=g-1bTTNOZa0&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=33 
https://github.com/bnsreenu/python_for_image_processing_APEER/tree/master/images
Osteosarcoma_01_8bit_salt_pepper.tif
Osteosarcoma_01_25Sigma_noise.tif
'''
 

from matplotlib import pyplot as plt
import numpy as np
import getpass
import cv2
from skimage import io, img_as_float
from skimage.filters import gaussian
 

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'



path1 = BASE_FOLDER + "Osteosarcoma_01_25Sigma_noise.tif"
path2 = BASE_FOLDER +"Osteosarcoma_01_8bit_salt_pepper.tif"

img_gaussian_noise = img_as_float(io.imread(path1, as_gray=True))
img_salt_pepper_noise = img_as_float(io.imread(path2, as_gray=True))

img = img_gaussian_noise

gaussian_using_cv2 = cv2.GaussianBlur(img, (3,3), 0, borderType=cv2.BORDER_CONSTANT)

gaussian_using_skimage = gaussian(img, sigma=1, mode='constant', cval=0.0)
#sigma defines the std dev of the gaussian kernel. SLightly different than
#how we define in cv2
 
cv2.imshow("Original", img)
cv2.imshow("Using cv2 gaussian", gaussian_using_cv2)
cv2.imshow("Using skimage", gaussian_using_skimage)
#cv2.imshow("Using scipy2", conv_using_scipy2)


cv2.waitKey(0)
cv2.destroyAllWindows()
'''
print(path1)  
print(path2) 
 
img1 = cv.imread(path1, 1)
img2 = cv.imread(path1, 1)
cv.imshow('Original', img1)
cv.waitKey(0)
plt.imshow(img1)
plt.show() 
plt.hist(img1.flat, bins=100, range=(0,250))#.flat turn to 1 dimantion
plt.show()
'''