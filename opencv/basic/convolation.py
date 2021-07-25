# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:41:50 2021
OpenCV with Python By Example/ Prateek Joshi
page 100 - 110
"""
import getpass
import cv2
import matplotlib.pyplot as plt 
import numpy as np 

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
     # "modrain.jpg"#"grains.jpg" #

mimg = "b1.jpg"
path = BASE_FOLDER + mimg
print(path)
img = cv2.imread(path,0)

rows, cols = img.shape[:2]
kernel_identity = np.array([[0,0,0], [0,1,0], [0,0,0]])

kernel_3x3 = np.ones((3,3), np.float32) / 9.0
kernel_5x5 = np.ones((5,5), np.float32) / 25.0

k_identity = cv2.filter2D(img, -1, kernel_identity)
##  value -1 is to maintain source image depth

k_3x3 = cv2.filter2D(img, -1, kernel_3x3)   
k_5x5 = cv2.filter2D(img, -1, kernel_5x5)

#             Edge detection
sobelX_kernel = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
sobelX  = cv2.filter2D(img, -1, sobelX_kernel)

sobelY_kernel = np.array([  [-1, -2, -1], [ 0, 0, 0], [1, 2, 1]  ])
sobelY  = cv2.filter2D(img, -1, sobelY_kernel)

s = sobelX+sobelY
k = cv2.filter2D(s, -1, kernel_5x5)
cv2.imshow("sum", ~k )
# edge drtrction with  sobel  function
sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

#laplacian = horizontal  and vertical edge detection
laplacian = cv2.Laplacian(img, cv2.CV_64F)# A lot of noise
#Canny edge detector
low_threshold = 50
high_threshold = 150
canny = cv2.Canny(img, low_threshold, high_threshold)


# Motion  = averages the pixel values in a particular direction

size = 25
# generating the kernel
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size
# applying the kernel to the input image
motion_blur = cv2.filter2D(img, -1, kernel_motion_blur)

cv2.imshow("original", img)
cv2.imshow("sobelX sobelY", sobelX)
cv2.imshow("sobelY kernel", sobelY)
cv2.imshow("canny", ~canny )


cv2.imshow('Motion Blur', motion_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()




'''


plt.imshow(k_5x5, cmap="gray")
plt.show()
fig, axes = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True,
                         figsize=(8, 8))
ax = axes.ravel()

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title('Original image')

ax[1].imshow(k_identity, cmap=plt.cm.gray)
ax[1].set_title('k_identity')

ax[2].imshow(k_3x3, cmap=plt.cm.gray)
ax[2].set_title('k_3x3')

ax[3].imshow(k_5x5, cmap=plt.cm.gray)
ax[3].set_title('k_5x5')

for a in ax:
    a.axis('off')

#plt.tight_layout()
plt.show()
'''