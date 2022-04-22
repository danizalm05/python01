# Detect 468 Face Landmarks in Real-time
# https://www.youtube.com/watch?v=V9bzew8A1tc
# https://www.computervision.zone/lessons/code-files-16/

import cv2
import getpass
import urllib.request as urlreq  # used for accessing url to download files
import os  # used to access local directory
import matplotlib.pyplot as plt  # used to plot our images
from pylab import rcParams  # used to change image size
import mediapipe as mp
import time

cameraNum = 0  # -1 : image     0: video
frameWidth = 640
frameHeight = 480
scaling_factor = 0.3

if (cameraNum == 0):
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Videos/Captures/'
    path = BASE_FOLDER + '2.mp4'  # 'PianoChords.mp4' '2.mp4' 'dog.mp4' 'dance.mp4'

    cap = cv2.VideoCapture(path)  # video file
    print(path)
    # cap = cv2.VideoCapture(cameraNum)  # video Camera
cap.set(3, frameWidth)
cap.set(4, frameHeight)
# cap.set(cv2.CAP_PROP_FPS,60)

img = cv2.imread(path)
pTime = 0
slowMotion = 20
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=3)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while True:
    if (cameraNum == 0):
        success, img = cap.read()

    img = cv2.resize(img, None, fx=scaling_factor,
                     fy=scaling_factor, interpolation=cv2.INTER_AREA)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            # mpFaceMesh.FACE_CONNECTIONS  .FACEMESH_CONTOURS
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS,
                                  drawSpec, drawSpec)
            for id, lm in enumerate(faceLms.landmark):
                ih, iw, ic = img.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                print(id, x, y)
                if (id  == 467) : #The tip of the nose id =1 tip of uper lips id = 0 id =467
                    cv2.circle(img, center=(x, y), radius=10, color=(255, 0, 0), thickness=2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)
    cv2.imshow("image", img)
    key = cv2.waitKey(slowMotion)

    if key == ord('q'):
        break
