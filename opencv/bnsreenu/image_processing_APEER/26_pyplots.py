"""
tutorial26 plotting using_pyplots python
11:04
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
plt.plot(a, b, 'bo')  #Blue dots. Also try: 'r--' 'g^' 'bs'
plt.axis([0, 6, 0, 50]) #Define range for x and y axes [xmin, xmax, ymin, ymax] 
 
plt.show()

#Images can also be plotted (covered in viewing images tutorial)
#Images are numpy arrays

gray_img = cv2.imread(IMAGE, 0)

#plt.imshow(gray_img, cmap="gray")
#plt.show()
#plt.hist(gray_img.flat, bins=100, range=(0, 255))
#(gray_img.flat will the into image to one demension
 
wells = ['well1', 'well2', 'well3', 'well4', 'well5']
cells = [80, 62, 88, 110, 90]

plt.bar(wells, cells)
plt.scatter(wells, cells)
plt.plot(wells, cells)
plt.show()


#Defining line properties
from matplotlib import pyplot as plt

import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([1,4,9,16,25])
plt.plot(a, b, linewidth=5.0)
#use setp() to define multiple parameters
fig = plt.plot(a, b, linewidth=5.0)
plt.setp(fig, color='r', linewidth=4.0)
#look at the documentation for more infor on setp()
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp
plt.show()