# -*- coding: utf-8 -*-
"""
 https://drive.google.com/open?id=1zPoNaBOwX61n9Co7t68JGgJX9Rny8KLU
 General-purpose and introductory examples for scikit-image.
 https://scikit-image.org/docs/stable/auto_examples/

 image list https://scikit-image.org/docs/0.13.x/api/skimage.data.html
"""
import numpy as np
from skimage import data
import matplotlib.pyplot as plt
camera0 =  data.astronaut()
camera =  data.astronaut()
camera[:10] = 0
mask = camera < 87
#mask = [[[ True  True  True]   .......
camera[mask] = 255
inds_x = np.arange(len(camera))
inds_y = (4 * inds_x) % len(camera)
camera[inds_x, inds_y] = 0

l_x, l_y = camera.shape[0], camera.shape[1]
X, Y = np.ogrid[:l_x, :l_y]
outer_disk_mask = (X - l_x / 2)**2 + (Y - l_y / 2)**2 > (l_x / 2)**2
camera[outer_disk_mask] = 0

plt.figure(figsize=(4, 4))
plt.title("Original")
plt.imshow(camera0, cmap='gray')
plt.figure(figsize=(4, 4))
plt.title("oppp")
plt.imshow(camera, cmap='gray')
plt.axis('off')
plt.show()