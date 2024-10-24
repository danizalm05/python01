"""
32 - Image filtering in python - Gaussian denoising for noise reduction

https://www.youtube.com/watch?v=g-1bTTNOZa0&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=33
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial32_denoising_using_gaussian.py 
 """

"""
cv2.filter2D - https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html?highlight=filter2d#filter2d
cv2.GaussianBlur - https://www.tutorialkart.com/opencv/python/opencv-python-gaussian-image-smoothing/
skimage.filters.gaussian - https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.gaussian 
"""
 
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

 



