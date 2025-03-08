"""
34 -  - Bilateral filter for image denoising
 
https://www.youtube.com/watch?v=CQPZhAVHsXg&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=35
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial34_denoising_using_bilateral.py

images
https://github.com/bnsreenu/python_for_image_processing_APEER/tree/master/images
cv2.cv2.bilateralFilter - https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
skimage bilateral - https://scikit-image.org/docs/dev/auto_examples/filters/plot_denoise.html

https://people.csail.mit.edu/sparis/bf_course/course_notes.pdf

Bilateral is slow and not very efficient at salt and 
pepper 

"""
 
import cv2
import getpass
import os
import cv2
from skimage.filters import median


USER = getpass.getuser()

IMAGE_NAME = '2.jpg' #'2.jpg' 'lena.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

print(IMAGE)
path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  # iterate through each file to perform some action
    print(image)

 