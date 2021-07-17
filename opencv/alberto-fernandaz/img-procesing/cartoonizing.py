"""
cartoonizing.py

Mastering-OpenCV-4-with-Python Chapter05 page 147

Alberto Fernández Villán
https://github.com/PacktPublishing/Mastering-OpenCV-4-with-Python/blob/master/Chapter05/01-chapter-content/geometric_image_transformations.py
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np
import getpass
import ImageTable

# Read the input image:
BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
img_name = "p1.jpg"  #"lena.png"     # "modrain.jpg"#"grains.jpg" #
path = BASE_FOLDER + img_name
print(path)




def sketch_image(img):
    """Sketches the image applying a laplacian operator to detect the edges"""

    # Convert to gray scale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median filter
    img_gray = cv2.medianBlur(img_gray, 5)#reduce the noise by smoothing

    # Detect edges using cv2.Laplacian()
    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)

    # Threshold the edges image:
    ret, thresholded = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)
      # thresholded a binary image from the given grayscale
    return thresholded

def cartonize_image(img, gray_mode=False):
    """Cartoonizes the image applying cv2.bilateralFilter()"""

    # Get the sketch:
    thresholded = sketch_image(img)

    # Apply bilateral filter with "big numbers" to get the cartoonized effect:
    filtered = cv2.bilateralFilter(img, 10, 250, 250)

    # Perform 'bitwise and' with the thresholded img as mask in order to set
    # these values to the output
    cartoonized = cv2.bitwise_and(filtered, filtered, mask=thresholded)

    if gray_mode:
        return cv2.cvtColor(cartoonized, cv2.COLOR_BGR2GRAY)

    return cartoonized


def show_with_matplotlib(color_img, title, pos):

    # Convert BGR image to RGB
    if (len(color_img.shape) == 3): # This is 3 color  image
               img_RGB = color_img[:, :, ::-1]
    else :
        img_RGB =  cv2.cvtColor(color_img, cv2.COLOR_GRAY2BGR)

    ax = plt.subplot(4, 3, pos )
    plt.xticks(position=(0, 0.06), size=10)
    plt.imshow(img_RGB)

    plt.title(title)
    #plt.axis('off')



# Create the dimensions of the figure and set title:
plt.figure(figsize=(16, 16))
plt.suptitle("Cartoonizing images", fontsize=14, fontweight='bold')
#####################
image = cv2.imread(path)

custom_sketch_image = sketch_image(image)
custom_cartonized_image = cartonize_image(image)
custom_cartonized_image_gray = cartonize_image(image, True)

# Call the OpenCV functions to get a similar output:
sketch_gray, sketch_color = cv2.pencilSketch(image, sigma_s=30, sigma_r=0.1, shade_factor=0.1)
stylizated_image = cv2.stylization(image, sigma_s=60, sigma_r=0.07)

# Display all the resulting images:
show_with_matplotlib(image, "original", 1)
#show_with_matplotlib(cv2.cvtColor(custom_sketch_image, cv2.COLOR_GRAY2BGR), "custom sketch", 2)
show_with_matplotlib(custom_sketch_image , "custom sketch", 2)

show_with_matplotlib(sketch_color, "sketch color cv2.pencilSketch()", 3)
show_with_matplotlib(stylizated_image, "cartoonized cv2.stylization()", 4)
show_with_matplotlib(custom_cartonized_image, "custom cartoonized", 5)
show_with_matplotlib( custom_cartonized_image_gray , "custom cartoonized gray", 7)
scale = 0.8
img_array = ([image, custom_sketch_image ],
             [custom_cartonized_image , custom_cartonized_image_gray])
title_array =(["image","custom_sketch_image"],
              ["custom_cartonized_image","custom_cartonized_image_gray"])
imgStack = ImageTable.stackImages(scale, img_array, title_array)
cv2.imshow("imgStack", imgStack)
plt.show()

