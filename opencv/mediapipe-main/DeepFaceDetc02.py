'''
Facial landmark detector under mediapipe solutions full  486 points list
https://sefiks.com/2022/01/14/deep-face-detection-with-mediapipe/
https://www.youtube.com/watch?v=Yg6bFRnOSbs
'''

imgName = 'test9.jpeg'  #"cat-face.png"
scaling_factor = 0.4
import mediapipe
import cv2
import getpass


def readImagePath(imgName):
    BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
    BASE_FOLDER = BASE_FOLDER +'/Pictures/faces/'
    path = BASE_FOLDER+imgName
    print(path)

    return path


def getLandMark(lmk_index,landmarks_list,img):
    x = landmarks_list.landmark[lmk_index].x
    y = landmarks_list.landmark[lmk_index].y

    relative_x = int(img.shape[1] * x)
    relative_y = int(img.shape[0] * y)

    cv2.circle(img, (relative_x, relative_y), 15, (0, 200, 255), -1)

image_path = readImagePath(imgName)
img = cv2.imread(image_path)

#mp_face_detection = mediapipe.solutions.face_detection
#face_detector =  mp_face_detection.FaceDetection(
#           min_detection_confidence = 0.6)

mp_face_mesh = mediapipe.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode = True)

#Feed the facial image to facial landmark detector.
results = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


face_number = 0
#Store the facial landmarks information of the first face
landmarks = results.multi_face_landmarks[face_number]
for landmark in landmarks.landmark:
    x = landmark.x
    y = landmark.y
    relative_x = int(img.shape[1] * x)
    relative_y = int(img.shape[0] * y)
    cv2.circle(img, (relative_x, relative_y), 5, (0, 0, 255), -1)

up_lips = 12 # Upper_lips
low_lips =15
getLandMark(up_lips,landmarks,img)
getLandMark(low_lips,landmarks,img)



while True:
    img01 = cv2.resize(img, None, fx=scaling_factor,
                       fy=scaling_factor, interpolation=cv2.INTER_AREA)

    cv2.imshow("output",img01)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break
