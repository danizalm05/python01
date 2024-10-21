'''
https://medium.com/ntust-aivc/opencv-fourier-transform-d9811aaac2d5


'''


import cv2
import numpy as np

import os
import getpass




USER = getpass.getuser()
IMAGE_NAME = 'lena.jpg' #'2.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME



# now we will be loading the image and converting it to grayscale
image = cv2.imread(IMAGE)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.imshow('Original', image)




f = np.fft.fft2(image)
fs = np.fft.fftshift(f)
lfs = 15 * np.log(1 + np.abs(fs))
lfs[0:562,  0: 648] = 55
cv2.imshow("dft:", np.uint8(lfs))


ishift_img = np.fft.ifftshift(fs)
ifft_img = np.fft.ifft2(ishift_img)
abs_img = np.abs(ifft_img)
cv2.imshow("idft:",np.uint8(abs_img))
cv2.waitKey(0)


cv2.waitKey(0)
cv2.destroyAllWindows()