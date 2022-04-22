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

import TrackBars # This file is in the same directory
TrackBars.initializeTrackbars()





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
frameWidth = 780
frameHeight = 480
scaling_factor = 2.5
cap = cv.VideoCapture(0)

keybrd = kb.KeyBoard(keyboard_keys, 'final_text', [22,420])# Initialize the virtual keyboard
buttonL = keybrd.CreateBtnlList()
with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
) as face_mesh:
    while True:
        ret, frame = cap.read()
        frame = cv.flip(frame, 1)

        frame = frame[20:320, 10:410]
        frame = cv.resize(frame, None, fx=scaling_factor,
                          fy=scaling_factor, interpolation=cv.INTER_AREA)
        if not ret:
            break
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        frame = keybrd.DrawKeyBoard(frame, buttonL)
        img_h, img_w = frame.shape[:2]
        results = face_mesh.process(rgb_frame)
        mask = np.zeros((img_h, img_w), dtype=np.uint8)

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

            # blink eye
            dl = mesh_points[23][1] - mesh_points[159][1]
            dr = mesh_points[253][1] - mesh_points[385][1]
            #print('def[',dl, dr,'] ',center_right[0], center_right[1] )

            if (dl < 15):  # blink left eye
                cv.putText(frame, "Left " + str(center_right), (20, 70), cv.FONT_HERSHEY_PLAIN,
                           4, (0, 0, 255), 3)
                cv.circle(frame, center_right, int(l_radius), (25, 0, 255), 6, cv.LINE_AA)
                keybrd.GetKey(center_right[0],center_right[1])
                time.sleep(0.2)
            if (dr < 15):  # blink right eye
                cv.putText(frame, "Right " + str(center_left), (480, 70), cv.FONT_HERSHEY_PLAIN,
                           4, (255, 0, 0), 3)
                cv.circle(frame, center_left, int(l_radius), (255, 0, 0), 4, cv.LINE_AA)
                keybrd.GetKey(center_left[0], center_left[1])
            # drawing on the mask
            cv.circle(mask, center_left, int(l_radius), (255, 255, 255), -1, cv.LINE_AA)
            cv.circle(mask, center_right, int(r_radius), (255, 255, 255), -1, cv.LINE_AA)

        cv.imshow('Mask', mask)
        cv.imshow('img', frame)
        key = cv.waitKey(1)
        if key == ord('q'):
            break
cap.release()
cv.destroyAllWindows()