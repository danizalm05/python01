"""
OpenCV with Python By Example/ Prateek Joshi
Vreate a vignette filter that focuses on the center of the image.
page 123 -129
"""

import cv2
import numpy as np
import getpass

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #
mimg = "bb.jpg"
path = BASE_FOLDER + mimg
print(path)
img = cv2.imread(path,1)# Read  color   image

rows, cols = img.shape[:2]


 
# generating vignette mask  in the middle using Gaussian kernels
#kernel_x = cv2.getGaussianKernel(cols,150)
#kernel_y = cv2.getGaussianKernel(rows,150)


# generating vignette mask  in upper left using Gaussian kernels
kernel_x = cv2.getGaussianKernel(int(1.5*cols),200)
kernel_y = cv2.getGaussianKernel(int(1.5*rows),200)
'''
getGaussianKernel,=standard deviation of the Gaussian 
controls the radius of the bright central region.
'''

kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
mask = mask[int(0.5*rows):, int(0.5*cols):]
# normalizing this kernel and scaling it up

output = np.copy(img)
h =  np.copy(img)
# applying the mask to each channel in the input image 
for i in range(3): 
         output[:,:,i] = output[:,:,i] * mask
         #Equalize   histogram to adjust the contrast
         #Histogram equalization is applicable only grayscale images.
         h[:,:,i] = cv2.equalizeHist( output[:,:,i] )

'''
The above process of Histogram equalization is wrong because
Histogram equalization is a nonlinear process. So, we cannot just separate out
 the three channels in an  RGB image, equalize the histogram separately, 
 and combine them later to form the output  image. 
The concept of histogram equalization is only applicable to the intensity values in the image.
So, we have to make sure not to modify the color information when we do this.
 
In order to handle the histogram equalization of color images, we need to 
convert it to a color space where intensity is separated from the color 
information. 
YUV is a good example of such a color space. 
Once we convert it to YUV, we just need to equalize the Ychannel
and combine it with the other two channels to get the output image.
'''
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)





cv2.imshow('Original', img) 
cv2.imshow('Vignette', output)
cv2.imshow('Wrong Histogram equalization', h)
cv2.imshow('equalize the Y channel', img_output)
cv2.waitKey(0)