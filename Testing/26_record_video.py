import cv2

# Open the default camera
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('mirrored_output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally (mirror effect)
    flipped = cv2.flip(frame, 1)

    out.write(flipped)  # Save the flipped (mirrored) frame
    cv2.imshow('Recording - Mirrored', flipped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
