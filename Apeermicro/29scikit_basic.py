#!/usr/bin/env python
'''

Apeer_micro
Dr Sreenivas Bhattiprolu
quick overview of scikit-image using basic image processing examples.
https://www.youtube.com/watch?v=mQkcf8kgit8&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=30
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial29_image_processing_using_scikit-image.py
'''

from PIL import Image
import getpass
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean


BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
     # "modrain.jpg"#"grains.jpg" #

mimg = "p1.jpg"
path = BASE_FOLDER + mimg






img0 = io.imread(path )
print (img0.shape)#This is a color image (900, 675, 3)
print (type(img0))  #  <class 'numpy.ndarray'>
print (format(img0))#each pixel 3 numbers (integer)
img = io.imread(path, as_gray=True)
print (img.shape)#(900, 675) this is a gray  image
print (type(img))#<class 'numpy.ndarray'>
print (format(img))#float number

#Rescale, resize image by a given factor. While rescaling image
#gaussian smoothing can performed to avoid anti aliasing artifacts.
img_rescaled = rescale(img, 1.0 / 4.0, anti_aliasing=False)
plt.imshow(img, cmap='gray')
plt.show()
plt.imshow(img_rescaled, cmap='gray')
plt.show()

#Resize, resize image to given dimensions (shape)
img_resized = resize(img, (200, 200),               #Check dimensions in variable explorer
                     anti_aliasing=True)

#Downscale, downsample using local mean of elements of each block defined by user
img_downscaled = downscale_local_mean(img, (14, 3))
plt.imshow(img_downscaled)
plt.show()


################################################

#A quick look at a few skimage functions
from skimage import io
from skimage.filters import gaussian, sobel
img = io.imread(path)
plt.imshow(img)
gaussian_using_skimage = gaussian(img, sigma=1, mode='constant', cval=0.0)
plt.imshow(gaussian_using_skimage)

img_gray = io.imread(BASE_FOLDER + "moon.tif", as_gray=True)
sobel_img = sobel(img_gray)  #Works only on 2D (gray) images
plt.imshow(sobel_img, cmap='gray')
plt.show()