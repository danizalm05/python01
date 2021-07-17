 #!/usr/bin/env python
'''
26 - Denoising and edge detection using opencv in Python
__author__ = "Sreenivas Bhattiprolu"
www.youtube.com/watch?v=-Qnb8Wv2p1c&list=PLZsOBAyNTZwbIjGnolFydAN33gyyGP7lT&index=27 
https://github.com/bnsreenu/python_for_microscopists/blob/master/026-image_processing_in_openCV_intro1-preprocessing.py
https://github.com/bnsreenu/python_for_microscopists/tree/master/images

BSE_Google_noisy.jpg
https://raw.githubusercontent.com/bnsreenu/python_for_microscopists/master/images/BSE_Google_noisy.jpg


Neuron.jpg 
https://raw.githubusercontent.com/bnsreenu/python_for_microscopists/master/images/Neuron.jpg

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
  
from ImageTable  import  stackImages
USER1 = "gilfm"
USER2 = "rockman"
BASE_FOLDER = 'C:/Users/'+ USER1 +'/Pictures/Saved Pictures/'
# BSE_Google_noisy
# url00 ="raw.githubusercontent.com/bnsreenu/python_for_microscopists/master/images/BSE_Google_noisy.jpg"
img_name = "BSE_Google_noisy.jpg" 
path = BASE_FOLDER + img_name

img = cv2.imread(path,1)# open image  colors 
 
ksize = 3
kernel = np.ones((ksize,ksize),np.float32)/ksize/ksize  
filt_2D = cv2.filter2D(img,-1,kernel)  #Convolution using the kernel we provide  
blur = cv2.blur(img,(ksize,ksize))   #Convolution with a normalized filter. 
blur_gaussian = cv2.GaussianBlur(img,(5,5),0)  #Gaussian kernel is used. 
median_blur = median = cv2.medianBlur(img,5)  #Using kernel size 5. Better on edges compared to gaussian.
bilateral_blur = cv2.bilateralFilter(img,9,75,75)  #Good for noise removal but retain edge sharpness. 



#cv2.imshow("BSE_Google_noisy", img)
#cv2.imshow("filt_2D ", filt_2D)
#cv2.imshow("bilateral_blur ", bilateral_blur)

scale = 0.6
img_array = ([img, filt_2D, blur], [blur_gaussian , median_blur , bilateral_blur])
imgStack = stackImages(scale, img_array)
cv2.imshow("original", imgStack)
cv2.waitKey(0)
cv2.destroyAllWindows() 

#############################################################

#Edge detection:
 
img_name = "Neuron.jpg" 
path = BASE_FOLDER + img_name 
img = cv2.imread(path,0)# open image  gray 
edges = cv2.Canny(img,100,200)   #Image, min and max values

cv2.imshow("Original Image", img)
cv2.imshow("Canny", edges) 
 
cv2.waitKey(0)
cv2.destroyAllWindows() 
 
 


