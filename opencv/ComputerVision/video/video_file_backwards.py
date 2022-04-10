"""
Example to introduce how to read a video file backwards
"""

# Import the required packages:
import cv2
import argparse

import getpass



BASE_FOLDER = 'C:/Users/'+ getpass.getuser() +'/Videos/Captures/'
vid_name = "highway.mp4" #"w1.mp4"   #"cars.mp4" "dog.mp4"
input_file = BASE_FOLDER + vid_name
print(input_file)


capture = cv2.VideoCapture(input_file)

# Check if camera opened successfully:
if capture.isOpened()is False:
    print("Error opening video stream or file")

# We get the index of the last frame of the video file:
#  Don't start form the end  but a few frame  before
frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 106
print("starting in frame: '{}'".format(frame_index))

# Read until video is completed:
while capture.isOpened() and frame_index >= 0:

    # We set the current frame position:
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

    # Capture frame-by-frame from the video file:
    ret, frame = capture.read()
    print("Frame number : '{}'".format(frame_index))

    if ret is True:

        # Print current frame number per iteration
        # print("CAP_PROP_POS_FRAMES : '{}'".format(capture.get(cv2.CAP_PROP_POS_FRAMES)))

        # Get the timestamp of the current frame in milliseconds
        # print("CAP_PROP_POS_MSEC : '{}'".format(capture.get(cv2.CAP_PROP_POS_MSEC)))

        # Display the resulting frame:
        cv2.imshow('Original frame', frame)

        # Convert the frame to grayscale:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the grayscale frame:
        cv2.imshow('Grayscale frame', gray_frame)

        # Decrement the index to read next frame:
        frame_index = frame_index - 1
        print("next index to read: '{}'".format(frame_index))
 
        # Press q on keyboard to exit the program:
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break
 
# Release everything:
capture.release()
cv2.destroyAllWindows()
