# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:26:05 2026


"""

import cv2
from mediapipe.tasks.python.vision import face_detection
from mediapipe.tasks.python import python

# --- יצירת mp_face_detection (כמו בקוד הישן) ---
class MPFaceDetection:
    def __init__(self, min_detection_confidence=0.5, model_selection=0):
        options = face_detection.FaceDetectorOptions(
            model_selection=model_selection,
            min_detection_confidence=min_detection_confidence
        )
        self.detector = face_detection.FaceDetector.create_from_options(options)
    
    def detect(self, image):
        """
        image: numpy array (BGR כמו OpenCV)
        מחזיר רשימת bounding boxes של הפנים
        """
        mp_image = python.Image(image_format=python.ImageFormat.SRGB, data=image)
        result = self.detector.detect(mp_image)
        boxes = []
        if result.detections:
            for face in result.detections:
                # ממיר ל-bbox בפורמט (x, y, width, height)
                bbox = face.bounding_box
                boxes.append((
                    bbox.origin_x,
                    bbox.origin_y,
                    bbox.width,
                    bbox.height
                ))
        return boxes

# --- שימוש בדימוי ---
# מחליף את הקוד הישן:
# mp_face_detection = mp.solutions.face_detection
mp_face_detection = MPFaceDetection(min_detection_confidence=0.5)

# קריאת תמונה לדוגמה
image = cv2.imread("4.jpg")

# זיהוי הפנים
faces = mp_face_detection.detect(image)

# הצגת התוצאות
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
