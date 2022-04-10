"""
T81-558: Applications of Deep Neural Networks
https://www.youtube.com/watch?v=4Bh3gqHkIgc&list=PLjy4p-07OYzulelvJ5KVaT2pDlxivl_BN
Module 6: Convolutional Neural Networks (CNN) for Computer Vision
 PIL  python image     library
   
    Part 6.1: Image Processing in Python [Video] [Notebook]
    Part 6.2: Keras Neural Networks for Digits and Fashion MNIST [Video] [Notebook]
    Part 6.3: Implementing a ResNet in Keras [Video] [Notebook]
    Part 6.4: Using Your Own Images with Keras [Video] [Notebook]
    Part 6.5: Recognizing Multiple Images with YOLO Darknet [Video] [Notebook]



 """
from PIL import Image, ImageFile
from matplotlib.pyplot import imshow
import requests
from io import BytesIO
import numpy as np

from IPython.display import display, HTML

import cv2 as cv

url = "https://upload.wikimedia.org/wikipedia/commons/9/92/Brookings.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.load()

print(np.asarray(img))
img.show("original")
'''
Creating Images (from pixels) in Python

'''
w, h = 64, 64
data = np.zeros((h, w, 3), dtype=np.uint8)

# Yellow
for row in range(32):
    for col in range(32):
        data[row, col] = [255, 255, 0]

# Red
for row in range(32):
    for col in range(32):
        data[row + 32, col] = [255, 0, 0]

# Green
for row in range(32):
    for col in range(32):
        data[row + 32, col + 32] = [0, 255, 0]

    # Blue
for row in range(32):
    for col in range(32):
        data[row, col + 32] = [0, 0, 255]


img = Image.fromarray(data, 'RGB')
img.show("Creating Images (from pixels) in Python")

'''
 Here we take the mean color of each pixel and form a grayscale image.


'''
#url = "https://upload.wikimedia.org/wikipedia/commons/9/92/Brookings.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.load()

img_array = np.asarray(img)
rows = img_array.shape[0]
cols = img_array.shape[1]

print("Rows: {}, Cols: {}".format(rows,cols))

# Create new image
img2_array = np.zeros((rows, cols, 3), dtype=np.uint8)
for row in range(rows):
    for col in range(cols):
        t = np.mean(img_array[row,col])
        img2_array[row,col] = [t,t,t]

img2 = Image.fromarray(img2_array, 'RGB')

img2.show("Creating Images (from pixels) in Python")

images = [
    "https://upload.wikimedia.org/wikipedia/commons/9/92/Brookings.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/f/ff/" \
    "WashU_Graham_Chapel.JPG",
    "https://upload.wikimedia.org/wikipedia/commons/9/9e/SeigleHall.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/a/aa/WUSTLKnight.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/3/32/WashUABhall.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/c/c0/Brown_Hall.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/f/f4/South40.jpg"
]


def make_square(img):
    cols, rows = img.size
    extra = abs(rows - cols) / 2

    if rows > cols:
        r = (0, extra, cols, cols + extra)
    else:
        r = (extra, 0, rows + extra, rows)

    return img.crop(r)


x = []

for url in images:
    ImageFile.LOAD_TRUNCATED_IMAGES = False
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.load()
    img = make_square(img)
    img = img.resize((128, 128), Image.ANTIALIAS)
    print(url)
    img.show("Creating Images (from pixels) in Python")

    display(img)
    img_array = np.asarray(img)
    img_array = img_array.flatten()
    img_array = img_array.astype(np.float32)
    img_array = (img_array - 128) / 128
    x.append(img_array)

x = np.array(x)

print(x.shape)