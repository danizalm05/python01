"""
Tutorial 29 - image_processing using scikit image

https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial29_image_processing_using_scikit-image.py
https://www.youtube.com/watch?v=mQkcf8kgit8&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=30

 resize and rescale.
 edge detection.
 sharpening using deconvolution method
 scratch assay analysis.
#Resize, rescale
"""
import matplotlib.pyplot as plt

from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean
import getpass
import os

USER = getpass.getuser()

IMAGE_NAME = '1.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  # iterate through each file to perform some action
    print(image)

img = io.imread(IMAGE, as_gray=True)
# Rescale, resize image by a given factor.
# gaussian smoothing can be performed to avoid antialiasing artifacts.
img_rescaled = rescale(img, 1.0 / 4.0, anti_aliasing=False)
# Resize, resize image to given dimensions (shape)

plt.imshow( img_rescaled, cmap='gray')


################################################

#A quick look at a few skimage functions

from skimage.filters import gaussian, sobel
#img = io.imread("images/Osteosarcoma_01_25Sigma_noise.tif")
plt.imshow(img)
gaussian_using_skimage = gaussian(img, sigma=1, mode='constant', cval=0.0)
plt.imshow(gaussian_using_skimage)

img_gray = io.imread(IMAGE, as_gray=True)
sobel_img = sobel(img_gray)  #Works only on 2D (gray) images
plt.imshow(sobel_img, cmap='gray')
plt.show()