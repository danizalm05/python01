"""
Find Nax Contours & sort -
https://www.youtube.com/watch?v=JfaZNiEbreE&list=PLCeWwpzjQu9gc9C9-iZ9WTFNGhIq4-L1X
https://www.youtube.com/watch?v=JOxebvuRpyo
https://github.com/maksimKorzh/open-cv-tutorials/blob/main/src/contours/contours.py
https://colab.research.google.com/drive/1QeXAHV3-BNaIoidWhSK3MJyVElNv3FLN#scrollTo=qF-0ptmAzxUv

"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import getpass
from inpOpenCV import stackImages,PutTextOnImage, inpTrackbar


def empty(a):
    pass
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #




cv2.namedWindow("ImageStack")
inpWinName = "Input"
inpTrackbar(inpWinName)

mimg =   "1.jpg" #"tree.jpg" #"basketball.jpg"  "tree.jpg"#  "image.png"
path = BASE_FOLDER + mimg

################## Main ####################

original_image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
image_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY) 
#contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# Find the contours from the thresholded image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours:" + str(len(contours)))
# Get the bounding rectangle

# Retreive the biggest contour
biggest_contour = max(contours, key = cv2.contourArea)

# Sort the contours in decreasing order
sorted_contours = sorted(contours, key=cv2.contourArea, reverse= True)
image0_copy = original_image.copy()
image1_copy = original_image.copy()

# Draw the biggest contour
cv2.drawContours(image0_copy, biggest_contour, -1, (255,255,170),8);
image0_copy = PutTextOnImage(image0_copy,'Max contour')

inpImage = np.zeros((50,200,3), np.uint8)
 
 
# Draw largest 4 contours
for i, cont in enumerate(sorted_contours[:4],1):
    #print( i ,cont[0,0,0], cont[0,0,1]-10)
    # Draw the contour
    cv2.drawContours(image1_copy, cont, -1, (0,255,255), 3)
    
    # Display the position of contour in sorted list
    cv2.putText(image1_copy, str(i), (cont[0,0,0], cont[0,0,1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 0),4)
    PutTextOnImage(image1_copy, "largest contours")
image3_copy = original_image.copy()


 

 
# Draw the rectangle around the object.
#cv2.rectangle(image3_copy,(x, y), (x+w, y+h), (0, 255, 0), 3)    
    
scale = 0.2
#####   Loop
while True:
   T_lower = cv2.getTrackbarPos("T_lower",inpWinName)
   T_upper = cv2.getTrackbarPos("T_upper",inpWinName)
   scale = cv2.getTrackbarPos("scale",inpWinName)/10
   switch = '0 : OFF \n1 : ON'
   on = cv2.getTrackbarPos(switch,inpWinName)

   ContourID = cv2.getTrackbarPos("Contour ID",inpWinName)
   blurred_image = cv2.GaussianBlur(original_image.copy(),(5,5),0)
   edges = cv2.Canny(blurred_image,  T_lower, T_upper)
   # cv2.RETR_EXTERNAL: Retrive only external countours
   # cv2.RETR_LIST:retrieves all  contours  without  hierarchical
   # cv2.RETR_TREE:retrieves all contours and constructs a full hierarchy of nested contours.
   #contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL,
   #                                             cv2.CHAIN_APPROX_SIMPLE)

   cntr = original_image.copy()
   cv2.drawContours(cntr, contours, -1, (0, 255, 0), 2)


   #print("Number of Contours Returned: {}".format(len(contours)),"ContourID =", ContourID)

   if(ContourID < (len(contours) )):
       contour_selected = contours[ContourID]
       cv2.drawContours(cntr, contour_selected, -1, (0, 0, 255), 5)
       
      
       x, y, w, h = cv2.boundingRect(contours[ContourID])
       #print(x, y, w, h) 
       image10_copy = original_image.copy()
       cv2.rectangle(image10_copy,(x,y),(x+w,y+h),(255,0,0),3)
       
       rect = cv2.minAreaRect(contours[ContourID])
        # convert the rect object to box points
       box =  cv2.boxPoints(rect).astype('int')
       
       # Draw a rectangle around the object
       image11_copy = original_image.copy()
       cv2.drawContours(image11_copy,[box],0,(0,255,0),3)
       
       

   imgStack = stackImages( scale,
        (
           [original_image,image_gray ,image1_copy ,image0_copy  ],
           [image10_copy,image10_copy ,edges ,image11_copy  ]
        )
        )

   cv2.imshow("ImageStack",imgStack)

   cv2.imshow("Input",inpImage)



   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
cv2.destroyAllWindows()