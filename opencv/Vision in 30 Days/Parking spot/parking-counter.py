# -*- coding: utf-8 -*-
"""
  
  https://www.youtube.com/watch?v=F-884J2mnOY&list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&index=16
 
  https://youtu.be/F-884J2mnOY?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=2821
 
  https://github.com/computervisioneng/parking-space-counter

data:
  https://drive.googQle.com/drive/folders/1CjEFWihRqTLNUnYRwHXxGAVwSXF2k8QC
  masks:
   https://github.com/computervisioneng/parking-space-counter/blob/master/mask_1920_1080.png
   https://github.com/computervisioneng/parking-space-counter/blob/master/mask_crop.png


next chapter :
  
Machine learning web app with Python, Streamlit & Segment Anything Model | Modelbit model deployment 
      https://www.youtube.com/watch?v=W8OvdQPL7lk&list=PLb49csYFtO2HGELdc-RLRCNVNy0g2UMwc&index=20
      
"""
import cv2 
import getpass
from util import get_parking_spots_bboxes, empty_or_not
 
import numpy as np


def calc_diff(im1, im2): # Smilarity between two images
    return np.abs(np.mean(im1) - np.mean(im2))

#Read the mask image
#img=  'mask_crop.png'  
img = 'mask_1920_1080.png'
MASK_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
mask = MASK_FOLDER+img
mask = cv2.imread(mask, 0)# 0 = gray scale

#Open the video  
VID_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Videos/'
vid_name = "parking_1920_1080_loop.mp4" #"parking_1920_1080.mp4" #  "parking_crop_loop.mp4" 

input_file = VID_FOLDER + vid_name

cap = cv2.VideoCapture(input_file)
# Check if video opened successfully:
if cap.isOpened()is False:
    print("Error opening video stream or file")

 

connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)

spots = get_parking_spots_bboxes(connected_components)

spots_status = [None for j in spots]
diffs = [None for j in spots]

previous_frame = None

frame_nmr = 0
ret = True
step = 30
while ret:
    ret, frame = cap.read()

    if frame_nmr % step == 0 and previous_frame is not None:
        for spot_indx, spot in enumerate(spots):
            x1, y1, w, h = spot

            spot_crop = frame[y1:y1 + h, x1:x1 + w, :]

            diffs[spot_indx] = calc_diff(spot_crop, previous_frame[y1:y1 + h, x1:x1 + w, :])

        #print([diffs[j] for j in np.argsort(diffs)][::-1])

    if frame_nmr % step == 0:
        if previous_frame is None:
            arr_ = range(len(spots))
        else:
            arr_ = [j for j in np.argsort(diffs) if diffs[j] / np.amax(diffs) > 0.4]
        for spot_indx in arr_:
            spot = spots[spot_indx]
            x1, y1, w, h = spot

            spot_crop = frame[y1:y1 + h, x1:x1 + w, :]

            spot_status = empty_or_not(spot_crop)

            spots_status[spot_indx] = spot_status

    if frame_nmr % step == 0:
        previous_frame = frame.copy()

    for spot_indx, spot in enumerate(spots):
        spot_status = spots_status[spot_indx]
        x1, y1, w, h = spots[spot_indx]

        if spot_status:
            frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
        else:
            frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)

    cv2.rectangle(frame, (80, 20), (550, 80), (0, 0, 0), -1)
    cv2.putText(frame, 'Available spots: {} / {}'.format(str(sum(spots_status)), str(len(spots_status))), (100, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    frame_nmr += 1

cap.release()
cv2.destroyAllWindows() 