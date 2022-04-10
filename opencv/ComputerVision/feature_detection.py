"""
Augmented Reality 255
feature_detection.py
Alberto Fernández Villán
Mastering OpenCV 4

Feature detection with ORB keypoint detector



FAST = Features from Accelerated Segment Test  Algorithm
Brief = Binary robust independent elementary feature

ORB is a fusion of FAST keypoint detector and BRIEF descriptor with some added
features to improve the performance.

How does Orb feature detection work?

Orb algorithm uses a multiscale image pyramid. Once orb has created a pyramid it
uses the fast algorithm to detect keypoints in the image.
 By detecting keypoints at each level orb is effectively locating
key points at a different scale.
In this way, ORB is partial scale invariant.
"""
import cv2
import numpy as np
import getpass
import matplotlib.pyplot as plt


img_name = 'p2.jpg'  # 'opencv_logo_with_text.png' "bb.jpg" "hickory.jpg"#
BASE_FOLDER = 'C:/Users/' + getpass.getuser() +'/Pictures/Saved Pictures/'
path = BASE_FOLDER + img_name
print(path)


def show_img_with_matplotlib(color_img, title, pos):

    img_RGB = color_img[:, :, ::-1] # Convert BGR image to RGB
    ax = plt.subplot(1, 2, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


# Create the dimensions of the figure and set title:
fig = plt.figure(figsize=(12, 5))
plt.suptitle("ORB keypoint detector", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')


image = cv2.imread(path)
orb = cv2.ORB_create()# Initiate ORB detector:
keypoints = orb.detect(image, None)# Detect the keypoints using ORB:

# Compute the descriptors of the detected keypoints:
keypoints, descriptors = orb.compute(image, keypoints)

# Print one ORB descriptor:
print("First extracted descriptor: {}".format(descriptors[0]))
print("Length of descriptor: {}".format(len(descriptors )))

# Draw detected keypoints:
image_keypoints = cv2.drawKeypoints(image, keypoints, None, color=(255, 0, 255), flags=0)

# Plot the images:
show_img_with_matplotlib(image, "image", 1)
show_img_with_matplotlib(image_keypoints, "detected keypoints", 2)

# Show the Figure:
plt.show()


