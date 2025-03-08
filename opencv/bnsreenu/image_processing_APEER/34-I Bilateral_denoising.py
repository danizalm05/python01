"""
34 -  - Bilateral filter for image denoising

Edge preserveing filter for image denoising
 https://www.youtube.com/watch?v=CQPZhAVHsXg&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=35
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial34_denoising_using_bilateral.py

cv2.cv2.bilateralFilter - https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
skimage bilateral - https://scikit-image.org/docs/dev/auto_examples/filters/plot_denoise.html

https://people.csail.mit.edu/sparis/bf_course/course_notes.pdf
Bilateral is slow and not very efficient at salt and pepper
"""
 
import cv2
import getpass
import os
import cv2
from skimage import io, img_as_float
from skimage.filters import gaussian


USER = getpass.getuser()

IMAGE_NAME = 'Osteosarcoma_01_25Sigma_noise.tif' #'2.jpg' 'lena.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

print(IMAGE)
path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  # iterate through each file to perform some action
    print(image)


import cv2

img_gaussian_noise = cv2.imread(IMAGE, 0)
#img_salt_pepper_noise = cv2.imread('images/Osteosarcoma_01_8bit_salt_pepper.tif', 0)

img = img_gaussian_noise
img_gaussian_noise = img_as_float(io.imread(IMAGE, as_gray=True))
img_salt_pepper_noise = img_as_float(io.imread(IMAGE, as_gray=True))


bilateral_using_cv2 = cv2.bilateralFilter(img, 5, 20, 100, borderType=cv2.BORDER_CONSTANT)

#  (img, d, sigmaCOlor, sigmaSpace, borderType=)
#d -   diameter of each pixel neighborhood used during filtering
# sigmaCOlor -   Sigma of grey/color space.
#sigmaSpace -   Large value means farther pixels influence each other
#                  (as long as the colors are close enough)

from skimage.restoration import denoise_bilateral

#This is a very slow filter it may take 5 minutes
#bilateral_using_skimage = denoise_bilateral(img, sigma_color=0.05, sigma_spatial=15,
#                multichannel=False)

#sigma_color = float - Sigma for grey or color value.
#For large sigma_color values the filter becomes closer to gaussian blur.
#sigma_spatial: float. Standard ev. for range distance. Increasing this smooths larger features.



cv2.imshow("Original", img)
cv2.imshow("cv2 bilateral", bilateral_using_cv2)
#cv2.imshow("Using skimage bilateral", bilateral_using_skimage)

cv2.waitKey(0)
cv2.destroyAllWindows()