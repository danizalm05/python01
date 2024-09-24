"""
Display Image
https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html
https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html 
https://docs.opencv.org/4.x/db/deb/tutorial_display_image.html 
"""

import cv2 as cv
import sys
import getpass

img='1.jpg'
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
path = BASE_FOLDER+img
print("Image  = ",path) 
img = cv.imread(path)

if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
key = cv.waitKey(0)
#cv2.destroyAllWindows()
