'''
                  contours 
 https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=6319
 https://youtu.be/eDIj5LuIL4A?list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&t=7094
 
 https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
'''
 
import cv2 as cv
import getpass
import numpy as np
from outputCV import stackImages,PutTextOnImage
from contourInp import   inpTrackbar 
  

inpWinName = "Input"
inpTrackbar(inpWinName)
img=  '1.jpg'  #'2.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
path = BASE_FOLDER+img
print("Image  = ",path) 
print("Image  shape  = ",path) 




imgs = cv.imread(path)

assert img is not None, "file could not be read, check with os.path.exists()"
img = cv.cvtColor(imgs, cv.COLOR_BGR2GRAY)

while True:

    scl = cv.getTrackbarPos("scale", inpWinName) / 10
    
    trash = cv.getTrackbarPos("trash", inpWinName)
    cnt_area =  cv.getTrackbarPos("cnt_area", inpWinName)
   
    ret, threshImg = cv.threshold(img, trash, 255, cv.THRESH_BINARY_INV)
  

    contours, hierarchy = cv.findContours(threshImg, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    print("Total Number of contours:" + str(len(contours)))
    i=0
    imgout = imgs.copy()
    imgout2 = imgs.copy()
    for cnt in contours:
        if cv.contourArea(cnt) > cnt_area:
           i += 1
           #print(i,".  " ,cv.contourArea(cnt))
           cv.drawContours( imgout, cnt, -1, (0,255,0), 3)
           x1,y1,w,h = cv.boundingRect(cnt)
           cv.rectangle(imgout2,(x1,y1),(x1+w,y1+h),(255,0,0),3)
    print("Number of contours:", i)
    imgg = img.copy()
    #PutTextOnImage(imgs,"source")
    PutTextOnImage(imgg,"gray")
    PutTextOnImage( threshImg,"thresh")
    PutTextOnImage( imgout,"imgout")
    PutTextOnImage( imgout2,"imgout2")
    
    
    imgStack = stackImages(scl,
                          ( [imgs, imgg, threshImg],
                            [ imgout, imgout2, imgg]
                          )    )
 
    cv.imshow("ImageStack", imgStack)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows() 
 
 
