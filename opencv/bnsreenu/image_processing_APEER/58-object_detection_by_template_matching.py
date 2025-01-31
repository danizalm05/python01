"""
 58-object_detection_by_template_matching.py
 -----------------------------------------------------
 https://www.youtube.com/watch?v=PqVH9IHMLss&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=59
 https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial58_object_detection_by_template_matching.py 
 
 https://docs.opencv.org/3.4/d4/dc6/tutorial_py_template_matching.html
 
 images:
   python_for_image_processing_APEER/blob/master/images/Ti_powder.tif
   python_for_image_processing_APEER/blob/master/images/Ti_powder_single.tif

 
Need a source image and a template image.
The template image T is slided over the source image (as in 2D
convolution),  and the program tries to find matches using 
statistics.
Several comparison methods are implemented in OpenCV.
It returns a grayscale image, where each pixel denotes how 
much does the  neighbourhood of that pixel match with template.

Once you got the result, you can use cv2.minMaxLoc() function 
to find where is the maximum/minimum value. Take it as the 
top-left corner of the  rectangle and take (w,h) as width and
 height of the rectangle.  That rectangle can be drawn on the 
 region of matched template.

This progrm will find only  the first match

11:03


"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


import getpass
from pathlib import Path
import sys
USER = getpass.getuser()

IMAGE_NAME = 'Ti_powder.tif'  # 'Osteosarcoma_01_transl.tif'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

# Check if the file exists
if not(Path(IMAGE).exists()):
    msg = "Error: file " + IMAGE +" does not exist"
    sys.exit(msg)
   
image = cv2.imread(IMAGE)#Gray image

img_rgb = cv2.imread(IMAGE)#'images/Ti_powder.tif')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
IMAGE = BASE_FOLDER + 'Ti_powder_single.tif'


template = cv2.imread(IMAGE, 0)# what we are looking for
h, w = template.shape[::] # get hight  and withd

#methods available: ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF)

# For TM_SQDIFF, Good match yields minimum value; bad match yields large values
# For all others it is exactly opposite, max value = good fit.


min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = min_loc  #Change to max_loc for all except for TM_SQDIFF
bottom_right = (top_left[0] + w, top_left[1] + h)
final_results = img_gray
cv2.rectangle(final_results, top_left, bottom_right, 0, 1)  #Black rectangle with thickness 2. 

#cv2.imshow("Matched image", final_results) 
plt.show()
#============================   Output  ===============================   

fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

 
ax1 = fig.add_subplot(4,3,1)
ax1.imshow(img_rgb)#  , cmap='gray')
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(4,3,2)
ax2.imshow(img_gray, cmap='gray')
ax2.title.set_text('img_gray')

ax3 = fig.add_subplot(4,3,3)
ax3.hist(image.flat, bins=100, range=(0,255))
ax3.title.set_text('hist color range')

ax4 = fig.add_subplot(4,3,4)
ax4.imshow(template, cmap='gray')
ax4.title.set_text('template')


ax5 = fig.add_subplot(4,3,5)
ax5.imshow(res)#,cmap='gray')
ax5.title.set_text('res')



ax6 = fig.add_subplot(4,3,6)
ax6.imshow(final_results)#, cmap='gray')
ax6.title.set_text('final_results')

ax7 = fig.add_subplot(4,3,7)
ax7.imshow(image, cmap='gray')
ax7.title.set_text('surebackground')

 

ax8 = fig.add_subplot(4,3,8)
ax8.imshow( image , cmap='gray')
ax8.title.set_text(' sure_fg ')

 
plt.show()
 