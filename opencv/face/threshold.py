'''
OpenCV With Python by Example  page 173
face_hannibal.py

'''
import cv2
import numpy as np
import getpass
import matplotlib.pyplot as plt

qqqqq
img_name = "bb.jpg"#"hickory.jpg"#
BASE_FOLDER = 'C:/Users/' + getpass.getuser() +'/Pictures/Saved Pictures/'
path = BASE_FOLDER + img_name
print(path)

img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h_mask, w_mask = img.shape[:2]
 
thshld=  180
max_value = 255

ret,thresh = cv2.threshold(img, thshld, max_value, cv2.THRESH_BINARY )
ret,bin_inv    = cv2.threshold(gray, thshld, max_value, cv2.THRESH_BINARY_INV)


#print(ret)

bitwiseAnd = cv2.bitwise_not(bin_inv)
bitwiseOr = cv2.bitwise_or(bin_inv, gray)
bitwiseAnd = cv2.bitwise_or(bin_inv, gray)


fig, axes = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True,
                         figsize=(18, 18))
ax = axes.ravel()

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title('Original image')

ax[1].imshow(thresh, cmap=plt.cm.gray)
ax[1].set_title('thresh')

ax[2].imshow(bin_inv, cmap=plt.cm.gray)
ax[2].set_title('THRESH_BINARY_INV')

ax[3].imshow(bitwiseAnd, cmap=plt.cm.gray)
ax[3].set_title('bitwiseAnd')


ax[4].imshow(bitwiseOr, cmap=plt.cm.gray)
ax[4].set_title('bitwiseOr')



for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
