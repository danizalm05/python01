# -*- coding: utf-8 -*-
"""
text-detection
www.youtube.com/watch?v=CcC3h0waQ6I&list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&index=5
https://youtu.be/CcC3h0waQ6I?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=388
https://github.com/computervisioneng/text-detection-python-tesseract-easyocr-textract/tree/main

https://bgshih.github.io/cocotext/
https://www.pexels.com/         search for text
"""
import cv2
import easyocr
import matplotlib.pyplot as plt
import getpass

img=  'txt1.jpg'  #'2.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
path = BASE_FOLDER+img
print("Image  = ",path) 
print("Image  shape  = ",path) 
img = cv2.imread(path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on image
text_ = reader.readtext(img)

threshold = 0.25
# draw bbox and text
for t_, t in enumerate(text_):
    #print(t)

    bbox, text, score = t

    if score > threshold:
        cv2.rectangle(img, [int(j) for j in bbox[0]], [int(j) for j in bbox[2]], (0, 255, 0), 15)
        cv2.putText(img, text, [int(j) for j in bbox[0]], cv2.FONT_HERSHEY_COMPLEX, 2.5, (0, 0, 255), 5)
        print(text)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()