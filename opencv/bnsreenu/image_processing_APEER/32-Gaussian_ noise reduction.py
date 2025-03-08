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
import cv2
from skimage import io, img_as_float
from skimage.filters import gaussian


USER = getpass.getuser()

IMAGE_NAME = '2.jpg' #'2.jpg' 'lena.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

print(IMAGE)
path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  # iterate through each file to perform some action
    print(image)

img_gaussian_noise = img_as_float(io.imread(IMAGE, as_gray=True))
img_salt_pepper_noise = img_as_float(io.imread(IMAGE, as_gray=True))

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




