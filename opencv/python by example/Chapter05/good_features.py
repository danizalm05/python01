'''
page  216
'''

import cv2
import numpy as np

import getpass

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #
mimg = "bb.jpg"
path = BASE_FOLDER + mimg
scaling_factor =0.5
img   = cv2.imread(path)
img = cv2.resize(img, None, fx=scaling_factor,
                 fy=scaling_factor, interpolation=cv2.INTER_AREA)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
 
corners = cv2.goodFeaturesToTrack(gray, maxCorners=7, qualityLevel=0.05,
                                  minDistance=25)
corners = np.float32(corners) 
print(corners)
for item in corners: 
    x, y = item[0] 
    cv2.circle(img, (int(x),int(y)), 5, 255, -1)
 
cv2.imshow("Top 'k' features", img) 
cv2.waitKey()