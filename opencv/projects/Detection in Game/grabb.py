"""

https://stackoverflow.com/questions/76373625/pywin32-cannot-capture-certain-windows-giving-black-screen-python-windows


"""
import cv2 as cv
import numpy as np
from ctypes import windll
import win32gui
import win32ui
import sys


#@staticmethod
def list_window_names():
     def winEnumHandler(hwnd, ctx):
         if win32gui.IsWindowVisible(hwnd):
             print(hex(hwnd), win32gui.GetWindowText(hwnd))
     win32gui.EnumWindows(winEnumHandler, None) 




def capture_win_alt(window_name: str,hwd):
    # Adapted from https://stackoverflow.com/questions/19695214/screenshot-of-inactive-window-printwindow-win32gui

    windll.user32.SetProcessDPIAware()
    if hwd == 0 :
         hwd  = win32gui.FindWindow(None, window_name)
    #print(hwd,hex(hwd ) )  
   
    #sys.exit()
    left, top, right, bottom = win32gui.GetClientRect(hwd)
    w = right - left
    h = bottom - top

    hwnd_dc = win32gui.GetWindowDC(hwd)
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    save_dc = mfc_dc.CreateCompatibleDC()
    bitmap = win32ui.CreateBitmap()
    bitmap.CreateCompatibleBitmap(mfc_dc, w, h)
    save_dc.SelectObject(bitmap)

    # If Special K is running, this number is 3. If not, 1
    result = windll.user32.PrintWindow(hwd, save_dc.GetSafeHdc(), 3)

    bmpinfo = bitmap.GetInfo()
    bmpstr = bitmap.GetBitmapBits(True)

    img = np.frombuffer(bmpstr, dtype=np.uint8).reshape((bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4))
    img = np.ascontiguousarray(img)[..., :-1]  # make image C_CONTIGUOUS and drop alpha channel

    if not result:  # result should be 1
        win32gui.DeleteObject(bitmap.GetHandle())
        save_dc.DeleteDC()
        mfc_dc.DeleteDC()
        win32gui.ReleaseDC(hwd, hwnd_dc)
        raise RuntimeError(f"Unable to acquire screenshot! Result: {result}")

    return img


def main():
    list_window_names()
    WINDOW_NAME ='Fast Window Capture - OpenCV Object Detection in Games #4 - YouTube — Mozilla Firefox'

    hwnd = 0
    #'Program Manager'
    while(True):
        screenshot = capture_win_alt(WINDOW_NAME,hwnd)
        image_gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        cv.imshow('grabbbb', image_gray)
        if cv.waitKey(1) == ord('q'):
             cv.destroyAllWindows()
             break
   
        


if __name__ == '__main__':
    main()