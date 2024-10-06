#!/usr/bin/env python
'''
17 - Read and  count only images files in a directory
Apeer_micro

######################################################################################
### Reading multiple images from a folder
#The glob module finds all the path names
#matching a specified pattern according to the rules used by the Unix shell
#The glob.glob returns the list of files with their full path

https://www.youtube.com/watch?v=52pMFnkDU-4
https://github.com/bnsreenu/python_for_microscopists/blob/master/017-Reading_Images_in_Python.py

'''

import cv2
import glob
import os
from PIL import Image
#C:\Users\rockman\Anaconda3\envs\tensorflow
USER1 = 'gilfm'
USER2 = 'rockman'
BASE_FOLDER = 'C:/Users/' + USER2 + '/Pictures/Saved Pictures/*'

file_list = glob.glob(BASE_FOLDER)
img_file_list = []
for file_name in  file_list :
    split_tup = os.path.splitext(file_name)
    file_extension = split_tup[1]
    if (file_extension == ".jpg") or (file_extension == ".png") \
            or (file_extension == ".tif"):
       img_file_list.append(file_name)

num_of_imgs = len(img_file_list)
print(" Number of   images = ",num_of_imgs)

i = 0
for img_name in  img_file_list :
    i += 1
    print(i,img_name)
    a = cv2.imread(img_name)
    cv2.imshow(img_name, a)

cv2.waitKey(0)
cv2.destroyAllWindows()







for  file in  img_file_list:

    print(file)     #just stop here to see all file names printed
    a= Image.open(file)  #now, we can read each file since we have the full path

    rotated45 = a.rotate(45, expand=True)
    rotated45.save(file+"_rotated45.png", "PNG")

