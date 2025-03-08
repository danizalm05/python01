"""
40 -  Fourier transform and how is it relevant for image processing?

https://www.youtube.com/watch?v=RVE-CSZijAI&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=41
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial40_what_is_fourier_transform.py

 

 
"""
 
import getpass
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np


USER = getpass.getuser()

IMAGE_NAME = '2.jpg' #'2.jpg' 'lena.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

print(IMAGE)
path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  # iterate through each file to perform some action
    print(image)

#Generate a 2D sine wave image
x = np.arange(256)  # generate values from 0 to 255 (our image size)
y = np.sin(2 * np.pi * x / 3)  #calculate sine of x values
#Divide by a smaller number above to increase the frequency.
y += max(y) # offset sine wave by the max value to go out of negative range of sine 

#Generate a 256x256 image (2D array of the sine wave)
img = np.array([  [y[j]*127 for j in range(256) ] for i in range(256)], dtype=np.uint8) 
# create 2-D array of sine-wave

plt.imshow(img)
#img = np.rot90(img)  #Rotate img by 90 degrees

img = cv2.imread(IMAGE, 0) # load an image

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

#Shift DFT. First check the output without the shift
#Without shifting the data would be centered around origin at the top left
#Shifting it moves the origin to the center of the image. 
dft_shift = np.fft.fftshift(dft)

#Calculate magnitude spectrum from the DFT (Real part and imaginary part)
#Added 1 as we may see 0 values and log of 0 is indeterminate
magnitude_spectrum = 20 * np.log((cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))+1)


#As the spatial frequency increases (bars closer), 
#the peaks in the DFT amplitude spectrum move farther away from the origin

#Center represents low frequency and the corners high frequency (with DFT shift).
#To build high pass filter block center corresponding to low frequencies and let
#high frequencies go through. This is nothing but an edge filter. 

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img)
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
#ax2.imshow(dft)
ax2.title.set_text('dft')

ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img)
ax3.title.set_text('Input Image')
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(magnitude_spectrum)
ax4.title.set_text('FFT of image')

plt.show() 

print('picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}')