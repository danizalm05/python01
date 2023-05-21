
import cv2
from PIL import Image
from inpOpenCV import stackImages,PutTextOnImage, inpTrackbar, get_limits


inpWinName = "Input"
inpTrackbar(inpWinName)

camera_num = 0
scale = 0.4

chosenColor  = [255, 0, 0]  # yellow in BGR colorspace

#######################################
cap = cv2.VideoCapture(camera_num)
while True:
    ret, frame = cap.read()
    colorBox = frame.copy()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    scale = cv2.getTrackbarPos("scale", inpWinName) / 10

    # Input BGR  values of the wanted color
    Red = cv2.getTrackbarPos("Red", inpWinName)
    Green = cv2.getTrackbarPos("Green", inpWinName)
    Blue = cv2.getTrackbarPos("Blue", inpWinName)

    chosenColor = [Red, Green, Blue]  # chosenColor in BGR colorspace
    lowerLimit, upperLimit = get_limits(color =  chosenColor)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)

    cv2.imshow('frame', frame)
    start_point = (25, 25)
    end_point = (320, 320)
    color = (255, 55, 0)
    thickness = -1
    colorBox = cv2.rectangle(colorBox, start_point, end_point, chosenColor, thickness)

    imgStack = stackImages(scale, ([colorBox], [frame]))
    cv2.imshow("ImageStack", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
