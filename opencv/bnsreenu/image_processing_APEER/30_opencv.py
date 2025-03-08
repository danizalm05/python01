"""
Tutorial 30 - Basic image processing using opencv in python 

https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial30_image_processing_using_opencv.py
https://www.youtube.com/watch?v=3J1YG17FDjw&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=31 
  
"""
import cv2
import getpass
import os

USER = getpass.getuser()

IMAGE_NAME = 'lena.jpg' #'2.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

print(IMAGE)
path = BASE_FOLDER
file_list = os.listdir(path)

for (image) in os.listdir(path):  # iterate through each file to perform some action
    print(image)

img = cv2.imread(IMAGE, 1)   #Color is BGR not RGB

#use cv2.resize. Can specify size or scaling factor.
#Inter_cubic or Inter_linear for zooming.
#Use INTER_AREA for shrinking
#Following zooms by 2 times.

resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow("original pic", img)
cv2.imshow("resized pic", resized)
cv2.waitKey(0)          
cv2.destroyAllWindows() 

grey_img = cv2.imread(IMAGE, 0) 
img = cv2.imread(IMAGE, 1)   #Color is BGR not RGB

print(img.shape)     #(586, 415, 3)
print("Top left", img[0,0])    #Top left pixel
print("Top right", img[0, 400])  # Top right
print("Bottom Left", img[511, 0]) # Bottom left
print("Bottom right", img[511, 400])  # Bottom right

cv2.imshow("color pic", img)
 

#Split and merging channels
#Show individual color channels in the image
blue = img[:, :, 0]   #Show only blue pic. (BGR so B=0)
green = img[:, :, 1]  #Show only green pixels
red = img[:, :, 2]  #red only
# another way
b,g,r = cv2.split(img)


cv2.imshow("blue pic", b)
cv2.imshow("green pic", g)
cv2.imshow("red pic", r)
cv2.waitKey(0)        

#Edge detection:
    
import cv2

 
edges = cv2.Canny(img,100,200)   #Image, min and max values

 
cv2.imshow("Canny", edges)

cv2.waitKey(0)          
  
cv2.destroyAllWindows()  