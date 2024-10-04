"""
Black and white image colorization 
https://www.youtube.com/watch?v=gAmskBNz_Vc
https://github.com/balajisrinivas/Colorizing-black-and-white-images-using-Python/blob/master/colorize.py
6:17
"""

# Import statements
import numpy as np
import argparse
import cv2
import os
import getpass
"""
Download the model files: 
1. colorization_deploy_v2.prototxt:   
   https://github.com/richzhang/colorization/blob/caffe/colorization/models/colorization_deploy_v2.prototxt
2. pts_in_hull.npy:					   
   https://github.com/richzhang/colorization/blob/caffe/colorization/resources/pts_in_hull.npy
3. colorization_release_v2.caffemodel: 
   https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1

"""

IMAGE_NAME = 'wed.jpg'
IMAGE_PATH = 'C:/Users/' + getpass.getuser() + '/Pictures/'
IMAGE = IMAGE_PATH +'Saved Pictures/'+ IMAGE_NAME
DIR = IMAGE_PATH + 'Resources/colorize/'

PROTOTXT = DIR + "colorization_deploy_v2.prototxt"
POINTS = DIR + "pts_in_hull.npy"
MODEL = DIR + "colorization_release_v2.caffemodel"
print(IMAGE)
# Argparser
ap = argparse.ArgumentParser()

# Load the Model
print("Load model")
#dnn =   Deep Nural Network
net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
pts = np.load(POINTS)
image = cv2.imread(IMAGE)

scaled = image.astype("float32") / 255.0
lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
print(MODEL)

resized = cv2.resize(lab, (224, 224))
L = cv2.split(resized)[0]
L -= 50

print("Colorizing the image")
net.setInput(cv2.dnn.blobFromImage(L))
ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

ab = cv2.resize(ab, (image.shape[1], image.shape[0]))

L = cv2.split(lab)[0]
colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
colorized = np.clip(colorized, 0, 1)

colorized = (255 * colorized).astype("uint8")

cv2.imshow("Original", image)
cv2.imshow("Colorized", colorized)
cv2.waitKey(0)