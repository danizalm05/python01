'''
 Detecting color with Python and OpenCV using HSV colorspace  
 
 https://www.youtube.com/watch?v=eDIj5LuIL4A&list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=5493s
https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=8929
https://colorizer.org/
'''


import cv2
import numpy as np
from PIL import Image
from outputCV import stackImages,PutTextOnImage
from colorDetectInp import  inpTrackbar ,get_limits
inpWinName = "Input"

inpTrackbar(inpWinName)

chosenColor = [0, 255, 255]  # yellow in BGR colorspace
camera_num = 0
cap = cv2.VideoCapture(camera_num)

while True:
     scale = cv2.getTrackbarPos("scale", inpWinName) / 10

      # Input BGR  values of the color
     Red = cv2.getTrackbarPos("Red", inpWinName)
     Green = cv2.getTrackbarPos("Green", inpWinName)
     Blue = cv2.getTrackbarPos("Blue", inpWinName)

     chosenColor = [Blue, Green, Red]  # chosenColor in BGR colorspace
     c = np.uint8([[chosenColor]])  #   bgr values  to convert to hsv
     
      
   # ----------------------
     ret, frame = cap.read()
     colorBox = frame.copy()
     hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
     lowerLimit, upperLimit = get_limits(chosenColor)

     mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
     mask_ = Image.fromarray(mask)
     #Convert opencv image to pil image(Image is taken from PIL lib)
     #So we can use the next 'mask_.getbbox()' function
     bbox = mask_.getbbox()
     print(bbox)
     if bbox is not None:
         x1, y1, x2, y2 = bbox
         frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (250,  5, 0), 2)

    
     #Draw a rectangle using the color 'chosenColor'
     start_point = (45, 100)
     end_point = (200, 300)
     color = (255, 55, 0)
     thickness = -1
     colorBox = cv2.rectangle(colorBox, start_point, end_point, chosenColor, thickness)
     hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
     PutTextOnImage(colorBox,"bgr:"+ str(chosenColor)+'hsv:'+ str(hsvC))
   
     imgStack = stackImages( scale,  ([colorBox, frame, mask])    )
     cv2.imshow("ImageStack", imgStack)
     #cv2.imshow('frame', frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()

