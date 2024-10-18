import cv2
import numpy as np

import matplotlib.pyplot as plt

import getpass
import os

USER = getpass.getuser()

IMAGE_NAME = 'lena.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

# now we will be loading the image and converting it to grayscale
image = cv2.imread(IMAGE)



# single chanel image
img = np.random.random((100, 100))
img = plt.imread(IMAGE)[:,:,0]

# should be only width and height
print(img.shape)

# do the 2D fourier transform
fft_img = np.fft.fft2(img)

# shift FFT to the center
fft_img_shift = np.fft.fftshift(fft_img)

# extract real and phases
real = fft_img_shift.real
phases = fft_img_shift.imag

# modify real part, put your modification here
real_mod = real/3

# create an empty complex array with the shape of the input image
fft_img_shift_mod = np.empty(real.shape, dtype=complex)

# insert real and phases to the new file
fft_img_shift_mod.real = real_mod
fft_img_shift_mod.imag = phases

# reverse shift
fft_img_mod = np.fft.ifftshift(fft_img_shift_mod)

# reverse the 2D fourier transform
img_mod = np.fft.ifft2(fft_img_mod)

# using np.abs gives the scalar value of the complex number
# with img_mod.real gives only real part. Not sure which is proper
img_mod = np.abs(img_mod)

# show differences
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.subplot(122)
plt.imshow(img_mod, cmap='gray')
plt.show() 