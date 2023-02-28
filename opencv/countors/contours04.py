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

def empty(a):
    pass
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #
mimg ="1.jpg"#"basketball.jpg"  "tree.jpg"#
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
       color = (255, 226, 25),
       thickness = 2)
   return im


original_image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

cv2.namedWindow("ImageStack")
cv2.namedWindow("Input")


# Display the result
cv2.createTrackbar("T_lower", "Input", 3, 255, empty)#100
cv2.createTrackbar("T_upper", "Input", 150, 255, empty)#160
cv2.createTrackbar("scale", "Input", 5,9, empty)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'

cv2.createTrackbar(switch, 'Input',0,1,empty)
cv2.createTrackbar("Contour ID", "Input", 0,100, empty)


################## Main ####################
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

while True:
   T_lower = cv2.getTrackbarPos("T_lower","Input")
   T_upper = cv2.getTrackbarPos("T_upper","Input")
   scale = cv2.getTrackbarPos("scale","Input")/10
   on = cv2.getTrackbarPos(switch,"Input")

   ContourID = cv2.getTrackbarPos("Contour ID","Input")
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
       
       
       # Drawing Convex Hull
       # Get the required hull
       hull_img = original_image.copy()
       cv = contours[ContourID]
       
       hull = cv2.convexHull(cv)
       # draw the hull
       cv2.drawContours(hull_img, [hull], 0 , (0,0,220), 3) 
       hull_img = PutTextOnImage(hull_img,'hull_img')
   imgStack = stackImages( scale,
        (  
           [original_image,cntr ,image1_copy ,image0_copy  ], 
           [image10_copy,image10_copy ,hull_img ,image0_copy  ]
        ) 
        )

   cv2.imshow("ImageStack",imgStack)

   cv2.imshow("Input",inpImage)



   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
cv2.destroyAllWindows()