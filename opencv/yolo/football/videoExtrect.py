'''
 Exreact fram from a video 

online version:
https://frame-extractor.com/en/extract 

YouTube Video Downloader:
   https://sceneform.ai/tools/youtube-video-downloader?task_id=4adbf356-63fd-43fa-a5fc-4ce3e66376b9 


commands
'b'   98    backward 1 frame
'f'  102    forward 1 frame

'u'  117    forward 'frame_jump' frames
'd'  100    backward 'frame_jump' frames

's'  115    save
'q'  115    quit
'''

import getpass
import cv2



vid= 'football.mp4' #    'los_angeles.mp4'   'dog.mp4''afriq0.MP4'
 
BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Videos/'
OUTPUT_FOLDER= BASE_FOLDER +'Captures/'
video_name = BASE_FOLDER+vid
#print("Image  = ",video_name ) 

# Vals to resize video frames | small frame optimise the run
frame_wid = 640
frame_hyt = 480


cap = cv2.VideoCapture(video_name )

if not cap.isOpened():
    print("Cannot open video")
    exit()

totalframecount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_jump = 100
frame_no = 1
frame_name = 'frame_%d.jpg'
while True:
    # Capture frame-by-frame
    cap.set(1, frame_no )
    ret, frame = cap.read()
    
    if not ret:
       print("Can't receive frame (stream end?). Exiting ...")
       break
       
           

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # Terminate run when "Q" pressed
    c =  cv2.waitKey(20)
    if c & 0xFF == ord('q'):
          break
    elif c == 115:# 's' save
       name = OUTPUT_FOLDER+(frame_name) % frame_no
       print("Save image to  " + name)
       
       #cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)
       # save frame as JPEG file
       frame01 = cv2.resize(frame, None, fx=2,
                          fy=2, interpolation=cv2.INTER_AREA)
   
       cv2.imwrite(name, frame01)
       print(name)
       

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

cap.release() 

cv2.destroyAllWindows()  