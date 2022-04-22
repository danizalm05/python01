'''
Blink eye detecter and return the cordinate of the blink eye
https://medium.com/@asadullah92c/eyes-blink-detector-and-counter-mediapipe-a66254eb002c

'''

import KeyBoardModule as kb
import cv2 as cv
import numpy as np
import mediapipe as mp
import time

mp_face_mesh = mp.solutions.face_mesh

WHITE =(255, 255, 255)
keyboard_keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                  ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
                  ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]



# left eyes indices
LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
# right eyes indices
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]

# irises Indices list
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

cameraNum = 0  # -1 : image     0: video
frameWidth = 980
frameHeight = 480
scaling_factor = 2.5
Delay =  0.35
cap = cv.VideoCapture(0)

keybrd = kb.KeyBoard(keyboard_keys, '')# Initialize the virtual keyboard
buttonL = keybrd.CreateBtnlList()

ret, frame = cap.read()
img_h, img_w = frame.shape[:2]
mask = np.zeros((img_h, img_w), dtype=np.uint8)




with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
) as face_mesh:
    while True:
        ret, frame = cap.read()
        frame = cv.flip(frame, 1)

        frame = frame[20:320, 10:480]
        frame = cv.resize(frame, None, fx=scaling_factor,
                          fy=scaling_factor, interpolation=cv.INTER_AREA)
        if not ret:
            break
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        #frame = keybrd.DrawKeyBoard(frame, buttonL)
        img_h, img_w = frame.shape[:2]
        results = face_mesh.process(rgb_frame)
        mask = np.zeros((img_h, img_w), dtype=np.uint8)
        mask = keybrd.DrawKeyBoard(mask, buttonL)
        if results.multi_face_landmarks:


            mesh_points = \
                np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int)
                          for p in results.multi_face_landmarks[0].landmark])

            (l_cx, l_cy), l_radius = cv.minEnclosingCircle(mesh_points[LEFT_IRIS])
            (r_cx, r_cy), r_radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])
            center_left = np.array([l_cx, l_cy], dtype=np.int32)
            center_right = np.array([r_cx, r_cy], dtype=np.int32)
            cv.circle(frame, center_left, int(l_radius), (0, 255, 0), 2, cv.LINE_AA)
            cv.circle(frame, center_right, int(r_radius), (0, 255, 0), 2, cv.LINE_AA)

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
            cv.circle(mask, targetPoint, int(r_radius), (255, 255,255), 2, cv.LINE_AA)
            dm = mesh_points[15][1] - mesh_points[12][1]

            print('dm =',dm)
            if (dm < 15):  # close mouse and check blink left eye position
                cv.putText(mask, "dm" + str(upperLips), (20, 70), cv.FONT_HERSHEY_PLAIN,
                           4, (255, 255, 255), 3)
                cv.circle(mask, center_right, int(l_radius), (250, 250, 255), 6, cv.LINE_AA)
                keybrd.GetKey(targetPoint)#
                time.sleep(Delay)

            '''
            # blink eye
            dl = mesh_points[23][1] - mesh_points[159][1]
            dr = mesh_points[253][1] - mesh_points[385][1]
            #print('def[',dl, dr,'] ',center_right[0], center_right[1] )
            
            if (dl < 15):  # blink left eye
                cv.putText(frame, "Left " + str(center_right), (20, 70), cv.FONT_HERSHEY_PLAIN,
                           4, (0, 0, 255), 3)
                cv.circle(frame, center_right, int(l_radius), (25, 0, 255), 6, cv.LINE_AA)
                keybrd.GetKey(center_right[0],center_right[1])
                time.sleep(Delay)
            if (dr < 15):  # blink right eye
                cv.putText(frame, "Right " + str(center_left), (480, 70), cv.FONT_HERSHEY_PLAIN,
                           4, (255, 0, 0), 3)
                cv.circle(frame, center_left, int(l_radius), (255, 0, 0), 4, cv.LINE_AA)
                keybrd.GetKey(center_left[0], center_left[1])
                time.sleep(Delay)
             '''
            # drawing on the mask
            cv.circle(mask, center_left, int(l_radius), (255, 255, 255), -1, cv.LINE_AA)
            cv.circle(mask, center_right, int(r_radius), (255, 255, 255), -1, cv.LINE_AA)

        # output Window
        cv.rectangle(mask, (35, 70), (800, 120),
                      (255, 255, 255), cv.FILLED)
        cv.putText(mask, keybrd.msg, (37, 121),
                    cv.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 3)

        #cv.imshow('img', frame)
        cv.imshow('Mask', mask)
        key = cv.waitKey(1)

        if key == ord('q'):
            break
cap.release()
cv.destroyAllWindows()