'''
 .py
Mastering-OpenCV-4-with-Python Chapter05 page 160
C:/Users/gilfm/Documents/d/python01
Alberto Fernández Villán
https://github.com/PacktPublishing/Mastering-OpenCV-4-with-Python/blob/master/Chapter05/01-chapter-content/geometric_image_transformations.py
'''

# Import required packages:
import cv2
import matplotlib.pyplot as plt

import getpass

import os


BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/faces/'

path = BASE_FOLDER+'b1.jpg'
print(path)

def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    # Add the subplot to the created figure
    ax = plt.subplot(1, 2, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


# We create a figure() object with appropriate size and title:
plt.figure(figsize=(8, 4))
plt.suptitle("Colormaps", fontsize=14, fontweight='bold')

# We load the image using cv2.imread() and using 'cv2.IMREAD_GRAYSCALE' argument:
gray_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# We apply the color map 'cv2.COLORMAP_HSV'
img_COLORMAP_HSV = cv2.applyColorMap(gray_img, cv2.COLORMAP_HSV)

# Add the subplot:
show_with_matplotlib(cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR), "gray image", 1)
show_with_matplotlib(img_COLORMAP_HSV, "HSV", 2)

# Show the created image:
plt.show()
