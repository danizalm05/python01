'''
Virtual keyboard
Return the coordinate of the tip of node. Close your lips to select a key
https://medium.com/@asadullah92c/eyes-blink-detector-and-counter-mediapipe-a66254eb002c
if import mediapipe as mp   cuses error try  to  run
     pip install 'protobuf~=3.19.0'
'''

import KeyBoardModule as Kb
import cv2 as cv
import numpy as np
import mediapipe as mp
import time



mp_face_mesh = mp.solutions.face_mesh

WHITE =(255, 255, 255)

cameraNum = 0  # -1 : image     0: video
frameWidth = 1380
frameHeight = 480
scaling_factor = 1.8
Delay =  0.35

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
cap.set(3, frameHeight)
cap.set(4, frameWidth)
font = cv.FONT_HERSHEY_SIMPLEX

keybrd = Kb.KeyBoard(Kb.keyboard_keys, '')# Initialize the virtual keyboard
buttonL = keybrd.CreateBtnlList()

ret, frame = cap.read()
img_h, img_w = frame.shape[:2]
mask = np.zeros((img_h, img_w), dtype=np.uint8)


face_mesh = mp_face_mesh.FaceMesh(  max_num_faces=1,   refine_landmarks=True,
                       min_detection_confidence=0.5,   min_tracking_confidence=0.5  )

fontScale = 1
thickness = 2

while True:
        ret, frame = cap.read()
        frame = cv.flip(frame, 1)

        frame = frame[ 0:420,  0:1080]
        frame = cv.resize(frame, None, fx=scaling_factor,
                          fy=scaling_factor, interpolation=cv.INTER_AREA)
        if not ret:
            break
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        img_h, img_w = frame.shape[:2]
        results = face_mesh.process(rgb_frame)

        '''
        Results store the facial landmarks information. It is a python
         list  length of number of faces in the image. 
          '''
        mask = np.zeros((img_h, img_w), dtype=np.uint8)
        mask = keybrd.DrawKeyBoard(mask, buttonL)
        if results.multi_face_landmarks:


            mesh_points = \
                np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int)
                          for p in results.multi_face_landmarks[0].landmark])

            #Mouth
            upperLips=[mesh_points[12][0] ,  mesh_points[12][1]]

            lowLips = [mesh_points[15][0], mesh_points[15][1]]
            cv.circle(mask, upperLips, 5, WHITE, -1, cv.LINE_AA)
            cv.circle(mask,  lowLips, 5, WHITE, -1, cv.LINE_AA)
            cv.line(mask, upperLips, lowLips,  WHITE, 2)
            #horz Mouth
            cv.line(mask,[mesh_points[185][0] ,  mesh_points[185][1]],
                     [mesh_points[407][0] ,  mesh_points[407][1]], WHITE, 2)
            #lower chin
            cv.line(mask, [mesh_points[176][0], mesh_points[176][1]],
                    [mesh_points[400][0], mesh_points[400][1]], WHITE, 2)
            targetPoint = [mesh_points[1][0], mesh_points[1][1]] #  tip of nose
            cv.circle(mask, targetPoint, 30, (255, 255,255), 2, cv.LINE_AA)
            dm0 = mesh_points[15][0] - mesh_points[12][0]# y coordinate difference
            dm1 = mesh_points[15][1] - mesh_points[12][1]# x coordinate difference
            dmp = pow (pow (dm0,2)+pow(dm1,2),0.5)#distance between upper and lower lips

            print('dm0 =',dm0 ,'dm1 =',dm1,'dmp =',dmp)
            if (dmp < 15):  # Is  mouse  is closed
                cv.putText(frame, "dm" + str(upperLips), (20, 70),font,fontScale, WHITE, 3)
                keybrd.GetKey(targetPoint)
                time.sleep(Delay)
            cv.putText(frame, keybrd.msg, (27, 170),font,fontScale,WHITE, thickness)

        # output Window
        cv.rectangle(mask, ( 5, 30), (800,80), WHITE, cv.FILLED)
        cv.putText(mask, keybrd.msg, (37, 80), font,fontScale, WHITE, thickness)

        cv.imshow('img', frame)
        cv.imshow('Mask', mask)

        key = cv.waitKey(1)

        if key == ord('q'):
            break

cap.release()
cv.destroyAllWindows()