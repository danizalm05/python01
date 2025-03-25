"""
 74_what is gabor filter.py
 -----------------------------------------------------

https://www.youtube.com/watch?v=yn1NUwaxhZg&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=76
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial74_what%20is%20gabor%20filter.py
image:
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/images/synthetic.jpg

 
Gabor filters are generally  used in texture analysis, 
edge detection, feature extraction, etc. 
Gabor filters are special classes of bandpass filters,


ksize Size of the filter returned.
sigma Standard deviation of the gaussian envelope.
theta Orientation of the normal to the parallel stripes of a 
Gabor function.
lambda Wavelength of the sinusoidal factor.
gamma Spatial aspect ratio.
psi Phase offset.
ktype Type of filter coefficients. It can be CV_32F or CV_64F.
indicates the type and range of values that each pixel in the Gabor kernel can hold.
Basically float32 or float64
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
 
import getpass
from pathlib import Path
import sys
import os
 

IMAGE_NAME =  'synthetic.jpg' # 'BSE.tif'   'Osteosarcoma_01_transl.tif'  '2.jpg'
USER = getpass.getuser()

if (os.name == "posix"):  #this is a linux  system 
    BASE_FOLDER = "/home/"+USER +'/Pictures/'
    print(BASE_FOLDER)
else: #this is a windows  system 
    BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

# Check if the file exists
if not(Path(IMAGE).exists()):
    msg = "Error: file " + IMAGE +" does not exist"
    sys.exit(msg)
   
img = cv2.imread(IMAGE)#Gray image
plt.imshow(img)

ksize = 5  #Use size that makes sense to the image and fetaure 
#          size. Large may not be good. 
#On the synthetic image it is clear how ksize affects imgae (try 5 and 50)
sigma = 5 #Large sigma on small features will fully miss the features. 
theta = 1*np.pi/2  #/4 shows horizontal 3/4 shows other horizontal. Try other contributions
lamda = 1*np.pi/4  #1/4 works best for angled. 
gamma=0.5  #Value of 1 defines spherical. Calue close to 0 has
#            high aspect ratio
#Value of 1, spherical may not be ideal as it picks up features from other regions.
phi = 1.0  #Phase offset. I leave it to 0. (For hidden pic use 0.8)


kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)

img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Apply the filter
fimg = cv2.filter2D(img, cv2.CV_8UC3, kernel)

kernel_resized = cv2.resize(kernel, (400, 400))                    # Resize image




#plt.imshow(kernel)





#============================   Output  ===============================   

fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

ax1 = fig.add_subplot(4,3,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(4,3,2)
ax2.imshow(kernel)#, cmap='gray')
ax2.title.set_text('kernel')


ax3 = fig.add_subplot(4,3,3)
ax3.hist(img.flat, bins=100, range=(0,255))
ax3.title.set_text('hist color range')
 
ax4 = fig.add_subplot(4,3,4)
ax4.imshow(img_g, cmap='gray')
ax4.title.set_text('Gray color')


ax5 = fig.add_subplot(4,3,5)
ax5.imshow(kernel_resized)#,cmap='gray')
ax5.title.set_text('kernel_resized')



ax6 = fig.add_subplot(4,3,6)
ax6.imshow(fimg )#, cmap='gray')
ax6.title.set_text('result')
'''
ax7 = fig.add_subplot(4,3,7)
ax7.imshow(sure_bg, cmap='gray')
ax7.title.set_text('surebackground')

 

ax8 = fig.add_subplot(4,3,8)
ax8.imshow( sure_fg , cmap='gray')
ax8.title.set_text(' sure_fg ')


ax9 = fig.add_subplot(4,3,9)
ax9.imshow(unknown, cmap='gray')
ax9.title.set_text('unknown')

#
ax10 = fig.add_subplot(4,3,10)
ax10.imshow(markers)#, cmap='gray')
ax10.title.set_text('markers')

 

ax11 = fig.add_subplot(4,3,11)
ax11.imshow(markers10,cmap='gray')
ax11.title.set_text('markers10')

 

ax12 = fig.add_subplot(4,3,12)
ax12.imshow(img2,cmap='gray')
ax12.title.set_text('labels are painted over the image.')

'''
plt.show()
 