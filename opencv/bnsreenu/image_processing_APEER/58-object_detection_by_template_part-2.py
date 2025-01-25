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
####----------------------------
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
plt.imshow(res, cmap='gray')

threshold = 0.8 #Pick only values above 0.8. For TM_CCOEFF_NORMED, larger values = good fit.

loc = np.where( res >= threshold)  
#Outputs 2 arrays. Combine these arrays to get x,y coordinates - take x from one array and y from the other.

#Reminder: ZIP function is an iterator of tuples where first item in each iterator is paired together,
#then the second item and then third, etc. 

for pt in zip(*loc[::-1]):   #-1 to swap the values as we assign x and y coordinate to draw the rectangle. 
    #Draw rectangle around each object. We know the top left (pt), draw rectangle to match the size of the template image.
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)  #Red rectangles with thickness 2. 

cv2.imshow("Matched image", img_rgb)
cv2.waitKey()
cv2.destroyAllWindows()
 
#============================   Output  ===============================   

fig = plt.figure(figsize=(16, 16))
plt.subplots_adjust ( hspace=0.6)

 
ax1 = fig.add_subplot(4,3,1)
ax1.imshow(image)#  , cmap='gray')
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
ax6.imshow(img_rgb, cmap='gray')
ax6.title.set_text('finl')

 
ax7 = fig.add_subplot(4,3,7)
ax7.imshow( res , cmap='gray')
ax7.title.set_text('cv2.TM_CCOEFF_NORMED')

 
plt.show()
 