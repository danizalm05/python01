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

mp_face_mesh = mediapipe.solutions.face_mesh