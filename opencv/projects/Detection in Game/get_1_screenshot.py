"""
Get one sceen shot
https://www.youtube.com/watch?v=WymCpVUPWQ4&source_ve_path=Mjg2NjY
https://learncodebygaming.com/blog/fast-window-capture 
https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html
 


"""

import cv2 as cv
import numpy as np
import os
import getpass
import win32gui,  win32ui, win32con 
 

frameWidth = 640
frameHeight = 480
path = 'C:/Users/' + getpass.getuser() + '/Pictures/opencv/'

def get_screenshot():
    # define your monitor width and height
    w, h = 1920, 1080

    # for now we will set hwnd to None to capture the 
    # primary monitor
    hwnd = None
    
    # if you want a specific window use the next code:
    #     window_name = <name of a spacfic window>
    #     hwnd = win32gui.FindWindow(None, window_name)
    window_name = 'Microsoft Text Input Application' #Windows Media Player'#Program Manager'
    hwnd = win32gui.FindWindow(None, window_name)
    # get the window image data
    wDC = win32gui.GetWindowDC(hwnd)
    
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

    # convert the raw data into a format opencv can read
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    #img = np.fromstring(signedIntsArray, dtype='uint8')
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    # free resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    # drop the alpha channel to work with cv.matchTemplate()
    img = img[...,:3]

    # make image C_CONTIGUOUS to avoid errors with cv.rectangle()
    img = np.ascontiguousarray(img)
  
    return img

# =================     MAIN   ===============



while(True):
  img =  get_screenshot() 
  img = cv.resize(img, (frameWidth, frameHeight))    
  
  cv.imshow('This is primery monitor', img)  
  if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows()
    break