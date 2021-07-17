'''
Create Cartoon Characters in Live Webcam Stream
How to convert the foreground characters of a live webcam
feed to become cartoons, while keeping the background as it is.
https://www.learnpythonwithrune.org/create-cartoon-characters-in-live-webcam-stream-with-opencv-and-python/
https://www.learnpythonwithrune.org/start-opencv-with-python/
'''


import cv2
import numpy as np

# Setup camera
cap = cv2.VideoCapture(0)
u0 = " "
cap = cv2.VideoCapture(u0)
# Set a smaller resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Just a dummy frame, will be overwritten
last_foreground = np.zeros((480, 640), dtype='uint8')
while True:
    # Capture frame-by-frame
    _, frame = cap.read()
    # Only needed if you webcam does not support 640x480
    frame = cv2.resize(frame, (640, 480))
    # Flip it to mirror you
    frame = cv2.flip(frame, 1)
    # Convert to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Keep the foreground
    foreground = gray
    # Take the absolute difference
    abs_diff = cv2.absdiff(foreground, last_foreground)
    # Update the last foreground image
    last_foreground = foreground
    _, mask = cv2.threshold(abs_diff, 20, 255, cv2.THRESH_BINARY)
    #Threshold makes the image black and white. This helps it
    # to become easier  to detect the moving parts.

    mask = cv2.dilate(mask, None, iterations=3)
    se = np.ones((85, 85), dtype='uint8')
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, se)

  # Creating cartoon effect and mask it into the foreground
    frame_effect = cv2.stylization(frame, sigma_s=150, sigma_r=0.25)
    idx = (mask > 1)
    frame[idx] = frame_effect[idx]
    cv2.imshow('WebCam (Mask)', mask)
    cv2.imshow('WebCam (frame)', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()