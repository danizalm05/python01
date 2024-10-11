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

plt.imshow(gray_img, cmap="gray")
plt.show()
plt.hist(gray_img.flat, bins=100, range=(0, 255))
#(gray_img.flat will the into image to one demension
plt.show()
wells = ['well1', 'well2', 'well3', 'well4', 'well5']
cells = [80, 62, 88, 110, 90]

plt.bar(wells, cells)
plt.scatter(wells, cells)
plt.plot(wells, cells)
plt.show()


#Defining line properties


a = np.array([1,2,3,4,5])
b = np.array([1,4,9,16,25])

#use setp() to define multiple parameters
fig = plt.plot(a, b, linewidth=5.0)
plt.setp(fig, color='r', linewidth=4.0)
#look at the documentation for more infor on setp()
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp
plt.show()

wells = [1,2,3,4,5]
cells = [80, 62, 88, 110, 90]

plt.figure(figsize=(8, 8))
plt.bar(wells, cells)
plt.xlabel('Well #', fontsize=18, color='red')
plt.ylabel('# dead cells')
plt.title('Dead cells in each well')
plt.axis([1, 6, 60, 120])   #xmin, xmax, ymin, ymax
plt.grid(True)
plt.show()

############################
#Log scale

y = [10, 125, 1350, 11250, 100500]

plt.figure(figsize=(12, 6))

# linear
plt.subplot(121)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

#Log
plt.subplot(122)
plt.plot(x, y)
plt.yscale('log') #log scale
plt.title('log')
plt.grid(True)
plt.show()

################################
#Use subplots to arrange multiple plots
wells = ['well1', 'well2', 'well3', 'well4', 'well5']
cells = [80, 62, 88, 110, 90]

plt.bar(wells, cells)
plt.scatter(wells, cells)
plt.plot(wells, cells)
#Multiple plots using subplot
#Define a figure size first

#PLotting horizontally
plt.figure(figsize=(16, 6))
#Let us plot in 1 row and 3 columns (13x) x is for the position
plt.subplot(131)
plt.bar(wells, cells)
plt.subplot(132)
plt.scatter(wells, cells)
plt.subplot(133)
plt.plot(wells, cells)
plt.suptitle('Multiple Plots')
plt.show()



wells = ['well1', 'well2', 'well3', 'well4', 'well5']
cells = [80, 62, 88, 110, 90]

# Initialize the plot and sublots
# Initialize the plot
fig = plt.figure(figsize=(16, 6))
ax1 = fig.add_subplot(131)
ax1.set(title='vertical bar', xlabel='Well #', ylabel='# cells')

ax2 = fig.add_subplot(132)
ax1.set(title='horizontal bar', xlabel='Well #', ylabel='# cells')

ax3 = fig.add_subplot(133)

# Plot the data
ax1.bar(wells, cells)
ax2.barh(wells, cells)
ax3.plot(wells, cells)

plt.savefig("my_plot.jpg")  # Save plot
# Show the plot
plt.show()