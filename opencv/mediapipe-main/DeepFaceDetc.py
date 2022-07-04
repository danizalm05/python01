'''
Regular face detector
Facial Landmark Detection with MediaPipe in Python  10 main points
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

image_path = readImagePath(imgName)
img = cv2.imread(image_path)
mp_face_detection = mediapipe.solutions.face_detection
face_detector =  mp_face_detection.FaceDetection(
           min_detection_confidence = 0.6)

# Running The Detector

results = face_detector.process(img) # Pass the input image to the detector
if results.detections:
    for face in results.detections:
        confidence = face.score
        bounding_box = face.location_data.relative_bounding_box

        x = int(bounding_box.xmin * img.shape[1])
        w = int(bounding_box.width * img.shape[1])
        y = int(bounding_box.ymin * img.shape[0])
        h = int(bounding_box.height * img.shape[0])

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), thickness = 2)
landmarks = face.location_data.relative_keypoints


right_eye = (int(landmarks[0].x * img.shape[1]), int(landmarks[0].y * img.shape[0]))
left_eye = (int(landmarks[1].x * img.shape[1]), int(landmarks[1].y * img.shape[0]))
nose = (int(landmarks[2].x * img.shape[1]), int(landmarks[2].y * img.shape[0]))
mouth = (int(landmarks[3].x * img.shape[1]), int(landmarks[3].y * img.shape[0]))
right_ear = (int(landmarks[4].x * img.shape[1]), int(landmarks[4].y * img.shape[0]))
left_ear = (int(landmarks[5].x * img.shape[1]), int(landmarks[5].y * img.shape[0]))

cv2.circle(img, right_eye, 15, (0, 0, 255), -1)
cv2.circle(img, left_eye, 15, (0, 0, 255), -1)
cv2.circle(img, nose, 15, (0, 0, 255), -1)
cv2.circle(img, mouth, 15, (0, 0, 255), -1)
cv2.circle(img, right_ear, 15, (0, 0, 255), -1)
cv2.circle(img, left_ear, 15, (0, 0, 255), -1)

while True:
    img01 = cv2.resize(img, None, fx=scaling_factor,
                       fy=scaling_factor, interpolation=cv2.INTER_AREA)

    cv2.imshow("output",img01)
    key = cv2.waitKey(0)
'''
print(dir(results))
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', 
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
 '__match_args__', '__module__', '__mul__', '__ne__', '__new__',
  '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__',
   '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_asdict',
    '_field_defaults', '_fields', '_make', '_replace', 'count', 'detections',
     'index']


'''