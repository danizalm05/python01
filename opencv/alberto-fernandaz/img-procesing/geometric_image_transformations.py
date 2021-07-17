"""
geometric_image_transformations.py

Mastering-OpenCV-4-with-Python Chapter05 page 138

Alberto Fernández Villán
https://github.com/PacktPublishing/Mastering-OpenCV-4-with-Python/blob/master/Chapter05/01-chapter-content/geometric_image_transformations.py
"""

# Import required packages:
import cv2
import matplotlib.pyplot as plt
import numpy as np
import getpass

def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
#####################################

# Read the input image:
BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
img_name = "lena.png"     # "modrain.jpg"#"grains.jpg" #
path = BASE_FOLDER + img_name
print(path)

image = cv2.imread(path)

# Show loaded image:
show_with_matplotlib(image, 'Original image')

# 1. Scaling or resizing
# Resize the input image using cv2.resize()
# Resize using the scaling factor for each dimension of the image
# In this case the scaling factor is 0.5 in every dimension
dst_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# Get the height and width of the image:
height, width = image.shape[:2]


# You can resize also the image specifying the new size:
dst_image_2 = cv2.resize(image, (width * 2, height * 2), interpolation=cv2.INTER_LINEAR)

# We see the two resized images:
show_with_matplotlib(dst_image, 'Resized image')
show_with_matplotlib(dst_image_2, 'Resized image 2')

# 2. Translation page 139
# Create a 2x3 transformation matrix using numpy array with float values (float32)
# Translation in the x direction: 200 pixels, and  in the y direction: 30 pixels:
M = np.float32([[1, 0, 200], [0, 1, 30]])

# Once this transformation Matrix is created, we can pass it to the function cv2.warpAffine():
dst_image = cv2.warpAffine(image, M, (width, height-260))
#The third (width, height) argument establishes the size of the output image.
# Show the translated image:
show_with_matplotlib(dst_image, 'Translated image (positive values)')

# Additionally, the translation can take negative values:
M = np.float32([[1, 0, -200], [0, 1, -30]])
dst_image = cv2.warpAffine(image, M, (width, height))
show_with_matplotlib(dst_image, 'Translated image (negative values)')