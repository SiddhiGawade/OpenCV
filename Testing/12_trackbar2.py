import cv2 as cv
import numpy as np

def nothing(x):
    print(x)  # Called when the trackbar value changes

cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 10, 400, nothing)  # Control Point trackbar
switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)  # Color switch

while True:
    img = cv.imread('lena.jpg') 
    if img is None:
        print("Error: Image not found")
        break

    pos = cv.getTrackbarPos('CP', 'image')  
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 2, (0, 255, 255), 5)  # Adjust font scale and thickness

    s = cv.getTrackbarPos(switch, 'image')  

    if s == 1:  # If switch is ON
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # For grayscale, convert to BGR to put colored text on it
        img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

    cv.imshow('image', img)  # Show updated image after putText()

    k = cv.waitKey(1) & 0xFF
    if k == 27:  # Press 'ESC' to exit
        break

cv.destroyAllWindows()