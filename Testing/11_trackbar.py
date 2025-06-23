import cv2 as cv
import numpy as np

def nothing(x):
    print(x) # This function is called when the trackbar value changes

#create a black image a window 
img = np.zeros((400,512,3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothing)  # Blue channel
cv.createTrackbar('G', 'image', 0, 255, nothing)  # Green channel
cv.createTrackbar('R', 'image', 0, 255, nothing)  # Red channel

switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)  # Switch to turn the color change on/off

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:  # Press 'ESC' to exit
        break 

    b=cv.getTrackbarPos('B', 'image')  # Get the current position of the Blue trackbar
    g=cv.getTrackbarPos('G', 'image')  # Get the current position of the Green trackbar
    r=cv.getTrackbarPos('R', 'image')  # Get the current position of the Red trackbar
    s=cv.getTrackbarPos(switch, 'image')  # Get the current position of the switch trackbar

    if s == 0:  # If the switch is OFF
        img[:] = 0  # Set the image to black
    else:  # If the switch is ON    
        img[:] = [b, g, r]  # Update the image with the new color values



    # img[:] = [b, g, r]  # Update the image with the new color values
cv.destroyAllWindows()