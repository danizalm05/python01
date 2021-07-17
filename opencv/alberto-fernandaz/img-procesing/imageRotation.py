"""
imageRotation.py

Mastering-OpenCV-4-with-Python Chapter05 page 149

Alberto Fernández Villán
https://github.com/PacktPublishing/Mastering-OpenCV-4-with-Python/blob/master/Chapter05/01-chapter-content/geometric_image_transformations.py
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np
import getpass

def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""
    img_RGB = color_img[:, :, ::-1]   # Convert BGR image to RGB:

    ax = plt.subplot(3, 6, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')
#####################################

# Read the input image:
BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
img_name = "lena.png"     # "modrain.jpg"#"grains.jpg" #
path = BASE_FOLDER + img_name
print(path)

image = cv2.imread(path)
#####################################
# create a figure() object with appropriate size and title:
plt.figure(figsize=(42, 15))
plt.suptitle("imageRotation", fontsize=14, fontweight='bold')
# Show loaded image:
show_with_matplotlib(image, 'Original image',1)
height, width = image.shape[:2]
# 3. Rotation

# Build the 2x3 rotation matrix:
# Rotate the image 180 degrees (upside down) scale factor of 1:
M = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), 180, 2)
dst_image = cv2.warpAffine(image, M, (width, height))

# Show the center of rotation and the rotated image:
radios = 18
color_radios= (125, 180, 100)
cv2.circle(dst_image, (round(width / 2.0), round(height / 2.0)), radios, color_radios, -1)
show_with_matplotlib(dst_image, 'Image rotated 180 degrees',2)

# Now, we are going to rotate the image 30 degrees changing the center of rotation
M = cv2.getRotationMatrix2D((width / 1.5, height / 1.5), 30, 3)
dst_image = cv2.warpAffine(image, M, (width, height))

# Show the center of rotation and the rotated image:
cv2.circle(dst_image, (round(width / 1.5), round(height / 1.5)), radios, color_radios, -1)
show_with_matplotlib(dst_image, 'Image rotated 30 degrees',3)

# 4. Affine Transformation  page 140
# In an affine transformation we first make use of the function
# cv2.getAffineTransform()
# to build the 2x3 transformation matrix, which is obtained from the relation
# between three points  from the input image and their corresponding coordinates
# in the transformed image.

# A copy of the image is created to show the points that will be used for the affine transformation:
image_points = image.copy()
cv2.circle(image_points, (135, 45), 20, (255, 250, 255), -1)
cv2.circle(image_points, (385, 45), 20, (255, 250, 255), -1)
cv2.circle(image_points, (135, 230), 20, (255, 250, 255), -1)

# Show the image with the three created points:
show_with_matplotlib(image_points, 'before affine transformation',7)

# We create the arrays with the aforementioned three points and the desired positions
# in the output image:
pts_1 = np.float32([[135, 45], [385, 45], [135, 230]])
pts_2 = np.float32([[135, 45], [385, 45], [150, 230]])

# We get the 2x3 tranformation matrix based on pts_1 and pts_2 and
# apply cv2.warpAffine():
M = cv2.getAffineTransform(pts_1, pts_2)
dst_image = cv2.warpAffine(image_points, M, (width, height))

# Show the image:
show_with_matplotlib(dst_image, 'Affine transformation',8)

# 5. Perspective transformation
# A copy of the image is created to show the points that will be used for the perspective transformation:
image_points = image.copy()
cv2.circle(image_points, (450, 65), radios, (255, 0, 255), -1)
cv2.circle(image_points, (517, 65), radios, (255, 0, 255), -1)
cv2.circle(image_points, (431, 164), radios, (255, 0, 255), -1)
cv2.circle(image_points, (552, 164), radios, (255, 0, 255), -1)

# Show the image:
show_with_matplotlib(image_points, 'before perspective transformation',10)
# cv2.getPerspectiveTransform() needs four pairs of points
# (coordinates of a quadrangle in both the source and output image)
# We create the arrays for these four pairs of points:
pts_1 = np.float32([[450, 65], [517, 65], [431, 164], [552, 164]])
pts_2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# To correct the perspective (also known as perspective transformation)
# you need to create the transformation matrix
# making use of the function cv2.getPerspectiveTransform(), where a 3x3 matrix
# is constructed:
M = cv2.getPerspectiveTransform(pts_1, pts_2)

# Then, apply cv2.warpPerspective(), where the source image is transformed applying
# the specified matrix and with a specified size:
dst_image = cv2.warpPerspective(image, M, (300, 300))

# Show the image:
show_with_matplotlib(dst_image, 'perspective transformation',12)

# 6. Cropping
# A copy of the image is created to show the points that will be used for the
# cropping example:
image_points = image.copy()

# Show the points and lines connecting the points:
cv2.circle(image_points, (230, 80), 5, (0, 0, 255), -1)
cv2.circle(image_points, (330, 80), 5, (0, 0, 255), -1)
cv2.circle(image_points, (230, 200), 5, (0, 0, 255), -1)
cv2.circle(image_points, (330, 200), 5, (0, 0, 255), -1)
cv2.line(image_points, (230, 80), (330, 80), (0, 0, 255))
cv2.line(image_points, (230, 200), (330, 200), (0, 0, 255))
cv2.line(image_points, (230, 80), (230, 200), (0, 0, 255))
cv2.line(image_points, (330, 200), (330, 80), (0, 0, 255))

# Show the image with the points and lines:
show_with_matplotlib(image_points, 'Before cropping',13)

# For cropping, we make use of numpy slicing:
dst_image = image[80:200, 230:330]

# Show the image:
show_with_matplotlib(dst_image, 'Cropping image',14)


plt.show()