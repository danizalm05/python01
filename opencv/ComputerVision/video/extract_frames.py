import getpass
import sys
import cv2
import matplotlib.pyplot as plt
''' 

'b'   98    backward 1 frame
'd'  100    backward 'frame_jump' frames
'f'  102    forward 1 frame
's'  115    save
'u'  117    forward 'frame_jump' frames
'''
scaling_factor = 0.7
vid_name = "dog.mp4"    # l.mkv "m.mp4"
frame_jump = 100
frame_no = 65
frame_name = 'frame_%d.jpg'
BASE_FOLDER = 'C:/Users/' +  getpass.getuser() +'/Videos/Captures/'


def readImagePath():
    input_file = BASE_FOLDER + vid_name
    return input_file


input_video_file = readImagePath()

print(input_video_file)


vidcap = cv2.VideoCapture(input_video_file)
totalframecount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
if totalframecount == 0:
    print("Error: Video file does exists or empty file!")
    exit(-1)
print (f'Video [{input_video_file}] Frame count is {totalframecount}')

#m.mp4  5   mkv 1
while True:
   vidcap.set(1, frame_no );  # Where frame_no is the frame you want
   ret, frame = vidcap.read()
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
       frame01 = cv2.resize(frame, None, fx=1,
                          fy=1, interpolation=cv2.INTER_AREA)
       cv2.imwrite(BASE_FOLDER+'/frame/'+(frame_name) % frame_no, frame01)

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
