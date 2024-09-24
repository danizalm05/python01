"""
                  colorspaces
https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html
https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html 

"""

import cv2 as cv




flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( flags  )
for p in flags:
    print (p)
