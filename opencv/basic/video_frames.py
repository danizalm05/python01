# -*- coding: utf-8 -*-
"""
 how to capture one or more video frames from a MP4 video. 
 method 1: scan the video up to the wanted frame.
 method 2: go strait to the wanted frame
""" 

import cv2
import numpy as np
import getpass
import imutils

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Videos/Captures/'
vid_name = "misty.mp4"   #"cars.mp4" "dog.mp4"
input_file = BASE_FOLDER + vid_name
print(input_file)
frame_name = 'frame_%d.jpg'

# method 1: scan the video up to the wanted frame.
frame_no = 455 
counter = 0
 
# read first frame
vidcap = cv2.VideoCapture(input_file)


totalframecount= int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

print("Total number of frames = ", totalframecount)
success, image = vidcap.read()

# write output and extract more frames
while success:
    #cv2.imwrite((output_file) % counter, image)
    success, image = vidcap.read()
    counter += 1
    
    # break after reading the wanted frame
    if(counter >= frame_no):
        
        break;
        
#cv2.imshow((frame_name) % frame_no + "  method 1",image)
## go to the frame    
frame_no = 12000# number  of first  frame

 

##############
#cv2.waitKey(0)
while True:
      vidcap.set(1, frame_no);  # Where frame_no is the frame you want
      ret, frame = vidcap.read()  # Read the frame
      cv2.imshow((frame_name) % frame_no + "  method 2",frame)
     

      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
      elif cv2.waitKey(1) & 0xFF == ord('s'):
          print("Save imge to  " + BASE_FOLDER+(frame_name) % frame_no)
          #cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  
          # save frame as JPEG file
          cv2.imwrite(BASE_FOLDER+(frame_name) % frame_no, frame)

      elif cv2.waitKey(1) & 0xFF == ord('u'):#move up
          frame_no += 600
          print("Move to frame number[{:d}]".format(frame_no))


###########



cv2.destroyAllWindows()