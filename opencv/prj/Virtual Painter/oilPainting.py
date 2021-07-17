import cv2
import numpy as np
import getpass
import matplotlib.pyplot as plt
###################
#image_source = "camera"
image_source = "image"
img_name = "b1.jpg"     # "modrain.jpg"#"grains.jpg" #

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
path = BASE_FOLDER + img_name
print(path)
img = cv2.imread(path)
cv2.imshow('original',img)
water2 = cv2.stylization(img, sigma_s=160, sigma_r=0.4)
water3 = cv2.stylization(img, sigma_s=60, sigma_r=0.2)
oil2 = cv2.xphoto.oilPainting(water2, 7, 1)
cv2.imshow('water color',water2)
# To stack horizontally (img_OpenCV to the left of img_matplotlib):
#img_concats = np.concatenate((img,water2), axis=1)
# Now, we show the concatenated image:
#cv2.imshow('bgr image and rgb image', img_concats)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Translate image from bgr to RGB color format
# Split the loaded image into its three channels (b, g, r):
imgt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
water = cv2.cvtColor(water2, cv2.COLOR_BGR2RGB)
# Show both images (img_OpenCV and img_matplotlib) using matplotlib
# This will show the image in wrong color:



# making subplots
fig, ax = plt.subplots(2, 2,figsize=(10, 8))


# set data with subplots and plot
ax[0, 0].set_title("Original bgr")
ax[0, 0].imshow(img)

ax[0, 1].set_title("Original rgb")
ax[0, 1].imshow(imgt, cmap='gray')


ax[1, 0].set_title("stylization(s_s=160, s_r=0.4")
ax[1, 0].imshow(cv2.cvtColor(water2, cv2.COLOR_BGR2RGB))

ax[1, 1].set_title("oil(1, 7")
ax[1, 1].imshow(cv2.cvtColor(oil2, cv2.COLOR_BGR2RGB), cmap='gray')

plt.suptitle('Various water oil color',fontsize=20,fontweight ="bold")


fig.tight_layout()
# set spacing
fig.tight_layout()
plt.show()