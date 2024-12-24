"""
  54-scratch_assay_in_python.py
 -----------------------------------------------------
https://www.youtube.com/watch?v=B_2-SeDZkhU&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=55 
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial54-scratch_assay_in_python.py


Scratch Assay single image segmentation

the input images are here:

https://github.com/eyadgad/Image-Processing-and-Analysis-of-the-Scratch-Assay/tree/main
"""


import matplotlib.pyplot as plt
from skimage import io
from skimage.filters.rank import entropy
from skimage.morphology import disk
import numpy as np
from skimage.filters import threshold_otsu

import getpass



USER = getpass.getuser()
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE_NAME_1 = 'scratch0.jpg'  # '2.jpg' 'lena.jpg' 'scratch0.tif'  'Osteosarcoma_01_transl.tif'
#IMAGE_NAME_1 =   '2.jpg' 

IMAGE1 = BASE_FOLDER + IMAGE_NAME_1

print(IMAGE1)

#img = cv2.imread(IMAGE1 , 0)#read as gray

img = io.imread(IMAGE1 , as_gray=True)


plt.imshow(img, cmap='gray')
plt.show()
#plt.hist(img.flat, bins=100, range=(100,255))
#plt.show()

#Use glob to extract image names and load them. 
import glob

time = 0
scale = 0.45 # microns/pixel
time_list=[]
area_list=[]
path = "images/scratch_assay/*.*" 

#Put the code from single image segmentation in af for loop
i=0
# to apply segmentaion to all images
for file in glob.glob(path):
    print(i) 
    img=io.imread(file)
    i  +=1
    
    entropy_img = entropy(img, disk(3))
    thresh = threshold_otsu(entropy_img)
    binary = entropy_img <= thresh
    scratch_area = np.sum(binary == 1)
    scratch_area = scratch_area*((scale)**2)  #Convert to microns from pixel units
    print("time=", time, "hr  ", "Scratch area=", scratch_area, "um\N{SUPERSCRIPT TWO}")
    time_list.append(time)
    area_list.append(scratch_area)
    time += 1

#print(time_list, area_list)
plt.plot(time_list, area_list, 'bo')  #Print blue dots scatter plot

#Print slope, intercept
from scipy.stats import linregress #Linear regression
#print(linregress(time_list, area_list))

slope, intercept, r_value, p_value, std_err = linregress(time_list, area_list)
print("y = ",slope, "x", " + ", intercept  )
print("R\N{SUPERSCRIPT TWO} = ", r_value**2)
#print("r-squared: %f" % r_value**2)
 
fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

ax1 = fig.add_subplot(3,3,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(3,3,2)
ax2.imshow( entropy_img , cmap='gray')
ax2.title.set_text(' entropy_img')

ax3 = fig.add_subplot(3,3,3)

ax3.hist(img.flat, bins=100, range=(0,255))
ax3.title.set_text('hist color range 100,255')

ax4 = fig.add_subplot(3,3,4)
ax4.imshow(binary, cmap='gray')
ax4.title.set_text('binary')


ax5 = fig.add_subplot(3,3,5)
ax5.imshow(img)
ax5.title.set_text('Entropy')



ax6 = fig.add_subplot(3,3,6)
plt.hist(img.flat, bins=100, range=(0,5))
#ax6.imshow(img, cmap='gray')
ax6.title.set_text('entropy hist')

ax7 = fig.add_subplot(3,3,7)
ax7.imshow(img, cmap='gray')
ax7.title.set_text('binarize entropy image')

plt.show()
 