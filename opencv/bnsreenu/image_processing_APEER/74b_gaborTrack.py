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

Gabor1 : theta= 0.0 : sigma= 1 : lamda= 0.0 : gamma= 0.05

Gabor253 : theta= 5.497787143782138 : sigma= 7 : lamda= 1.5707963267948966 : gamma= 0.05
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


#Display Group of images in one window
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
    







img = cv2.imread(IMAGE)#Gray image
#plt.imshow(img)

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

def empty(a):
    pass
 
wname = 'image'
cv2.namedWindow(wname)
 
# create trackbars 
cv2.createTrackbar('scale',wname,0,10,empty)
  
cv2.createTrackbar('ksize',wname,6,5,empty)
cv2.createTrackbar('theta',wname,1,16,empty)
 
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, wname,0,1,empty)



 
     
while True:
   
    scale = 0.4 + cv2.getTrackbarPos("scale", wname) / 25
    ksize=  cv2.getTrackbarPos("ksize", wname) 
    n_theta=  cv2.getTrackbarPos("theta", wname)  
    theta = n_theta*np.pi/16  #/4 shows horizontal 3/4 shows other horizontal. Try other contributions
   
    kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
    img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Apply the filter
    fimg = cv2.filter2D(img, cv2.CV_8UC3, kernel)

    kernel_resized = cv2.resize(kernel, (400, 400)) 
    
    ##  Display
    imgStack = stackImages( scale,  ([img,kernel ],[fimg,kernel_resized ])    )
  
    cv2.imshow("kernel", imgStack)
    cv2.imshow("Result", fimg)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()

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
plt.show()

 