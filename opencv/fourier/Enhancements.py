"""
Enhancements using Fourier Transform
How to remove unnecessary objects or artifacts in images?

https://medium.com/swlh/image-processing-with-python-fourier-transform-for-digital-images-bc918786e375
"""
import os
import getpass

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2gray



USER = getpass.getuser()
IMAGE_NAME = 'lena.jpg' #'2.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

print(IMAGE)
path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  # iterate through each file to perform some action
    print(image)

cargoship_rgb = imread(IMAGE)
cargoship_gray = rgb2gray(cargoship_rgb)
#plt.imshow(cargoship_gray, cmap='gray')
#plt.title('org Grayscale')


cargoship_fft = np.fft.fftshift(np.fft.fft2(cargoship_gray))
#plt.imshow(np.log(abs(cargoship_fft)), cmap='gray')
#plt.title(' Fourier Transform Representation of the Cargo Ship');

f, axarr = plt.subplots(2,2)
axarr[0,0].imshow(cargoship_rgb)
axarr[0,1].imshow(cargoship_gray, cmap='gray')
axarr[1,0].imshow(np.log(abs(cargoship_fft)), cmap='gray')
axarr[1,1].imshow(cargoship_gray)
axarr[1,1].axis('off')
axarr[1,1].set_title("gray")
plt.subplots_adjust(hspace=0.5)
plt.show()