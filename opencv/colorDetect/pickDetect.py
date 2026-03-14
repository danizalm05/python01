'''
https://github.com/techoflassh/Color-detector-using-OpenCV
v vidoe   i image file

'''
 
import numpy as np
import cv2
import colorsys
from tkinter import filedialog as fd

Optionimage =  False
Optionvideo =  True
mouseX, mouseY = 0, 0

 
def mousePos(event, x, y, flags, param):
    # print(x, y)
    global mouseX, mouseY
    mouseX, mouseY = x, y
 
inp = cv2.VideoCapture(0)
inp.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
inp.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# bug fix
img = cv2.imread('red.jpg', 1)
cv2.imshow("IMAGE COLOR ANALYZER", img)


while True:
    if Optionimage == True:
        frame = np.copy(img)

    # elif Optionvideo == True:
    if Optionvideo == True:
        _, frame = inp.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    height, width, _ = frame.shape

    cv2.setMouseCallback("IMAGE COLOR ANALYZER", mousePos)
    x = mouseX
    y = mouseY

    try:
        pixel = rgb_frame[y, x]
    except:
        pixel = (0, 0, 0)

 
    r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
    (rn, gn, bn) = (r / 255, g / 255, b / 255)
    #convert to hsv
    (h, s, v) = colorsys.rgb_to_hsv(rn, gn, bn)
    #expand HSV range
    (h, s, v) = (int(h * 360), int(s * 100), int(v * 100))
    
    if x + 10 + 185 >= width:
        x = x - 185 - 15
    if y + 10 + 115 >= height:
        y = y - 115 - 15
    # rectangle for color
    frame = cv2.rectangle(frame, (x+15, y+5), (x+185, y+115), (99, 99, 99), -1)
    frame = cv2.rectangle(frame, (x+15, y+5), (x+185, y+115), (9, 9, 9), 1)
    frame = cv2.rectangle(frame, (x+20, y+10), (x+180, y+50), (b, g, r), -1)
    frame = cv2.rectangle(frame, (x+20, y+10), (x+180, y+50), (9, 9, 9), 1)
    # rectangle for rgb value output
    frame = cv2.rectangle(frame, (x+20, y+60), (x+180, y+82), (30, 30, 30), -1)
    frame = cv2.rectangle(frame, (x+20, y+60), (x+180, y+82), (9, 9, 9), 1)
    # rectangle for name output
    frame = cv2.rectangle(frame, (x+20, y+87), (x+180, y+110), (30, 30, 30), -1)
    frame = cv2.rectangle(frame, (x+20, y+87), (x+180, y+110), (9, 9, 9), 1)

    rbginText = (f"RGB : ({r}, {g}, {b})")
    cv2.putText(frame, rbginText, (x+21, y+76), 1, 0.8, (255, 255, 255), 1)
    #cv2.putText(frame, color, (x+15, y+103), 1, 0.8, (255, 255, 255), 1)
    hsvinText =  (f"HSV : ({h}, {s}, {v})")
    cv2.putText(frame,  hsvinText, (x+17, y+103), 1, 0.8, (255, 255, 255), 1)

    cv2.imshow("IMAGE COLOR ANALYZER", frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break  
    if key == ord('I') or key == ord('i'):
        Optionimage = True
        Optionvideo = False

        filename = fd.askopenfilename()
        img = cv2.imread(filename)

    if key == ord('V') or key == ord('v'):
        Optionimage = False
        Optionvideo = True
         
        
    if key == ord('q') or key == 27:
        break
inp.release()
cv2.destroyAllWindows()
