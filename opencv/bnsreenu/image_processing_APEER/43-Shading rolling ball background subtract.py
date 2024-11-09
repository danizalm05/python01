"""
43 - Shading correction using rolling ball 
              background subtraction
-----------------------------------------------------
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial43_shading_correction_using_rolling_ball.py
https://www.youtube.com/watch?v=BQ-YrAIl2GU&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=44
Non-uniform illumination results in images with shaded background. The
shading can be linear, from one end (or corner) to the other or it can be
radial. This non-uniform illumination makes digital image analysis difficult
 if not impossible. Rolling ball based background subtraction can be used to
 correct for this effect,
 especially on images with small features and constant background.

1st approach: Perform CLAHE
# Equalize light by performing CLAHE on the Luminance channel
# The equalize part,  covered as aprt of previous tutorials about CLAHE
# This kind of works but you can still see shading after the correction.

2nd approach:
Apply rolling ball background subtraction

pip install opencv-rolling-ball
"""
import cv2
import numpy as np

 


 
import getpass
import os
 

USER = getpass.getuser()

<<<<<<< HEAD
IMAGE_NAME = 'lena.jpg' #'2.jpg' 'lena.jpg'
=======
IMAGE_NAME = 'lena.jpg'  #'2.jpg' 'lena.jpg''Alloy.jpg'
>>>>>>> 8ab4d2cf5e09a310f8ba976fe612bdb6f34e53b0
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

print(IMAGE)

path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  # iterate through each file to perform some action
    print(image)

<<<<<<< HEAD
img = cv2.imread(IMAGE, 1)

"""
=======
img = cv2.imread(IMAGE, 1) # load an image
cv2.imshow("Original image", img)
'''
>>>>>>> 8ab4d2cf5e09a310f8ba976fe612bdb6f34e53b0
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab_img)


clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8,8))
clahe_img = clahe.apply(l)
CLAHE_img = cv2.merge((clahe_img,a,b))

corrected_image = cv2.cvtColor(CLAHE_img, cv2.COLOR_LAB2BGR)

cv2.imshow("Original image", img)
cv2.imshow("Corrected image", corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
<<<<<<< HEAD
"""




#2nd method
# https://pypi.org/project/opencv-rolling-ball/
#
# pip install opencv-rolling-ball
# Only works with 8 bit grey
"""
=======

'''
############################################################
"""
#2nd method
# https://pypi.org/project/opencv-rolling-ball/
# 
# pip install opencv-rolling-ball
# Only works with 8 bit grey

>>>>>>> 8ab4d2cf5e09a310f8ba976fe612bdb6f34e53b0
A local background value is determined for every pixel by averaging over a 
very large ball around the pixel. This value is then subtracted from 
the original image, removing large spatial variations of the 
background intensities. The radius should be set to at least the size of the 
largest object that is not part of the background.
"""

<<<<<<< HEAD

from cv2_rolling_ball import subtract_background_rolling_ball


img = cv2.imread(IMAGE, 0)

radius=20
final_img, background = subtract_background_rolling_ball(img, radius, light_background=True,
                                     use_paraboloid=False, do_presmooth=True)
=======
from cv2_rolling_ball import subtract_background_rolling_ball
 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
radius = 15
final_img, background = subtract_background_rolling_ball(
                             img,
                             radius, light_background=True,
                             use_paraboloid=False,
                             do_presmooth=True)
>>>>>>> 8ab4d2cf5e09a310f8ba976fe612bdb6f34e53b0


#optionally perform CLAHE to equalize histogram for better segmentation
#otherwise the image may appear washedout.

clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8,8))
clahe_img = clahe.apply(final_img)

<<<<<<< HEAD
#cv2.imshow("Original image", img)
=======

>>>>>>> 8ab4d2cf5e09a310f8ba976fe612bdb6f34e53b0
cv2.imshow("Background image", background)
cv2.imshow("AFter background subtraction", final_img)
cv2.imshow("After CLAHE", clahe_img)

cv2.waitKey(0)
cv2.destroyAllWindows()