"""
contours_introduction.py
Introduction to contours (1)
page 223
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt


def get_one_contour():
    """Returns a 'fixed' contour"""

    cnts =  [np.array(
         [[  [600, 320]], [[563, 460]], [[460, 562]], [[320, 600]],
            [[180, 563]], [[78, 460]], [[40, 320]], [[77, 180]],
            [[179, 78]], [[319, 40]], [[459, 77]], [[562, 179]
        ]],
         dtype=np.int32) ]
    return cnts


def array_to_tuple(arr):
    """Converts array to tuple"""
     # -1 means 2'd dimention is unknown so it will be claculated by  python
    return tuple(arr.reshape(1, -1)[0])


def draw_contour_points(img, cnts, color):
    """Draw all points from a list of contours"""

    for cnt in cnts:
        print("Shape before  squeeze = ",cnt.shape)
        #print(cnt)
        #squeeze --> get rid of onedimensional arrays like using [1,2,3]
        # instead of [[[1,2,3]]].
        squeeze = np.squeeze(cnt)
        print("Shape after  squeeze = ",squeeze.shape)
        #print(squeeze)

        for p in squeeze:
            # print(p)
            p = array_to_tuple(p)#converts an array into a tuple
            #  first point of  the contour, [600 320], is transformed
            #i nto(600, 320), which is ready to  use inside cv2.circle()

            # print(p)
            cv2.circle(img, p, 10, color, -1)

    return img


def draw_contour_outline(img, cnts, color, thickness=1):
    """Draws contours outlines of each contour
    img np.zeros((640, 640, 3)
    cnts =  array that contains the points of the  contour
    """

    for cnt in cnts:
        # Draw  a contour outline in the image
        cv2.drawContours(img, [cnt], 0, color, thickness)


def show_img_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(1, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')
###########################################################

# Create the dimensions of the figure and set title:
fig = plt.figure(figsize=(12, 5))
plt.suptitle("Contours introduction", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')

# Create the canvas (black image with three channels):
canvas = np.zeros((640, 640, 3), dtype="uint8")

# Get a sample contours:
contours = get_one_contour()
print("contour shape: '{}'".format(contours[0].shape))
print("'detected' contours: '{}' ".format(len(contours)))

# Create copy images to show the different results:
image_contour_points = canvas.copy()
image_contour_outline = canvas.copy()
image_contour_points_outline = canvas.copy()

# Draw only contour points:
draw_contour_points(image_contour_points, contours, (255, 0, 255))

# Draw only contour outline:
draw_contour_outline(image_contour_outline, contours, (0, 255, 255), 3)

# Draw both contour outline and points:
draw_contour_outline(image_contour_points_outline, contours, (255, 0, 0), 3)
draw_contour_points(image_contour_points_outline, contours, (0, 0, 255))

# Plot the images:
show_img_with_matplotlib(image_contour_points, "contour points", 1)
show_img_with_matplotlib(image_contour_outline, "contour outline", 2)
show_img_with_matplotlib(image_contour_points_outline, "contour outline and points", 3)

# Show the Figure:
plt.show()
