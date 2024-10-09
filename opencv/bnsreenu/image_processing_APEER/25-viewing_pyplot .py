"""
display of images pyplot and opencv skimage
   
https://www.youtube.com/watch?v=2Q-bmlsdqRk&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=26
https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial25_viewing_images_in_python.py
"""
#
from skimage import io
import matplotlib.pyplot as plt
import cv2

USER1 = 'gilfm'
USER2 = 'rockman'
IMAGE_NAME = '1.jpg'
BASE_FOLDER = 'C:/Users/' + USER2 + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

img = io.imread(IMAGE)
io.imshow(img)

#MATPLOTLIB.PYPLOT

plt.imshow(img)  

#Colormaps...  https://matplotlib.org/tutorials/colors/colormaps.html
plt.imshow(img, cmap="hot")
#Not going to do anything as the input image is RGB

img_gray = io.imread(IMAGE, as_gray=True)
plt.imshow(img_gray, cmap="hot")
plt.imshow(img_gray, cmap="jet")


#Multiple plots using pyplot
fig = plt.figure(figsize=(10, 10))

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img_gray, cmap='hot')
ax1.title.set_text('1st')

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_gray, cmap='jet')
ax2.title.set_text('2nd')

ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img_gray, cmap='gray')
ax3.title.set_text('3rd')

ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img_gray, cmap='nipy_spectral')
ax4.title.set_text('4th')
plt.show()



############################################
#Using opencv



gray_img = cv2.imread(IMAGE, 0)
color_img = cv2.imread(IMAGE, 1)


# Use the function cv2.imshow() to display an image in a window. 
# First argument is the window name which is a string. second argument is our image. 

cv2.imshow("pic from skimage import", img)  #Shows weird colors as R and B channels are swapped
cv2.imshow("color pic from opencv", color_img)
cv2.imshow("gray pic from opencv", gray_img)

# Maintain output window until 
# user presses a key or 1000 ms (1s)
cv2.waitKey(0)          

#destroys all windows created
cv2.destroyAllWindows() 