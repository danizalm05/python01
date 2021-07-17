"""
Sobel operator example in order to see how this operator works and how
 cv2.addWeighted() can be used


Mastering-OpenCV-4-with-Python Chapter05 page 151
Alberto Fernández Villán
https://github.com/PacktPublishing/Mastering-OpenCV-4-with-Python/blob/master/Chapter05/01-chapter-content/
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

def show_with_matplotlib(color_img, title, pos):

    # Convert BGR image to RGB
    if (len(color_img.shape) == 3): # This is 3 color  image
               img_RGB = color_img[:, :, ::-1]
    else :
        img_RGB =  cv2.cvtColor(color_img, cv2.COLOR_GRAY2BGR)

    ax = plt.subplot(4, 3, pos )
    #plt.xticks(position=(0, 0.06), size=10)
    plt.imshow(img_RGB)

    plt.title(title)
    plt.axis('off')



# Create the dimensions of the figure and set title:
plt.figure(figsize=(10, 4))
plt.suptitle("Sobel operator and cv2.addWeighted() to show the output",
             fontsize=14, fontweight='bold')

# Load the original image:
image = cv2.imread(path)
# Filter the image with a gaussian kernel:
image_filtered = cv2.GaussianBlur(image, (3, 3), 0)

# We convert the image to grayscale:
gray_image = cv2.cvtColor(image_filtered, cv2.COLOR_BGR2GRAY)

# Gradient x is calculated:
# the depth of the output is set to CV_16S to avoid overflow
# CV_16S = one channel of 2-byte signed integers (16-bit signed integers)
gradient_x = cv2.Sobel(gray_image, cv2.CV_16S, 1, 0, 3)

# Gradient y is calculated:
# the depth of the output is set to CV_16S to avoid overflow
# CV_16S = one channel of 2-byte signed integers (16-bit signed integers)
gradient_y = cv2.Sobel(gray_image, cv2.CV_16S, 0, 1, 3)

# Conversion to an unsigned 8-bit type:
abs_gradient_x = cv2.convertScaleAbs(gradient_x)
abs_gradient_y = cv2.convertScaleAbs(gradient_y)

# Combine the two images using the same weight:
sobel_image = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)

# Display all the resulting images:
show_with_matplotlib(image, "Image", 1)
show_with_matplotlib(cv2.cvtColor(abs_gradient_x, cv2.COLOR_GRAY2BGR), "Gradient x", 2)
show_with_matplotlib(cv2.cvtColor(abs_gradient_y, cv2.COLOR_GRAY2BGR), "Gradient y", 3)
show_with_matplotlib(cv2.cvtColor(sobel_image, cv2.COLOR_GRAY2BGR), "Sobel output", 4)


scale = 0.6
img_array = ([image,abs_gradient_x],
             [abs_gradient_y,sobel_image])

title_array =(["original", "Gradient x"],
              ["Gradient y","Sobel output"])


imgStack = ImageTable.stackImages(scale, img_array, title_array)
cv2.imshow("imgStack", imgStack)
plt.show()

