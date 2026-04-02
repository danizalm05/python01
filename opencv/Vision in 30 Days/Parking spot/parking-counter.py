# -*- coding: utf-8 -*-
"""
  
  https://www.youtube.com/watch?v=F-884J2mnOY&list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&index=16
  https://youtu.be/F-884J2mnOY?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=524
  https://github.com/computervisioneng/parking-space-counter

data:
  https://drive.google.com/drive/folders/1CjEFWihRqTLNUnYRwHXxGAVwSXF2k8QC
  masks:
   https://github.com/computervisioneng/parking-space-counter/blob/master/mask_1920_1080.png
   https://github.com/computervisioneng/parking-space-counter/blob/master/mask_crop.png

"""
import cv2 
import getpass
 

 
BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Videos/'
vid_name = "parking_crop_loop.mp4" 
input_file = BASE_FOLDER + vid_name
print(input_file)

cap = cv2.VideoCapture(input_file)
# Check if camera opened successfully:
if cap.isOpened()is False:
    print("Error opening video stream or file")



cap.release()
cv2.destroyAllWindows()    