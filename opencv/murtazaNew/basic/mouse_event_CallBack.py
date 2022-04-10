'''
https://www.youtube.com/watch?v=rrh-4NtuK-w&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=9
https://gist.github.com/pknowledge/a17bd66aa7a68ea4a74d0cbc52193c5c

https://www.youtube.com/watch?v=a7_dBO3EAng&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=10
'''

import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in  i]
print(events)

'''
['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 
'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 
'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 
'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 
 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE',
 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 
 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

'''

def click_event(event, x, y, flags, param):
    print (event)
    if event == cv2.EVENT_LBUTTONDOWN:#Mouse   click Down
        print(x,',sdfsff ' ,y)

    if event == cv2.EVENT_LBUTTONDBLCLK:#Mouse Duble click
        print(x,', ' ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0] #Get the blue color number on  index (y,x)
        green = img[y, x, 1]
        red = img[y, x, 2]

        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)

img = np.zeros((512, 512, 3), np.uint8)

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

