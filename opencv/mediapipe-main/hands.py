'''
Hand Tracking 30 FPS using CPU  Computer Vision 
https://www.youtube.com/watch?v=NZde8Xt78Iw&t=0s  15:01
hand gesture https://www.youtube.com/watch?v=9iEPzbG-xLE
'''



import mediapipe as mp
import numpy as np
import cv2
import getpass
imgName = 'hand_pen.jpg'#'test4.jpg'

def readImagePath(imgName):
	BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
	BASE_FOLDER = BASE_FOLDER +'/Pictures/Saved Pictures/'
	path = BASE_FOLDER+imgName
	print(path)

	return path


cap = cv2.VideoCapture(0)
#image_path = readImagePath(imgName)
#print('image_path =',image_path )

hands = mp.solutions.hands
hands_mesh = hands.Hands(static_image_mode=False,
                         min_detection_confidence=0.7)


draw = mp.solutions.drawing_utils
#frm = cv2.imread(image_path )
while True:

	_, frm = cap.read()
	rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
	op = hands_mesh.process(rgb)
	# (op.multi_hand_landmarks) == true, means one or two hands are in view
	if op.multi_hand_landmarks:
	 for i in op.multi_hand_landmarks:

		 connect  = draw.DrawingSpec(thickness=1, color=(0,0,255))
		 landmark = draw.DrawingSpec(color = (255, 100,0),circle_radius=4, thickness=2)

		 draw.draw_landmarks(frm, i, hands.HAND_CONNECTIONS,
				        landmark_drawing_spec= landmark,
				         connection_drawing_spec = connect)


	cv2.imshow("window", frm)
	#cv2.imwrite("hand.jpg", frm)

	if cv2.waitKey(1) == 27:
		cv2.destroyAllWindows()
		cap.release()
		break