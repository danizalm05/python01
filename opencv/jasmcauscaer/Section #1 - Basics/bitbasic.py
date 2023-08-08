'''
# Change first 100 rows to random pixels
https://www.youtube.com/watch?v=wlYPhdTbRmk&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn&index=2
https://github.com/techwithtim/OpenCV-Tutorials/blob/main/tutorial2.py
'''

import cv2
import random
import getpass

file_name = '3.jpg'
def readImagePath():
	BASE_FOLDER = 'C:/Users/' + getpass.getuser()
	BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
	path = BASE_FOLDER
	return path+file_name

file_path = readImagePath()
print(file_path)
img = cv2.imread(file_path, -1)
 
print("type = ",type(img))#<class 'numpy.ndarray'>
print("shape =", img.shape[0],img.shape[1])
for i in range(44):
	for j in range(img.shape[1]-22):
		img[i][j] = [random.randint(0, 25), random.randint(100, 255), random.randint(0, 255)]

###### Copy part of image  ############
#######################################
#tag = img[50:70, 60:90]
#img[10:30, 20:50] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()