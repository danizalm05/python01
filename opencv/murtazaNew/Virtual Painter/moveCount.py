'''
OpenCV: A Simple Approach to Counting Cars
https://www.learnpythonwithrune.org/opencv-counting-cars-a-simple-approach/
https://www.learnpythonwithrune.org/start-opencv-with-python/
 '''
import cv2
import numpy as np
import getpass
import imutils

#BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Pictures/Saved Pictures/'

BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Videos/Captures/'
vid_name = "cars.mp4"
path = BASE_FOLDER + vid_name
print(path)
 
class Box:
    def __init__(self, start_point, width_height):
        self.start_point = start_point
        self.end_point = (start_point[0] + width_height[0], start_point[1] + width_height[1])
        self.counter = 0
        self.frame_countdown = 0

    def overlap(self, start_point, end_point):
        if self.start_point[0] >= end_point[0] or self.end_point[0] <= start_point[0] or \
                self.start_point[1] >= end_point[1] or self.end_point[1] <= start_point[1]:
            return False
        else:
            return True




cap = cv2.VideoCapture(path)
#cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# We will keep the last frame in order to see if there has been any movement
last_frame = None

# To build a text string with counting status
text = ""

# The boxes we want to count moving objects in
boxes = []
boxes.append(Box((200, 420), (300, 120)))#Left side of road
boxes.append(Box((730, 420), (300, 120)))#right side of road

while cap.isOpened():
    ret, frame = cap.read()

    if ret==False:
        print("End of video")

        break
   # Processing of frames are done in gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # We blur it to minimize reaction to small details
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Need to check if we have a last_frame, if not get it
    if last_frame is None:
        last_frame = gray
        continue
    # Get the difference from last_frame
    delta_frame = cv2.absdiff(last_frame, gray)
    last_frame = gray
    # Have some threshold on what is enough movement
    thresh = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]
    # This dilates with two iterations
    thresh = cv2.dilate(thresh, None, iterations=2)
    # Returns a list of objects
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Converts it
    contours = imutils.grab_contours(contours)


    # Loops over all objects found
    for contour in contours:
        # Skip if contour is small (can be adjusted)
        if cv2.contourArea(contour) < 500:
            continue

        # Get's a bounding box and puts it on the frame
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # The text string we will build up
        text = "Cars:"
        # Go through all the boxes
        for box in boxes:
            box.frame_countdown -= 1
            if box.overlap((x, y), (x + w, y + h)):
                if box.frame_countdown <= 0:
                    box.counter += 1
                # The number might be adjusted, it is just set based on my settings
                box.frame_countdown = 20
            text += " (" + str(box.counter) + " ," + str(box.frame_countdown) + ")"

    # Set the text string we build up
    cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    # Let's also insert the boxes
    for box in boxes:
        cv2.rectangle(frame, box.start_point, box.end_point, (255, 255, 255), 2)

    # Let's show the frame in our window
    cv2.imshow("Car counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()