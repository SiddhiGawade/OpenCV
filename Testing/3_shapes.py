import cv2
import numpy as np

#img = cv2.imread('lena.jpg',1)
img = np.zeros((712,512,3), np.uint8)  # Create a black image
img[:] = (25, 70, 55)  # Fill the image with white color
img = cv2.line(img,(0,1),(255,255),(135,100,10), 20)  # Draw a blue line
img = cv2.arrowedLine(img,(520,0),(255,255),(0,0,255), 20)  # Draw a blue line

img = cv2.rectangle(img,(384,0),(510,120),(0,255,255), -1)  # Draw a blue rectangle
img = cv2.circle(img,(247,103), 50, (100,0,255), -1)  # Draw a pinkish circle

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV',(10,400),font,4,(255,255,255),10,cv2.LINE_AA)

cv2.imshow('siddhi', img)


cv2.waitKey(0)
cv2.destroyAllWindows()