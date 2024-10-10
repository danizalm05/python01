"""
tutorial26 plotting using_pyplots python
5:40
https://www.youtube.com/watch?v=67ylv7ldPj0&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=27
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial26_plotting_using_pyplots_python.py
"""
#

import matplotlib.pyplot as plt
import numpy as np
import cv2
import getpass

USER = getpass.getuser()

IMAGE_NAME = '1.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

# PLot using lists


x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)  # plot takes any number of arguments
#plt.show()
#Also understands numpy arrays

a = np.array(x)
b = np.array(y)
plt.plot(a, b)
plt.show()

#Images can also be plotted (covered in viewing images tutorial)
#Images are numpy arrays

gray_img = cv2.imread(IMAGE, 0)

plt.imshow(gray_img, cmap="gray")
plt.show()
plt.hist(gray_img.flat, bins=100, range=(0, 150))
plt.show()