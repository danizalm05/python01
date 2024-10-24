"""
tutorial 31 - image_sharpening_using_unsharp_mask.py

https://www.youtube.com/watch?v=_p_36DIJMIw&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=32
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial31_image_sharpening_using_unsharp_mask.py
"""
from skimage.util import img_as_float

"""
Unsharp mask enhances edges by subtracting an unsharp (smoothed) version of 
the image from the original.
Effectively making the filter a high pass filter. 

enhanced image = original + amount * (original - blurred)

Amount of sharpening can be controlled via scaling factor,
 a multiplication factor
for the sharpened signal. 

skimage uses Gaussian smoothing for image blurring therefore the radius 
parameter in the unsharp masking filter refers to the sigma parameter of the 
gaussian filter.
"""
#This code shows that unsharp is nothing but original + amount *(original-blurred)
from skimage import io  #, img_as_float #skimage.util.img_as_float.
from skimage.filters import unsharp_mask
from skimage.filters import gaussian
import cv2
import getpass
import os

USER = getpass.getuser()

IMAGE_NAME = 'lena.jpg' #'2.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

print(IMAGE)
path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  # iterate through each file to perform some action
    print(image)

#  Manuel  version enhanced image = original + amount * (original - blurred)
img = img_as_float(io.imread(IMAGE, as_gray=True))
resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
gaussian_img = gaussian(img, sigma=2, mode='constant', cval=0.0)
amount = 2
img2 = (img - gaussian_img)* amount
img3 = img + img2
cv2.imshow("original", img)
cv2.imshow("amount = 2", img3)

amount = 4
img2 = (img - gaussian_img)* amount
img3 = img + img2
cv2.imshow("amount = 4", img3)
#

#Autmatic version

#Radius defines the degree of blurring
#Amount defines the multiplication factor for original - blurred image
unsharped_img = unsharp_mask(img, radius=3, amount=2)

cv2.imshow("unsharped_img", unsharped_img)

cv2.waitKey(0)

cv2.destroyAllWindows()



