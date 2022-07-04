'''
Face Mesh | mediapipe | deep learning
https://www.youtube.com/watch?v=7WPdEajSL6c
https://github.com/Pawandeep-prog/mediapipe
Reference: https://google.github.io/mediapipe/solutions/face_mesh.html
5:50
'''


import mediapipe as mp
import numpy as np
import cv2

scaling_factor = 1.8

cap = cv2.VideoCapture(0)

facmesh = mp.solutions.face_mesh
face = facmesh.FaceMesh(static_image_mode=True, min_tracking_confidence=0.6, min_detection_confidence=0.6)
draw = mp.solutions.drawing_utils



while True:

	_, frm = cap.read()
	frm = cv2.resize(frm, None, fx=scaling_factor,
					   fy=scaling_factor, interpolation=cv2.INTER_AREA)
	#break
	rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)

	op = face.process(rgb)
	#print(dir(op))#Print all  possible  commands
	#print('----',op.multi_face_landmarks)
	if op.multi_face_landmarks:
		for i in op.multi_face_landmarks:
			print('--',i.landmark[0].y*480,i.landmark[0].x*640)
			draw.draw_landmarks(frm, i, facmesh.FACEMESH_CONTOURS,
						 landmark_drawing_spec=draw.DrawingSpec(
							           color=(255,0  , 255),
							           circle_radius=2))


	cv2.imshow("window", frm)

	if cv2.waitKey(1) == 27:
		cap.release()
		cv2.destroyAllWindows()
		break
