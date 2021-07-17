"""
arithmetic.py

Mastering-OpenCV-4-with-Python Chapter05 page 150

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
plt.figure(figsize=(18, 10))
plt.suptitle("Arithmetic with images", fontsize=14, fontweight='bold')
#####################
image = cv2.imread(path)
# Add 60 to every pixel on the image. The result will look lighter:
M = np.ones(image.shape, dtype="uint8") * 60
added_image = cv2.add(image, M)

# Subtract 60 from every pixel. The result will look darker:
subtracted_image = cv2.subtract(image, M)



# Additionally, we can build an scalar and add/subtract it:
scalar = np.ones((1, 3), dtype="float") * 110
added_image_2 = cv2.add(image, scalar)
subtracted_image_2 = cv2.subtract(image, scalar)

# Display all the resulting images:
show_with_matplotlib(image, "image", 1)
show_with_matplotlib(added_image, "added 60 (image + image)", 2)
show_with_matplotlib(subtracted_image, "subtracted 60 (image - images)", 3)
show_with_matplotlib(added_image_2, "added 110 (image + scalar)", 5)
show_with_matplotlib(subtracted_image_2, "subtracted 110 (image - scalar)", 6)



scale = 0.6
img_array = ([image,added_image,subtracted_image   ],
             [added_image_2  , subtracted_image_2, image ])
title_array =(["original", "added_image","subtracted_image"],
              ["added_image_2","subtracted_image_2","original"])
imgStack = ImageTable.stackImages(scale, img_array, title_array)
cv2.imshow("imgStack", imgStack)
plt.show()

