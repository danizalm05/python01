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
#img = cv2.imread(IMAGE,cv2.IMREAD_UNCHANGED)

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

 

cv2.waitKey(0)          
  
cv2.destroyAllWindows()


#

#Autmatic version

#Radius defines the degree of blurring
#Amount defines the multiplication factor for original - blurred image
unsharped_img32 = unsharp_mask(img, radius=3, amount=2)
unsharped_img42 = unsharp_mask(img, radius=4, amount=2)
unsharped_img34 = unsharp_mask(img, radius=3, amount=4)

#cv2.imshow("unsharped_img32", unsharped_img32)




import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12, 12))

ax1 = fig.add_subplot(3,3,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(3,3,2)
ax2.imshow( unsharped_img32, cmap='gray')
ax2.title.set_text('radius=3, amount=2')

ax3 = fig.add_subplot(3,3,3)
ax3.imshow( unsharped_img42, cmap='gray')
ax3.title.set_text('radius=4, amount=2')

ax4 = fig.add_subplot(3,3,4)
ax4.imshow( unsharped_img34, cmap='gray')
ax4.title.set_text('radius=3, amount=4')

unsharped_img55 = unsharp_mask(img, radius=5, amount=5)
ax5 = fig.add_subplot(3,3,5)
ax5.imshow( unsharped_img55, cmap='gray')
ax5.title.set_text('radius=5, amount=5')
  

unsharped_img57 = unsharp_mask(img, radius=5, amount=7)
ax6 = fig.add_subplot(3,3,6)
ax6.imshow( unsharped_img57, cmap='gray')
ax6.title.set_text('radius=5, amount=5')

plt.show()



