"""
Use a white circle black background and apply it to the FFT magnitude to do
 a low pass filter.
https://stackoverflow.com/questions/66935821/how-to-apply-a-lpf-and-hpf-to-a-fft-fourier-transform


"""
import numpy as np
import cv2
import getpass

import sys
import os
from FFTinp import stackImages,PutTextOnImage, inpTrackbar, get_limits


image_name = 'lambo.png' #'lambo.png' 'cards.jpg'
BASE_FOLDER = 'C:/Users/'+ getpass.getuser()
BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + image_name

if not (os.path.isfile(IMAGE)):
    print("ERROR --> Missing File: " + IMAGE   )
    sys.exit(1)


CameraID = 0

cap = cv2.VideoCapture(CameraID)

inpWin = "TrackBars"
scale = 0.2


inpTrackbar(inpWin)
vid_on = cv2.getTrackbarPos("switch", inpWin)
if (vid_on):
    ret, img = cap.read()
else:
    img = cv2.imread(IMAGE)

# do dft saving as complex output
dft = np.fft.fft2(img, axes=(0,1))
# apply shift of origin to center of image
dft_shift = np.fft.fftshift(dft)

# generate spectrum from magnitude image (for viewing only)
mag = np.abs(dft_shift)
spec = np.log(mag) / 20



imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
rect =  np.ones((312, 312, 3), np.uint8)
colRectLow =  cv2.cvtColor(rect,cv2.COLOR_BGR2HSV)
colRectHigh =  cv2.cvtColor(rect,cv2.COLOR_BGR2HSV)
#colRect_copy = colRect.copy()

##############################################################

while True:
    #        hue
    h_min = cv2.getTrackbarPos("Hue Min",inpWin)
    h_max = cv2.getTrackbarPos("Hue Max", inpWin)
    #        saturation
    s_min = cv2.getTrackbarPos("Sat Min", inpWin)
    s_max = cv2.getTrackbarPos("Sat Max", inpWin)
    #        value
    v_min = cv2.getTrackbarPos("Val Min", inpWin)
    v_max = cv2.getTrackbarPos("Val Max", inpWin)


    scale = cv2.getTrackbarPos("Scale", inpWin)/10
    vid_on = cv2.getTrackbarPos("switch", inpWin)


    #print(h_min,h_max,s_min,s_max,v_min, v_max)
    #For HSV, hue range is [0,179], saturation range is [0,255],
    # and value range is [0,255
    lower = np.array([h_min,s_min,v_min])#array of 3 min values
    upper = np.array([h_max,s_max,v_max])

    # Threshold the HSV image to get only the target colors
    if (vid_on):
        _ , img = cap.read()
        imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)



    cv2.rectangle(colRectLow, (1,1), (312, 312),(h_min,s_min,v_min), -1)
    cv2.rectangle(colRectHigh, (1,1), (312, 312),(h_max,s_max,v_max), -1)

    stext = str(h_min) + " " +str(s_min) +" " + str(v_min)
    colRectLow =PutTextOnImage(colRectLow ,"Low Color")
    stext = str(h_max) + " " +str(s_max) +" " + str(v_max)
    colRectHigh =PutTextOnImage(colRectHigh ,"High Color")


    # create circle mask
    radius = 32
    mask = np.zeros_like(img)
    cy = mask.shape[0] // 2
    cx = mask.shape[1] // 2
    cv2.circle(mask, (cx,cy), radius, (255,255,255), -1)[0]

    # blur the mask
    mask2 = cv2.GaussianBlur(mask, (19,19), 0)

    # apply mask to dft_shift
    dft_shift_masked = np.multiply(dft_shift,mask) / 255
    dft_shift_masked2 = np.multiply(dft_shift,mask2) / 255


    # shift origin from center to upper left corner
    back_ishift = np.fft.ifftshift(dft_shift)
    back_ishift_masked = np.fft.ifftshift(dft_shift_masked)
    back_ishift_masked2 = np.fft.ifftshift(dft_shift_masked2)


    # do idft saving as complex output
    img_back = np.fft.ifft2(back_ishift, axes=(0,1))
    img_filtered = np.fft.ifft2(back_ishift_masked, axes=(0,1))
    img_filtered2 = np.fft.ifft2(back_ishift_masked2, axes=(0,1))

    # combine complex real and imaginary components to form (the magnitude for) the original image again
    img_back = np.abs(img_back).clip(0,255).astype(np.uint8)
    img_filtered = np.abs(img_filtered).clip(0,255).astype(np.uint8)
    img_filtered2 = np.abs(img_filtered2).clip(0,255).astype(np.uint8)

    imgResult = PutTextOnImage(imgResult ,"Result")
    cv2.imshow("ORIGINAL", img)
    cv2.imshow("SPECTRUM", spec)
    cv2.imshow("MASK", mask)
    cv2.imshow("MASK2", mask2)
    cv2.imshow("ORIGINAL DFT/IFT ROUND TRIP", img_back)
    cv2.imshow("FILTERED DFT/IFT ROUND TRIP", img_filtered)
    cv2.imshow("FILTERED2 DFT/IFT ROUND TRIP", img_filtered2)
    imgStack = stackImages(scale,([spec,mask ,mask2, img_back],
                                  [img_filtered, mask,imgResult,colRectHigh]))
    cv2.imshow("Stacked Images", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()