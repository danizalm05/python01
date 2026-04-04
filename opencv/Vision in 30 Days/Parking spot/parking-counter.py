# -*- coding: utf-8 -*-
"""
  
  https://www.youtube.com/watch?v=F-884J2mnOY&list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&index=16
 
  https://youtu.be/F-884J2mnOY?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=954
  https://github.com/computervisioneng/parking-space-counter

data:
  https://drive.googQle.com/drive/folders/1CjEFWihRqTLNUnYRwHXxGAVwSXF2k8QC
  masks:
   https://github.com/computervisioneng/parking-space-counter/blob/master/mask_1920_1080.png
   https://github.com/computervisioneng/parking-space-counter/blob/master/mask_crop.png

"""
import cv2 
import getpass
from util import get_parking_spots_bboxes, empty_or_not


#Read the mask image
img=  'mask_crop.png'  
MASK_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
mask = MASK_FOLDER+img
mask = cv2.imread(mask, 0)# 0 = gray scale

#Open the video  
VID_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Videos/'
vid_name = "parking_crop_loop.mp4" 
input_file = VID_FOLDER + vid_name


cap = cv2.VideoCapture(input_file)
connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
spots = get_parking_spots_bboxes(connected_components)

# Check if camera opened successfully:
if cap.isOpened()is False:
    print("Error opening video stream or file")

ret = True
step = 30
while ret:
    ret, frame = cap.read()
    
    for spot_indx, spot in enumerate(spots):
        x1, y1, w, h = spot  
        frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)       


    #cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)   
    if cv2.waitKey(5) & 0xFF == ord('q'):
       break
   
    
   
cap.release()
cv2.destroyAllWindows()    