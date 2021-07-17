"""
OpenCV Course - Full Tutorial with Python
https://www.youtube.com/watch?v=oXlwWbU8l2o
https://github.com/jasmcaus/opencv-course/tree/master/Section%20%231%20-%20Basics
12:56

 """
import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

BASE_FOLDER = 'C:/Users/rockman/Pictures/Saved Pictures/'
moon_img = "moon.JPG"
path = BASE_FOLDER +  moon_img

img = cv.imread(path)
img_resized = rescaleFrame(img,scale=.2)

window_name = 'image'
cv.imshow(window_name, img)
window_name = 'img_resized'
cv.imshow(window_name, img_resized)


# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv.waitKey(0)

# closing all open windows
cv.destroyAllWindows()

VIDEO_FOLDER ='C:/Users/rockman/Videos/Captures/'
v = "dog.mp4"
vid1 = VIDEO_FOLDER + v



vid = vid1
capture = cv.VideoCapture(vid)
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):  # if 'd'  is pressed stop  the  video
        break

capture.release()
cv.destroyAllWindows()