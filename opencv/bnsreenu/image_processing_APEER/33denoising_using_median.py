"""
33 - Image filtering in python - Median filter for denoising images
 
https://www.youtube.com/watch?v=MTaCVDll9Iw&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=34
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial33_denoising_using_median.py

Why Median denoising filter is better at removing salt
 and pepper noise. 

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



#Needs 8 bit, not float.
img_gaussian_noise = cv2.imread(IMAGE, 0)
img_salt_pepper_noise = cv2.imread(IMAGE, 0)

img = img_salt_pepper_noise


median_using_cv2 = cv2.medianBlur(img, 3)

from skimage.morphology import disk  
#Disk creates a circular structuring element, similar to a mask with specific radius
median_using_skimage = median(img, disk(3), mode='constant', cval=0.0)


cv2.imshow("Original", img)
cv2.imshow("cv2 median", median_using_cv2)
cv2.imshow("Using skimage median", median_using_skimage)

cv2.waitKey(0)          
cv2.destroyAllWindows() 
