#!/usr/bin/env python
'''
16:00
Sreenivas Bhattiprolu
105 - What is Fourier Transform?
https://www.youtube.com/watch?v=lzR86lz1Sg8&list=PLZsOBAyNTZwbIjGnolFydAN33gyyGP7lT&index=107

https://github.com/bnsreenu/python_for_microscopists/blob/master/105_what_is_fourier_transform.py'
'''

# https://youtu.be/lzR86lz1Sg8

import cv2
from matplotlib import pyplot as plt
import numpy as np

BASE_FOLDER = 'C:/Users/gilfm/Pictures/Saved Pictures/'
img_name = "lena.png"
path = BASE_FOLDER + img_name
img0 = cv2.imread(path,0)# open image  witg gray colors


#Generate a 2D sine wave image
x = np.arange(256)  # generate 1-D sine wave
y = np.sin(2 * np.pi * x / 30)  #Control the frequency
y += max(y) # offset sine wave by the max value to go out of negative range of sine

# create 2-D array of sine-wave
img = np.array( [ [y[j]*127 for j in range(256)] for i in range(256)] , dtype=np.uint8)
img = np.rot90(img)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# magnitude_spectrum =   20*log [magnitude(dft[real]  dft[imanry]
magnitude_spectrum = 20 * np.log((cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))+1)


#As the spatial frequency increases (bars closer),
#the peaks in the DFT amplitude spectrum move farther away from the origin

fig = plt.figure(figsize=(14, 8))#   8 is width, 14 is height
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img)
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,3)
ax2.imshow(magnitude_spectrum)
ax2.title.set_text('FFT of image')
plt.show()