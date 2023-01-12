"""
Contours & Masks using Python & OpenCV -
How to separate object from image background?
https://www.youtube.com/watch?v=JOxebvuRpyo
https://github.com/maksimKorzh/open-cv-tutorials/blob/main/src/contours/contours.py


"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import getpass



def empty(a):
    pass
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #
mimg = "image.png"#"basketball.jpg"
path = BASE_FOLDER + mimg

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def PutTextOnImage(image,txt):
   im= cv2.putText (img = image,
       text = txt,
       org = (20 , 50 ),
       fontFace = cv2.FONT_HERSHEY_DUPLEX,
       fontScale = 2.0,
       color = (255, 26, 25),
       thickness = 3)
   return im


original_image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
image1_copy = original_image.copy()


plt.figure(figsize=[20,10])
# Convert to grayscale.
imageGray = cv2.cvtColor(image1_copy,cv2.COLOR_BGR2GRAY)
#cv2.imshow("ImageStack",imageGray)
# Find all contours in the image
contours, hierarchy = cv2.findContours(imageGray, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
for i,cont in enumerate(contours):

   # Draw the ith contour
   print(i )
   image1_copy = cv2.drawContours(image1_copy, cont, -1, (0,255,0), 3)

   # Add a subplot to the figure
   plt.subplot(2, 4, i+1)

   # Turn off the axis
   plt.axis("off");plt.title('contour ' +str(i))

   # Display the image in the subplot
   plt.imshow(image1_copy)


cv2.waitKey(0) & 0xFF == ord('q')

cv2.destroyAllWindows()