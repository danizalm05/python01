'''
action  read, resize, save
https://www.youtube.com/watch?v=oXlwWbU8l2o   14:00 - 20:20

https://www.youtube.com/watch?v=qCR2Weh64h4&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn
https://github.com/techwithtim/OpenCV-Tutorials/blob/main/tutorial1.py

'''


import cv2
import getpass


# Rescale video


image_name = '1.jpg' #'a1.jpg'
video_name = 'dog.mp4'

 

def readVideoPath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Videos/Captures/'
    return BASE_FOLDER + video_name

def readImagePath():
    BASE_FOLDER = 'C:/Users/' + getpass.getuser()
    BASE_FOLDER = BASE_FOLDER + '/Pictures/Saved Pictures/'
    path = BASE_FOLDER

    return path+image_name

 
def changeRes(width,height):
    # Live video   only
    capture.set(3,width)
    capture.set(4,height)




def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)



file_path = readImagePath()

img = cv2.imread(file_path)
cv2.imshow('Original', img)
#img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
rescaleFrame(img, 0.5)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg', img)
cv2.imshow('resize Image', img)



# Reading Video  file
video_path = readVideoPath()
print(video_path)
capture = cv2.VideoCapture(video_path) 




while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)
    
    cv2.imshow('Video', frame)
    cv2.imshow('Video Resized', frame_resized)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()



cv2.destroyAllWindows()