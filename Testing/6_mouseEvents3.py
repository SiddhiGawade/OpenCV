import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 5, (255, 255, 0), -1)
        
        mycolorImg = np.zeros((512, 512, 3), np.uint8)
        mycolorImg[:] = [blue, green, red]
        cv2.imshow('color', mycolorImg)

img = cv2.imread('lena.jpg', 1)  
# img = np.zeros((512, 512, 3), np.uint8)  # Create a black image

cv2.imshow('image', img)  

cv2.setMouseCallback('image', click_event)  
cv2.waitKey(0)
cv2.destroyAllWindows()  