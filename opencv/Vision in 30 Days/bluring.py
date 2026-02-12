'''
                                 Color Spaces
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=3099 
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=3528
https://github.com/jasmcaus/opencv-course/blob/master/Section%20%232%20-%20Advanced/blurring.py
https://docs.opencv.org/4.x/
https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html#autotoc_md1369
'''

import cv2 as cv
#import sys
import getpass

img='cat.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
path = BASE_FOLDER+img
print("Image  = ",path) 
print("Image  shape  = ",path) 



import numpy as np
 
from matplotlib import pyplot as plt
 
img = cv.imread(path)
assert img is not None, "file could not be read, check with os.path.exists()"
 
k_size = 7

# Averaging
average = cv.blur(img, (k_size,k_size ))


kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
 
plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.subplot(232),plt.imshow(average),plt.title('average')
 
plt.subplot(236),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
 

cv.imshow("Display window", img)
cv.imshow(" average" , average)
cv.waitKey(0)
cv.destroyAllWindows() 
 
 
