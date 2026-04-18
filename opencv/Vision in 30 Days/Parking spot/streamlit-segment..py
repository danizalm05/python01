'''

Machine learning web app with Python, Streamlit & Segment Anything Model
 | Modelbit model deployment 

https://www.youtube.com/watch?v=W8OvdQPL7lk&list=PLb49csYFtO2HGELdc-RLRCNVNy0g2UMwc&index=21
 

https://youtu.be/W8OvdQPL7lk?list=PLb49csYFtO2HGELdc-RLRCNVNy0g2UMwc&t=555



https://github.com/computervisioneng/streamlit-segment-anything-model-python/blob/main/BackgroundRemovalWebaPP_Backend.ipynb

https://github.com/facebookresearch/segment-anything

colab address 
https://colab.research.google.com/drive/109oevnjECkL-tG5z5T3KPG70wIkjjtAj#scrollTo=2LozyVi_i6rE

'''
#colab read and show image 

import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io
u0 ="https://c8.alamy.com/comp/2M79D5J/fantastic-view-of-the-bahai-gardens-in-haifa-on-the-steep-slope-of-mount-carmel-great-view-of-the-city-and-the-mediterranean-sea-cactus-palm-trees-2M79D5J.jpg "
u1 =  "https://upload.wikimedia.org/wikipedia/commons/f/ff/Bat_eared_fox_Kenya_crop.jpg"
url =u0
img = io.imread(url)
cv2_imshow(img)
#-----------
# load image and select x, y coordinates to test
import cv2


image_path = './test.jpg'
if not os.path.exists(image_path):
  #!wget https://utils-computervisiondeveloper.s3.amazonaws.com/media/public/test.jpg
  !wget https://upload.wikimedia.org/wikipedia/en/0/0e/Mary_Anne_Trump.jpg
x = 528
y = 606

image = cv2.imread(image_path)
u5 ="https://raw.githubusercontent.com/bnsreenu/python_for_microscopists/master/images/monkey.jpg"

