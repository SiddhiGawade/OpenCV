import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, (255, 255, 0), -1)
        points.append((x,y))  # Store the point in the list
        if len(points) >= 2:
            cv2.line(img, points[-2], points[-1], (0, 255, 0), 2)
        cv2.imshow('image', img)


# img = cv2.imread('lena.jpg', 1)  
img = np.zeros((512, 512, 3), np.uint8)  # Create a black image
cv2.imshow('image', img)  
points =[] # Initialize an empty list to store points

cv2.setMouseCallback('image', click_event)  
cv2.waitKey(0)
cv2.destroyAllWindows()  