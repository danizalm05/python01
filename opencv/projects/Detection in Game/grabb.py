"""

https://stackoverflow.com/questions/76373625/pywin32-cannot-capture-certain-windows-giving-black-screen-python-windows


"""
import cv2
import numpy as np
from ctypes import windll
import win32gui
import win32ui






def capture_win_alt(window_name: str):
    # Adapted from https://stackoverflow.com/questions/19695214/screenshot-of-inactive-window-printwindow-win32gui

    windll.user32.SetProcessDPIAware()
    hwnd = win32gui.FindWindow(None, window_name)

    left, top, right, bottom = win32gui.GetClientRect(hwnd)
    w = right - left
    h = bottom - top

    hwnd_dc = win32gui.GetWindowDC(hwnd)
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    save_dc = mfc_dc.CreateCompatibleDC()
    bitmap = win32ui.CreateBitmap()
    bitmap.CreateCompatibleBitmap(mfc_dc, w, h)
    save_dc.SelectObject(bitmap)

    # If Special K is running, this number is 3. If not, 1
    result = windll.user32.PrintWindow(hwnd, save_dc.GetSafeHdc(), 3)

    bmpinfo = bitmap.GetInfo()
    bmpstr = bitmap.GetBitmapBits(True)

    img = np.frombuffer(bmpstr, dtype=np.uint8).reshape((bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4))
    img = np.ascontiguousarray(img)[..., :-1]  # make image C_CONTIGUOUS and drop alpha channel

    if not result:  # result should be 1
        win32gui.DeleteObject(bitmap.GetHandle())
        save_dc.DeleteDC()
        mfc_dc.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwnd_dc)
        raise RuntimeError(f"Unable to acquire screenshot! Result: {result}")

    return img


def main():

    WINDOW_NAME = 'OpenCV Object Detection in Games Python Tutorial #1 - YouTube — Mozilla Firefox Private Browsing'#'Windows Media Player'#'Program Manager'
    while cv2.waitKey(1) != ord('q'):
        screenshot = capture_win_alt(WINDOW_NAME)
        cv2.imshow('grabb Computer Vision', screenshot)


if __name__ == '__main__':
    main()