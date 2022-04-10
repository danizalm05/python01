
"""
 
OpenCV with Python By Example/ Prateek Joshi
page 110 120
"""
import getpass
import cv2
import matplotlib.pyplot as plt 
import numpy as np 

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
     # "modrain.jpg"#"grains.jpg" "b1.jpg"#

mimg ="bb.jpg"
path = BASE_FOLDER + mimg
print(path)
img = cv2.imread(path,1)

rows, cols = img.shape[:2]
# generating the kernels
kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                             [-1,2,2,2,-1],
                             [-1,2,8,2,-1],
                             [-1,2,2,2,-1],
                             [-1,-1,-1,-1,-1]]) / 8.0

# applying different kernels to the input image
output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)

cv2.imshow('Sharpening', output_1)
cv2.imshow('Excessive Sharpening', output_2)
cv2.imshow('Edge Enhancement', output_3)
cv2.imshow('Original', img)

kernel_emboss_1 = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])
kernel_emboss_2 = np.array([[-1,-1,0],
                            [-1,0,1],
                            [0,1,1]])
kernel_emboss_3 = np.array([[1,0,0],
                            [0,0,0],
                            [0,0,-1]])

# converting the image to grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# applying the kernels to the grayscale image and adding the offset to produce the shadow
output_1 = cv2.filter2D(gray_img, -1, kernel_emboss_1) + 128
output_2 = cv2.filter2D(gray_img, -1, kernel_emboss_2) + 128
output_3 = cv2.filter2D(gray_img, -1, kernel_emboss_3) + 128


cv2.imshow('Embossing - South West', output_1)
cv2.imshow('Embossing - South East', output_2)
cv2.imshow('Embossing - North West', output_3)


kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=3)
img_dilation = cv2.dilate(img, kernel, iterations=3)


cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

'''
Erosion = strips out the outermost layer of pixels in a structure. darker
Dilation = adds an extra layer of pixels on a structure.

'''

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