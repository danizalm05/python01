"""
https://www.youtube.com/watch?v=IBQYqwq_w14
 https://github.com/jakkcoder/object_detection_cv2/blob/master/image-enhancement.ipynb

"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import getpass

def empty(a):
    pass
BASE_FOLDER = 'C:/Users/' + getpass.getuser() + '/Pictures/Saved Pictures/'
# "modrain.jpg"#"grains.jpg" #


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

#-------------------------------


cv2.namedWindow("ImageStack")
cv2.namedWindow("Input")


# Display the result
cv2.createTrackbar("color_scale", "Input", 3, 785, empty)#100
cv2.createTrackbar("T_upper", "Input", 150, 255, empty)#160
cv2.createTrackbar("scale", "Input", 5,9, empty)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'

cv2.createTrackbar(switch, 'Input',0,1,empty)
cv2.createTrackbar("Contour ID", "Input", 0,100, empty)
inpImage = np.zeros((50,200,3), np.uint8)



mimg = "3.jpg"   #"tree.jpg" "1.jpg" "basketball.jpg"  "tree.jpg"#  "image.png"
path = BASE_FOLDER + mimg

################## Main ####################

original_image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
image_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
backup= image_gray.copy()
image0_copy = original_image.copy()
for i in range(len(original_image[:,0,0])):
    for j in range(len(original_image[0,:,0])):
        R = int(image0_copy[i, j, 0])
        G = int(image0_copy[i, j, 1])
        B = int(image0_copy[i, j, 2])
        sum_col = R + G + B
        if (sum_col > 180) & (R > 200) & (G > 200) & (B > 200):
           image0_copy[i, j, 0] = image0_copy[i - 1, j - 1, 0]
           image0_copy[i, j, 1] = image0_copy[i - 1, j - 1, 1]
           image0_copy[i, j, 2] = image0_copy[i - 1, j - 1, 2]



image= original_image.copy()

#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# red color boundaries [B, G, R]
lower = [np.mean(image[:, :, i] - np.std(image[:, :, i]) / 3) for i in range(3)]
upper = [250, 250, 250]
#lower = [65.80094910473821, 45.52074150121598, 43.65427002768734]

# create NumPy arrays from the boundaries
lower = np.array(lower, dtype="uint8")
upper = np.array(upper, dtype="uint8")

# find the colors within the specified boundaries and apply
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask=mask)

ret, thresh = cv2.threshold(mask, 40, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(contours))
if len(contours) != 0:
    # draw in blue the contours that were founded
    cv2.drawContours(output, contours, -1, 255, 3)

    # find the biggest countour (c) by the area
    c = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(c)

    # draw the biggest contour (c) in green
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 5)
scale = 0.2
#####   Loop
while True:
   color_scale = cv2.getTrackbarPos("color_scale","Input")
   T_upper = cv2.getTrackbarPos("T_upper","Input")
   scale = cv2.getTrackbarPos("scale","Input")/10
   on = cv2.getTrackbarPos(switch,"Input")
   ContourID = cv2.getTrackbarPos("Contour ID","Input")


   imgStack = stackImages( scale,
        (
           [original_image, image0_copy ,image ,output ],
           [image0_copy ,image0_copy  ,image0_copy  ,image0_copy   ]
        )
        )

   cv2.imshow("ImageStack",imgStack)

   cv2.imshow("Input",inpImage)



   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
cv2.destroyAllWindows()