import cv2
import numpy as np
# events = [i for i in dir(cv2) if 'EVENT' in i]

# print(events)
# print(len(events))

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left Button clicked at ({x}, {y})")
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ',' + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (0, 255, 255), 2)
        cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)  # Create a black image
img = cv2.imread('messi.jpg', 1)  # Load an image from file
cv2.imshow('image', img)  # Display the image


cv2.setMouseCallback('image', click_event)  # Set the mouse callback function
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows
# Note: The above code creates a black image and allows the user to click on it.