"""
 
Tutorial 27 - Using glob to read multiple files in python 
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial27_using_glob_to_read_multiple_images.py
https://www.youtube.com/watch?v=Z90KEqJoC3w&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=28

#The glob module finds all the path names
#matching a specified pattern according to the rules used by the
Unix shell.The glob.glob returns the list of files with their full path

"""
#
import matplotlib.pyplot as plt
import numpy as np
import cv2
import getpass
import glob
from matplotlib import pyplot as plt

USER = getpass.getuser()

IMAGE_NAME = '1.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

path = "C:/Users/rockman/Pictures/backimage/*.*"
file_list = glob.glob(path) #Rerurns a list of file names
#print(file_list)  #Prints the list containing file names


my_list = []  # Empty list to store images from the folder.

for file in glob.glob(path):
    print(file)
    a = cv2.imread(file)
    my_list.append(a)  # list of images
plt.imshow(my_list[2])  #View the 3rd image in the list.
plt.show()

img_number = 1  #Start an iterator for image number.
for file in glob.glob(path):
    print(file)     #just stop here to see all file names printed
    a= cv2.imread(file)  #now, we can read each file since we have the full path
    #print(a)  #print numpy arrays for each file

#let us look at each file
    cv2.imshow('Original Image', a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # process each image - change color from BGR to RGB.
    c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)  # Change color space from BGR to RGB
    #cv2.imwrite("images/test_images/Color_image" + str(img_number) + ".jpg", c)
    img_number += 1
    cv2.imshow('Color image', c)
    cv2.waitKey(1000)  # Display each image for 1 second
    cv2.destroyAllWindows()
