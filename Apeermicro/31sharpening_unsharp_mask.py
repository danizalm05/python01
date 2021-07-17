'''
Apeer_micro
Dr Sreenivas Bhattiprolu
https://twitter.com/digitalsreeni

Tutorial 30 - Basic image processing using opencv.
https://www.youtube.com/watch?v=_p_36DIJMIw&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=32
Apeer_micro
Dr Sreenivas Bhattiprolu
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial31_image_sharpening_using_unsharp_mask.pyVideo Playlist:
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/images/sandstone_blur_2sigma.tif
"""
Unsharp mask enhances edges by subtracting an unsharp (smoothed) version of the
image from the original.
Effectively making the filter a high pass filter.
enhanced image = original + amount * (original - blurred)
Amount of sharpening can be controlled via scaling factor, a multiplication factor
for the sharpened signal.
skimage uses Gaussian smoothing for image blurring therefore the radius parameter
in the unsharp masking filter refers to the sigma parameter of the gaussian filter.
"""
'''


from matplotlib import pyplot as plt
from skimage import io, img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian
import cv2
import getpass

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
     # "modrain.jpg"#"grains.jpg" #

path = BASE_FOLDER + 'sandstone_blur_2sigma.tif'
print(path)




img = img_as_float(io.imread(path, as_gray=True))

gaussian_img = gaussian(img, sigma=2, mode='constant', cval=0.0)

img2 = (img - gaussian_img)*2.

img3 = img + img2

plt.imshow(img2, cmap="gray")

plt.show()


#Radius defines the degree of blurring
#Amount defines the multiplication factor for original - blurred image
unsharped_img = unsharp_mask(img, radius=3, amount=2)

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(1,3,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(1,3,2)
ax2.imshow(unsharped_img, cmap='gray')
ax2.title.set_text('Unsharped Image')

ax3 = fig.add_subplot(1,3,3)
ax3.imshow(img2, cmap='gray')
ax3.title.set_text('(img - gaussian_img)*2')

plt.show()