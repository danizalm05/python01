'''
Hand Tracking 30 FPS using CPU  Computer Vision 
https://www.youtube.com/watch?v=NZde8Xt78Iw&t=0s  26:01
hand gesture https://www.youtube.com/watch?v=9iEPzbG-xLE
'''



import mediapipe as mp
import numpy as np
import cv2
import time
import getpass
imgName = 'hand_pen.jpg'#'test4.jpg'

def readImagePath(imgName):
	BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
	BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
	path = BASE_FOLDER+imgName
	print(path)

	return path



#image_path = readImagePath(imgName)
#print('image_path =',image_path )

hands = mp.solutions.hands
hands_mesh = hands.Hands(static_image_mode=False,
                         min_detection_confidence=0.7)


draw = mp.solutions.drawing_utils

 
while True:
    n=2
     
    rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
    op = hands_mesh.process(rgb)
	# (op.multi_hand_landmarks) == true, means one or two hands are in view
    if op.multi_hand_landmarks:
     for i in op.multi_hand_landmarks:
      for id,lm in enumerate(i.landmark):
          #print(id, lm)
          h, w, c = frm.shape
          cx, cy = int(lm.x * w), int(lm.y * h)

          if id == 4: #tip  of the tomb
              print(id, cx, cy)
              cv2.circle(frm, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
      connect  = draw.DrawingSpec(thickness=1, color=(0,0,255))
      landmark = draw.DrawingSpec(color = (255, 100,0),circle_radius=4, thickness=2)
      draw.draw_landmarks(frm, i, hands.HAND_CONNECTIONS,
				        landmark_drawing_spec= landmark,
				         connection_drawing_spec = connect)
    
     
   
     

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0) 
    
    while True:
        _, frm = cap.read()
        rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(frm, f'FPS: {int(fps)}', (10, 60), 
             cv2.FONT_HERSHEY_PLAIN, 3, (255 , 220, 0), 2)

        cv2.imshow("window", frm)
       
        if cv2.waitKey(1) == 27:
          cv2.destroyAllWindows()
          cap.release()
          break
      
        
      
if __name__ == "__main__":
    main()  