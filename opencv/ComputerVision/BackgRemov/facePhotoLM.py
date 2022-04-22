# Facial landmarks whit python on a image
# https://pysource.com/2021/05/14/facial-landmarks-detection-with-opencv-mediapipe-and-python/

import cv2
import mediapipe as mp
import getpass

frameWidth = 640
frameHeight = 480
scaling_factor = 1.7
BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
######################## READ IMAGE ############################

BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
path = BASE_FOLDER+'lady0.jpg'  #'b1.jpg' 'lena.png' 'bb.jpg'
print(path)




img = cv2.imread(path)
img = cv2.resize(img, None, fx=scaling_factor,
                     fy=scaling_factor, interpolation=cv2.INTER_AREA)
cv2.imshow("Len", img)

#load face mesh and create an object for that.

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Facial landmarks
result = face_mesh.process(rgb_image)

height, width, _ = img.shape
for facial_landmarks in result.multi_face_landmarks:
    for i in range(0, 468):
        pt1 = facial_landmarks.landmark[i]
        x = int(pt1.x * width)
        y = int(pt1.y * height)
        cv2.circle(img, (x, y), 2, (200,  0, 0), -1)
        cv2.putText(img, f' {int(i)}', (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1, (0, 255, 0), 2)
        if (i==10):
            cv2.circle(img, (x, y), 7, (0, 0, 250), 2)

cv2.imshow("Image2", img)
cv2.waitKey(0)

