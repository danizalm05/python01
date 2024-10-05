"""
Black and white image colorization
https://www.youtube.com/watch?v=oNjQpq8QuAo
The basic idea is:
https://github.com/opencv/opencv/blob/master/samples/dnn/colorization.py

"""

# Import statements
import numpy as np


import argparse
import cv2 as cv

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

IMAGE_NAME = '1.jpg'#'wed.jpg' '3.jpg'
IMAGE_PATH = 'C:/Users/' + getpass.getuser() + '/Pictures/'
IMAGE = IMAGE_PATH +'Saved Pictures/'+ IMAGE_NAME
DIR = IMAGE_PATH + 'Resources/colorize/'

PROTOTXT = DIR + "colorization_deploy_v2.prototxt"
POINTS = DIR + "pts_in_hull.npy"
MODEL = DIR + "colorization_release_v2.caffemodel"
print(IMAGE)
# Argparser
ap = argparse.ArgumentParser()
W_in = 224
H_in = 224
imshowSize = (640, 480)
# Load the Model
print("Load model")
#dnn =   Deep Nural Network
net = cv.dnn.readNetFromCaffe(PROTOTXT, MODEL)
pts_in_hull = np.load(POINTS)  # load cluster centers
# populate cluster centers as 1x1 convolution kernel
pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1)

net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull.astype(np.float32)]
net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full([1, 313], 2.606, np.float32)]


frame = cv.imread(IMAGE)


 
# hasFrame, frame = cap.read()
# if not hasFrame:
#    cv.waitKey()
#    break
img_rgb = (frame[:,:,[2, 1, 0]] * 1.0 / 255).astype(np.float32)
img_lab = cv.cvtColor(img_rgb, cv.COLOR_RGB2Lab)
img_l = img_lab[:,:,0] # pull out L channel
(H_orig,W_orig) = img_rgb.shape[:2] # original image size

# resize image to network input size
img_rs = cv.resize(img_rgb, (W_in, H_in)) # resize image to network input size
img_lab_rs = cv.cvtColor(img_rs, cv.COLOR_RGB2Lab)
img_l_rs = img_lab_rs[:,:,0]
img_l_rs -= 50 # subtract 50 for mean-centering

net.setInput(cv.dnn.blobFromImage(img_l_rs))
ab_dec = net.forward()[0,:,:,:].transpose((1,2,0)) # this is our result

(H_out,W_out) = ab_dec.shape[:2]
ab_dec_us = cv.resize(ab_dec, (W_orig, H_orig))
img_lab_out = np.concatenate((img_l[:,:,np.newaxis],ab_dec_us),axis=2) # concatenate with original image L
img_bgr_out = np.clip(cv.cvtColor(img_lab_out, cv.COLOR_Lab2BGR), 0, 1)
frame = cv.resize(frame, imshowSize)

cv.imshow('origin', frame)
cv.imshow('gray', cv.cvtColor(frame, cv.COLOR_RGB2GRAY))
cv.imshow('colorized', cv.resize(img_bgr_out, imshowSize))


while True:
   if cv.waitKey(1) & 0xFF == ord('q'):
       break 
  
cv.destroyAllWindows()  
print("end")
 