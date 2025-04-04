'''
 take overlapping results from matchTemplate() and turn
 them into single object detections.   using  groupRectangles(),
https://www.youtube.com/watch?v=KecMlLUuiE4&list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI&index=3
https://github.com/learncodebygaming/opencv_tutorials/blob/master 
https://learncodebygaming.com/blog/grouping-rectangles-into-click-points
https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html
 
'''


import cv2 as cv
import numpy as np
import os
import getpass
 

frameWidth = 640
frameHeight = 480
path = 'C:/Users/' + getpass.getuser() + '/Pictures/opencv/'



def findClickPositions(needle_img_path, haystack_img_path, threshold=0.5, debug_mode=None):
        

    needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)
    haystack_img = cv.imread(haystack_img_path, cv.IMREAD_UNCHANGED)



    # Save the dimensions of the needle image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    # There are 6 methods to choose from:
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(haystack_img, needle_img, method)

    # Get the all the positions from the match result that exceed our threshold
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    #print(locations)

    # You'll notice a lot of overlapping rectangles get 
    # drawn.  We can eliminate those redundant
    # locations by using groupRectangles().
    # First we need to create the list of [x, y, w, h] 
    # rectangles
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        # Add every box to the list twice in order to 
        # retain single (non-overlapping) boxes
        rectangles.append(rect)
        rectangles.append(rect)
    # Apply group rectangles.
    # The groupThreshold parameter should usually be 1.
    # If you put it at 0 then no grouping is done.
    #  If you put it at 2 then an object needs at least 3
    # overlapping rectangles to appear in the result.
    #   eps to 0.5 
    # "Relative difference between sides of the rectangles
    # to merge them into a group."
   
    rectangles, weights = cv.groupRectangles(
                   rectangles, groupThreshold=1, eps=0.5)
    # We will ignore the weights 
    #print(rectangles)

    points = []
    if len(rectangles):
        #print('Found needle.')

        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        # Loop over all the rectangles
        for (x, y, w, h) in rectangles:

            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append((center_x, center_y))

            if debug_mode == 'rectangles':
                # Determine the box position
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                # Draw the box
                cv.rectangle(haystack_img, top_left, bottom_right, color=line_color, 
                             lineType=line_type, thickness=2)
            elif debug_mode == 'points':
                # Draw the center point
                cv.drawMarker(haystack_img, (center_x, center_y), 
                              color=marker_color, markerType=marker_type, 
                              markerSize=40, thickness=2)

        if debug_mode:
            #cv.imshow('Matches', haystack_img)
            img = cv.resize(haystack_img, (frameWidth, frameHeight))    
            cv.imshow('Result02', img)
            cv.imshow("needle",needle_img)
            cv.waitKey(0)
            #cv.imwrite('result_click_point.jpg', haystack_img)

    return points

 # ================          Main             ======================


points = findClickPositions(path+'albion_cabbage.jpg', path+'albion_farm.jpg', debug_mode='points')
print("points 1 = ",points)
points = findClickPositions(path+'albion_turnip.jpg', path+'albion_farm.jpg', 
                            threshold=0.70, debug_mode='rectangles')
print("points 2 = ",points)
print('Done.')


cv.destroyAllWindows() 