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

    ax = plt.subplot(3, 3, pos )
    #plt.xticks(position=(0, 0.06), size=10)
    plt.imshow(img_RGB)

    plt.title(title)
    plt.axis('off')





# Create the dimensions of the figure and set title:
plt.figure(figsize=(12, 6))
plt.suptitle("Bitwise operations (AND, OR, XOR, NOT)", fontsize=14, fontweight='bold')

# Create the first image:
img_1 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(img_1, (10, 10), (110, 110), (255, 255, 255), -1)
cv2.circle(img_1, (200, 200), 50, (255, 255, 255), -1)

# Create the second image:
img_2 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(img_2, (50, 50), (150, 150), (255, 255, 255), -1)
cv2.circle(img_2, (225, 200), 50, (255, 255, 255), -1)# Load the original image:

# Bitwise OR
bitwise_or = cv2.bitwise_or(img_1, img_2)

# Bitwise AND
bitwise_and = cv2.bitwise_and(img_1, img_2)

# Bitwise XOR
bitwise_xor = cv2.bitwise_xor(img_1, img_2)

# Bitwise NOT
bitwise_not_1 = cv2.bitwise_not(img_1)

# Bitwise NOT
bitwise_not_2 = cv2.bitwise_not(img_2)


# Display all the resulting images:
show_with_matplotlib(cv2.cvtColor(img_1, cv2.COLOR_GRAY2BGR), "image 1", 1)
show_with_matplotlib(cv2.cvtColor(img_2, cv2.COLOR_GRAY2BGR), "image 2", 2)
show_with_matplotlib(cv2.cvtColor(bitwise_or, cv2.COLOR_GRAY2BGR), "image 1 OR image 2", 3)
show_with_matplotlib(cv2.cvtColor(bitwise_and, cv2.COLOR_GRAY2BGR), "image 1 AND image 2", 4)
show_with_matplotlib(cv2.cvtColor(bitwise_xor, cv2.COLOR_GRAY2BGR), "image 1 XOR image 2", 5)
show_with_matplotlib(cv2.cvtColor(bitwise_not_1, cv2.COLOR_GRAY2BGR), "NOT (image 1)", 6)
show_with_matplotlib(cv2.cvtColor(bitwise_not_2, cv2.COLOR_GRAY2BGR), "NOT (image 2)", 7)

# See how these operations can be used to work with images:
# Load the original image:
image = cv2.imread(path)
cv2.imshow("image", image)
(m,n) =(image.shape[0],image.shape[1])
print(m,n)

# Create the image to be used as mask:
img_3 = np.zeros(shape = (m,n), dtype="uint8")
cv2.circle(img_3, (150, 150), 150, (255, 255, 255), -1)

# Bitwise AND using the img_3 as mask:
bitwise_and_example = cv2.bitwise_and(image, image, mask=img_3)

# Show these two images:
show_with_matplotlib(cv2.cvtColor(img_3, cv2.COLOR_GRAY2BGR), "image 3", 8)
show_with_matplotlib(bitwise_and_example, "image 3 AND a loaded image", 9)


scale = 1.3
img_array = ([img_1,img_2,bitwise_or],
             [bitwise_and,bitwise_xor,bitwise_not_1],
             [bitwise_not_2,img_3,bitwise_and_example])

title_array =(["image 1", "image 2", "OR"],
              ["and", "xor", "not 1"],
              ["not 2", "img_3", "bitwise_and_example"])


imgStack = ImageTable.stackImages(scale, img_array, title_array)
cv2.imshow("imgStack", imgStack)


plt.show()

