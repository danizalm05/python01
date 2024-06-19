'''
Perspective  Transform
https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=549s  45:20
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter5.py'''

import numpy as np
import cv2
import getpass
import os

image_name =  'cards.jpg' 
BASE_FOLDER = 'C:/Users/'+ getpass.getuser()+'/Pictures/Saved Pictures/'
path = BASE_FOLDER + image_name  #'b1.jpg' 'lena.png' 'bb.jpg'
print(path)


if os.path.isfile(path):
    img = cv2.imread(path)
    print(img.shape)

    cv2.imshow("Image",img)
    width,height = 250,350
    # 4  conrners of the card
    pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
    #4 corners of the output screen
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv2.warpPerspective(img,matrix,(width,height))

    print(pts1)
    cv2.imshow("Image",img)
    cv2.imshow("Output",imgOutput)
    cv2.waitKey(0)

else:
    print("ERROR --> Missing File: " + path   ) 


