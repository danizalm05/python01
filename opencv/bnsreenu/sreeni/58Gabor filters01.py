"""
 
 DigitalSreeni
 python_for_microscopists/058-ML_06_03_what is gabor filter.py 
https://www.youtube.com/watch?v=QEz4bG9P3Qs&list=PLZsOBAyNTZwbIjGnolFydAN33gyyGP7lT&index=59

https://github.com/bnsreenu/python_for_microscopists
 
images:
 
opencv docs
https://docs.opencv.org/master/db/d27/tutorial_py_table_of_contents_feature2d.html
Brute-Force Matching with ORB Descriptors
"""
 
import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests

import getpass
def empty(a):
    pass

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
     # "modrain.jpg"#"grains.jpg" #

path1 = BASE_FOLDER + 'synthetic.jpg' #"monkey_distorted.jpg" 'synthetic.jpg'
path2 = BASE_FOLDER + "lena.png"# "1.jpg"#"monkey.jpg" BSE_Image.jpg
img = cv2.imread(path1)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h_mask, w_mask = img.shape[:2]
"""
For image processing and computer vision, Gabor filters are generally 
used in texture analysis, edge detection, feature extraction, etc. 
Gabor filters are special classes of bandpass filters, i.e., they allow a certain 
‘band’ of frequencies and reject the others.
ksize Size of the filter returned.
sigma Standard deviation of the gaussian envelope.
theta Orientation of the normal to the parallel stripes of a Gabor function.
lambda Wavelength of the sinusoidal factor.
gamma Spatial aspect ratio.
psi Phase offset.
ktype Type of filter coefficients. It can be CV_32F or CV_64F.
indicates the type and range of values that each pixel in the Gabor kernel can hold.
Basically float32 or float64
"""

phi = 0  #Phase offset. I leave it to 0. 

cv2.namedWindow("Gabor")
cv2.resizeWindow("Gabor",640,340)
cv2.createTrackbar("ksize", "Gabor", 3, 50, empty)## Large may not be good.
cv2.createTrackbar("sigma", "Gabor", 3, 50, empty)#Large sigma on small features will fully miss the features.
cv2.createTrackbar("theta", "Gabor", 0, 628, empty)# 0 : 2PI   628/100
# theta pi/4 shows horizontal pi3/4 shows other horizontal. Try other contributi
cv2.createTrackbar("lamda", "Gabor", 1, 628, empty)
cv2.createTrackbar("gamma", "Gabor", 0, 100, empty)
 #Value of 1 defines spherical. Calue close to 0 has high aspect ratio
cv2.createTrackbar("resiz", "Gabor", 1, 5, empty)
while True:
  ksize = cv2.getTrackbarPos("ksize", "Gabor")
  sigma = cv2.getTrackbarPos("sigma", "Gabor")
  theta = cv2.getTrackbarPos("theta", "Gabor")/100
  lamda = cv2.getTrackbarPos("lamda", "Gabor")/100
  gamma = cv2.getTrackbarPos("gamma", "Gabor")/100
  resize = cv2.getTrackbarPos("resiz", "Gabor")
  kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
  plt.imshow(kernel)
  print("sigma =",sigma, " theta = ",theta," lamda = ",lamda," gamma = ",gamma)
  fimg = cv2.filter2D(img, cv2.CV_8UC3, kernel)
  resize_fimg= cv2.resize(fimg, (resize*h_mask, resize*w_mask))

  kernel_resized = cv2.resize(kernel, (400, 400))   # Resize image
  cv2.imshow('Kernel', kernel_resized)
 
  cv2.imshow('Original Img.', img)
  cv2.imshow('Filtered', resize_fimg)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break


cv2.destroyAllWindows()
