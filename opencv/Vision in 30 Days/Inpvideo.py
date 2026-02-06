'''
Read   video  file
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=1374
https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter1.py
'''

import cv2
import getpass
import os


frameWidth = 640
frameHeight = 480
BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
######################## READ IMAGE ############################
 
 
 
BASE_FOLDER = BASE_FOLDER +'/Videos/Captures/'
 
path = BASE_FOLDER+'dog.mp4'
print(path)

if os.path.isfile(path):
   success =  True
   cap = cv2.VideoCapture(path)
   while success:
     success, img = cap.read()
     img = cv2.resize(img, (frameWidth, frameHeight))
     cv2.imshow("Result", img)
     if cv2.waitKey(40) & 0xFF == ord('q'):
         break
else:
    print("ERROR --> Missing File: " + path   )
   
cv2.destroyAllWindows()    
cap.realse() 