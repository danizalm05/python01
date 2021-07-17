
#basic_opencv

#https://github.com/bnsreenu/python_for_microscopists/blob/master/025-image_processing_in_openCV_intro1-preprocessing.py
# https://www.youtube.com/watch?v=yj40XoUqo70

# https://drive.google.com/drive/folders/1vIm0uQxygOGCbZQZPIY4kRYl3Sk5it7W
#It is used extensively for facial recognition, object recognition, motion tracking,
#optical character recognition, segmentation, and even for artificial neural netwroks.

#Useful preprocessing steps for image processing, for example segmentation.
#1. SPlit & Merge channels
#2. Scaling / resizing
#3. Denoising / smoothing
#4. Edge detection
#5. Enhancing images. using histogram equalization


import cv2

USER1 = "gilfm"
USER2 = "rockman"
BASE_FOLDER = 'C:/Users/'+ USER1 +'/Pictures/Saved Pictures/'
img_name = "lena.png"
path = BASE_FOLDER + img_name
img0 = cv2.imread(path,0)# open image  witg gray colors
u0 = "https://raw.githubusercontent.com/bnsreenu/python_for_microscopists/master/images/RGBY.jpg"
grey_img = cv2.imread(path, 0)#"images/RGBY.jpg"
img = cv2.imread(path, 1)   #Color is BGR not RGB

print(img.shape)     #(586, 415, 3)
print("Top left pixel", img[0,0])    #Top left pixel
print("Top right pixel [0", img.shape[1], "] = ",  img[0, img.shape[1]-1])  # Top right
print("Bottom Left pixel", img[img.shape[0]-1, 0]) # Bottom left
print("Bottom right pixel[",img.shape[0]-1,",",img.shape[1]-1 ,"] = ",img[img.shape[0]-1  , img.shape[1]-1] )  # Bottom right
# yellow = green +red
cv2.imshow("color pic", img)

#Split and merging channels  (using numpy)
#Show individual color channels in the image
blue = img[:, :, 0]   #Show only blue pic. (BGR so B=0)
green = img[:, :, 1]  #Show only green pixels
red = img[:, :, 2]  #red only
cv2.imshow("blue pic", blue)
cv2.imshow("green pic", green)
cv2.imshow("red pic", red)
cv2.waitKey(0)          
cv2.destroyAllWindows()

#  Or split all channels at once (using cv2)

b, g, r = cv2.split(img)

cv2.imshow("green pic", g)
cv2.waitKey(0)
cv2.destroyAllWindows()

#to merge each image into bgr

img_merged = cv2.merge((b,g,r))

cv2.imshow("merged pic", img_merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Basic image operations
# Scaling,
#https://docs.opencv.org/3.3.1/da/d6e/tutorial_py_geometric_transformations.html



path = BASE_FOLDER + "lena.png"
img = cv2.imread(path, 1)   #Color is BGR not RGB

#use cv2.resize. Can specify size or scaling factor.
#Inter_cubic or Inter_linear for zooming.
#Use INTER_AREA for shrinking
#Following xample zooms by 2 times.

resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow("original pic", img)
cv2.imshow("resized pic", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()