'''
Facial Landmarks
Using 'haarcascade_frontalface_alt2.xml'
https://medium.com/analytics-vidhya/facial-landmarks-and-face-detection-in-python-with-opencv-73979391f30e
'''



import getpass
import cv2 # opencv 4.1.2 to read images
import urllib.request as urlreq # used for accessing url to download files
import os # used to access local directory
import matplotlib.pyplot as plt # used to plot our images
from pylab import rcParams # used to change image size

# Local image
BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
path = BASE_FOLDER+'lena.png'  #'b1.jpg' 'lena.png' 'bb.jpg'
print(path)

# save picture's url in pics_url variable
pics_url = "https://static.timesofisrael.com/www/uploads/2019/02/F190207TNFF18.jpg"
#pics_url = " "
pic = "image.jpg" # save picture's name as pic

# download picture from url and save locally as image.jpg
urlreq.urlretrieve(pics_url, pic)


image = cv2.imread(pic)
cv2.imshow("Benet", image)

# convert image to RGB colour
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow("image_rgb", image_rgb)
# set dimension for cropping image
x, y, width, depth = 250, 100, 950,700
#image_cropped = image_rgb[y:(y+depth), x:(x+width)]
image_cropped = image_rgb

image_template = image_cropped.copy() # A copy of the cropped image
image_gray = cv2.cvtColor(image_cropped, cv2.COLOR_BGR2GRAY)

cv2.imshow("image_gray", image_gray)


cv2.waitKey(0)

# save face detection algorithm's url in haarcascade_url variable
haarcascade_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_alt2.xml"

# save face detection algorithm's name as haarcascade
haarcascade = "haarcascade_frontalface_alt2.xml"

# chech if file is in working directory
if (haarcascade in os.listdir(os.curdir)):
    print("File exists")
else:
    # download file from url and save locally as haarcascade_frontalface_alt2.xml, < 1MB
    urlreq.urlretrieve(haarcascade_url, haarcascade)
    print("File downloaded")

# create an instance of the Face Detection Cascade Classifier
detector = cv2.CascadeClassifier(haarcascade)

# Detect faces using the haarcascade classifier on the "grayscale image"
faces = detector.detectMultiScale(image_gray)

# Print coordinates of detected faces
print("Faces:\n", faces)

for face in faces:
#     save the coordinates in x, y, w, d variables
    (x,y,w,d) = face
    # Draw a white coloured rectangle around each face using the face's coordinates
    # on the "image_template" with the thickness of 2
    cv2.rectangle(image_template,(x,y),(x+w, y+d),(255, 255, 255), 2)



cv2.imshow("Face Detection", image_template)


cv2.waitKey(0)




# save facial landmark detection model's url in LBFmodel_url variable
LBFmodel_url = "https://github.com/kurnianggoro/GSOC2017/raw/master/data/lbfmodel.yaml"

# save facial landmark detection model's name as LBFmodel
LBFmodel = "lbfmodel.yaml"

# check if file is in working directory
if (LBFmodel in os.listdir(os.curdir)):
    print("File exists")
else:
    # download from url and save locally as lbfmodel.yaml, < 54MB
    urlreq.urlretrieve(LBFmodel_url, LBFmodel)
    print("File downloaded")

# create an instance of the Facial landmark Detector with the model
landmark_detector = cv2.face.createFacemarkLBF()
landmark_detector.loadModel(LBFmodel)


# Detect landmarks on "image_gray"
_, landmarks = landmark_detector.fit(image_gray, faces)


for landmark in landmarks:
    for x,y in landmark[0]:
        xx = int(x)
        yy = int(y)
		# display landmarks on "image_cropped"
		# with white colour in BGR and thickness 1
        cv2.circle(image_cropped, (xx, yy), 5, (255, 0, 0), 3)


cv2.imshow("image_cropped01", image_cropped)


cv2.waitKey(0)