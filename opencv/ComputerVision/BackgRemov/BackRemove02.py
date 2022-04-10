'''

Background Removal Like Zoom  Murtaza's Workshop
https://www.youtube.com/watch?v=k7cVPGpnels&list=PLMoSUbG1Q_r8jFS04rot-3NzidnV54Z2q&index=32
No source code  link
'''


import cv2
import getpass
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os


cameraNum = 0  # -1 : image     0: video
frameWidth = 640
frameHeight = 480


if (cameraNum == 0):
    cap = cv2.VideoCapture(cameraNum)  # Camera
    #cap = cv2.VideoCapture("C:/Users/rockman/Videos/Captures/cars.mp4")#video file

BASE_FOLDER = 'C:/Users/' + getpass.getuser()
BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
if (cameraNum == -1):

    path = BASE_FOLDER+'cat-face.png'   # 'b1.jpg'  'lambo.PNG''bb.jpg' 'p3.jpg' 'bz.jpg'
    print(path)
    img = cv2.imread(path)

if (cameraNum == 0):
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(cv2.CAP_PROP_FPS,60)

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()
listImg = os.listdir(BASE_FOLDER +'backimage/')# All image must be of size (frameWidth X frameHeight)
imgList = []

for imgPath in listImg:
   print(BASE_FOLDER +'backimage/'+imgPath)
   imgBack = cv2.imread(BASE_FOLDER +'backimage/'+imgPath)
   imgList.append(imgBack)


indexImg = 0

while True:
    if (cameraNum == 0):
        success, img = cap.read()

    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)

    imgStack = cvzone.stackImages([img, imgOut], 2,1)
    _, imgStack = fpsReader.update(imgStack, color = (0, 244, 0))

    cv2.imshow("image", imgStack)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg>0:
            indexImg -=1
    elif key == ord('d'):
        if indexImg<len(imgList)-1:
            indexImg +=1
    elif key == ord('q'):
        break