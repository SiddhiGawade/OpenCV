import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.mp4')  # Open the default camera

ret, frame1 = cap.read()
ret, frame2 = cap.read()

cv2.namedWindow("inter", cv2.WINDOW_NORMAL)
cv2.resizeWindow("inter", 720, 540)

while cap.isOpened():
    if not ret:
        break   

    diff = cv2.absdiff(frame1, frame2)  # Calculate the absolute difference between two frames
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # Convert the difference to grayscale
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur to reduce noise
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)  # Threshold the blurred image
    dilated = cv2.dilate(thresh, None, iterations=3)  # Dilate the thresholded image to fill in holes
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Find contours in the dilated image


    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 700:  # Filter out small contours
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format("Movement"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)  # Draw contours on the first frame

    cv2.imshow("inter", frame1)  # Display the current frame
    frame1 = frame2  # Move to the next frame
    ret , frame2= cap.read()  # Read the next frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()  # Release the video capture object