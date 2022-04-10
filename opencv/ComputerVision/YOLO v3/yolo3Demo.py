#  yalo3Demo.py
#  YOLO: Real-Time Object Detection
#  part 1 https://www.youtube.com/watch?v=GGeF_3QOHGE&t=144s
#  part 2 https://www.youtube.com/watch?v=9AycYn9gj1U
#  part 3 https://www.youtube.com/watch?v=xK4li3jinSw&list=PLMoSUbG1Q_r8nz4C5Yvd17KaXy8p0ufPH&index=3
#  part 4 https://www.youtube.com/watch?v=Sp9mEGubBJs&list=PLMoSUbG1Q_r8nz4C5Yvd17KaXy8p0ufPH&index=4
#  https://www.computervision.zone/courses/object-detection-yolo/
#  https://www.computervision.zone/topic/complete-code-5/
#  Website: https: // www.computervision.zone
#Download the next files
#  1.
#  coco.names  URL:
#  https://usercontent.one/wp/www.computervision.zone/wp-content/uploads/2020/06/cocoNames.zip?media=1632743877
# The cfg and the weight files can be downloaded from the
# official yolo website.
#
#2.
#   320 version:
#   file yolov3.weights URL : https://pjreddie.com/media/files/yolov3.weights
#   file yolov3.cfg     URL :https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg
#3.
#  Tiny version:
#    file  yolov3-tiny.weights  URL https://pjreddie.com/media/files/yolov3-tiny.weights
#    file  yolov3-tiny.cfg    URL:https://github.com/pjreddie/darknet/blob/master/cfg/yolov3-tiny.cfg
#
# D:\dmyd\networks\python

import cv2

import numpy as np
import getpass

cameraNum = 0  #  -1 : image     0: video
whT = 320
confThreshold =0.5
nmsThreshold= 0.3

if (cameraNum == 0):
    #cap = cv2.VideoCapture(cameraNum)# Camera
    cap = cv2.VideoCapture("C:/Users/rockman/Videos/Captures/cars.mp4")#video file
######################## READ IMAGE ############################

if (cameraNum == -1):
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
    path = BASE_FOLDER+'cat-face.png'   # 'b1.jpg'  'lambo.PNG''bb.jpg' 'p3.jpg' 'bz.jpg'
    print(path)
    img = cv2.imread(path)
 


#### LOAD MODEL
## Coco Names
classesFile = "coco.names"
classNames = []
with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')# Exterct base on new line
print("Number of class Names = ",len(classNames),'\n', classNames)

## Model Files
CFG_FOLDER = 'D:/dmyd/networks/python/'
# yolov3-tiny is faster but less  reliable
modelConfiguration = CFG_FOLDER + 'yolov3-tiny.cfg' #'yolov3.cfg' 'yolov3-tiny.cfg'
modelWeights = CFG_FOLDER +   'yolov3-tiny.weights' #yolov3.weights' 'yolov3-tiny.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
##########
def findObjects(outputs, img):
    hT, wT, cT = img.shape
    bbox = [] # Bounding box
    classIds = []
    confs = [] # Confidence  value
    for output in outputs:
        for det in output:  # Detection in output Find the highest probability
            scores = det[5:] # Remove first 5 elements
            classId = np.argmax(scores)# Find index of maxvalue
            confidence = scores[classId] # Get the actual maxvalue
            if confidence > confThreshold:
                w, h = int(det[2] * wT), int(det[3] * hT)
                # x,y are the center points
                x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))
    # Remove over lapping boxes
    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)

    for i in indices:
        #print("len(indices) = ", len(indices), " i= ", i )
        #i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        # print(x,y,w,h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 1)
        cv2.putText(img,
             f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%',
             (x, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,250, 25 ), 1)


#####
while cv2.waitKey(1) != 27:

    if (cameraNum == 0):
                success, img = cap.read()
    # blob is another  format for images
    blob = cv2.dnn.blobFromImage(
                     img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
    net.setInput(blob)
    layersNames = net.getLayerNames()
    #print(len(layersNames), " ",layersNames)#254 layers
    outputNames = [(layersNames[i - 1]) for i in net.getUnconnectedOutLayers() ]
    #print(outputNames)
    outputs = net.forward(outputNames)
    findObjects(outputs, img)
    #print(outputs[0].shape,outputs[1].shape,outputs[2].shape)
    cv2.imshow("Image", img)
