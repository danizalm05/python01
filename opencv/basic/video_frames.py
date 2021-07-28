# -*- coding: utf-8 -*-
"""
'b'   98    backward 1 frame
'd'  100    backward 'frame_jump' frames
'f'  102    forward 1 frame
's'  115    save
'u'  117    forward 'frame_jump' frames
 how to capture one or more video frames from a MP4 video. 
 method 1: scan the video up to the wanted frame.
 method 2: go   to the wanted frame
""" 

import cv2
import numpy as np
import getpass
import imutils

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Videos/'
vid_name = "movie.mp4"   #"cars.mp4" "dog.mp4"
input_file = BASE_FOLDER + vid_name
print(input_file)
frame_name = 'frame_%d.jpg'

# method 1: scan the video up to the wanted frame.


frame_no = 20 # number  of first  frame
frame_jump = 10

vidcap = cv2.VideoCapture(input_file)
totalframecount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
if totalframecount == 0:
    print("Error: Video file does exists or empty file!")
    exit(-1)
print("Total number of frames = ", totalframecount)
success, image = vidcap.read()

# write output and extract more frames
counter = 0
while success:
    #cv2.imwrite((output_file) % counter, image)
    success, image = vidcap.read()
    counter += 1
    
    # break after reading the wanted frame
    if(counter >= frame_no):
        
        break;
        
#cv2.imshow((frame_name) % frame_no + "  method 1",image)
## go to the frame    


scaling_factor = 1.2
##############
#cv2.waitKey(0)
while True:
      vidcap.set(1, frame_no);  # Where frame_no is the frame you want
      ret, frame = vidcap.read()  # Read the frame
      #cv2.imshow((frame_name) % frame_no + "  method 2",frame)
      frame = cv2.resize(frame, None, fx=scaling_factor,
                         fy=scaling_factor, interpolation=cv2.INTER_AREA)
      cv2.imshow(vid_name, frame)
      c = cv2.waitKey(1)

      if c ==27: #esc
          break
      elif c == 115:# 's' save
          print("Save imge to  " + BASE_FOLDER+(frame_name) % frame_no)
          #cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  
          # save frame as JPEG file
          cv2.imwrite(BASE_FOLDER+(frame_name) % frame_no, frame)

      elif c==117: #  ('u')  move up
          frame_no += frame_jump
          if frame_no > totalframecount : frame_no =0
          print("Move to frame number[{:d}]".format(frame_no))
      elif c==102:#   'f'   forward 1 frame
          frame_no += 1
          if frame_no > totalframecount : frame_no =0
          print("Move to frame number[{:d}]".format(frame_no))
      elif c==98:#   'b''   backward 1 frame
          frame_no -= 1
          if frame_no < 0 : frame_no = totalframecount -1
          print("Move to frame number[{:d}]".format(frame_no))
      elif c==100: #  ('d')  move down
          frame_no -= frame_jump
          if frame_no < 0 : frame_no =  totalframecount -1
          print("Move to frame number[{:d}]".format(frame_no))


###########



cv2.destroyAllWindows()