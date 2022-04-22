# Module Detect 468 Face Landmarks in Real-time
# https://www.youtube.com/watch?v=V9bzew8A1tc  21:12
# https://www.computervision.zone/lessons/code-files-16/

import cv2
import getpass
import mediapipe as mp
import time


class FaceMeshDetector():

    def __init__(self, staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5):

        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)

    def findFaceMesh(self, img, draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:#scan all the faces
            for faceLms in self.results.multi_face_landmarks:#scan one face
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms,
                                               self.mpFaceMesh.FACEMESH_CONTOURS,
                                               self.drawSpec, self.drawSpec)
                face = []
                for id, lm in enumerate(faceLms.landmark):
                    # print(lm)
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)

                    if (id == 33):  # The tip of the nose id =1 tip of uper lips id = 0 id =467
                        cv2.circle(img, center=(x, y), radius=10, color=(0, 255, 0), thickness=2)
                        # Write TEXT of the id on the image
                        cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN,
                                  2.7, (255, 0, 0), 2)
                    # print(id,x,y)
                    face.append([x, y])#Add the lm to the lm list
                faces.append(face)
        return img, faces

def main():
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
        #cap = cv2.VideoCapture(cameraNum)  # video Camera

    if (cameraNum == -1):
        BASE_FOLDER = 'C:/Users/' + getpass.getuser()
        BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
        path = BASE_FOLDER + 'lady0.jpg'  # 'b1.jpg'  'lambo.PNG''bb.jpg' 'p3.jpg' 'bz.jpg'
        print(path)
        img = cv2.imread(path)
        img = cv2.resize(img, None, fx=scaling_factor,
                         fy=scaling_factor, interpolation=cv2.INTER_AREA)
    if (cameraNum == 0):
        cap.set(3, frameWidth)
        cap.set(4, frameHeight)
        cap.set(cv2.CAP_PROP_FPS, 60)

    slowMotion =5

    pTime = 0
    detector = FaceMeshDetector(maxFaces=3)
    while True:
        if (cameraNum == 0):
            success, img = cap.read()
            img = cv2.resize(img, None, fx=scaling_factor,
                         fy=scaling_factor, interpolation=cv2.INTER_AREA)
        img, faces = detector.findFaceMesh(img,True)#True Draw False not Draw
        # faces = list of lm of a face
        if len(faces) != 0: #len faces = number of faces. face[0] =list of lm of 1'st face
            print(len(faces[0]))
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 255, 0), 3)
        cv2.imshow("Image", img)


        key = cv2.waitKey(slowMotion)

        if key == ord('q'):
            break


if __name__ == "__main__":
    main()
