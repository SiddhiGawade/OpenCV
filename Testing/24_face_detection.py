import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('cd_pic.jpg')

cap = cv2.VideoCapture(0)  # Open the default camera


while cap.isOpened():
    ret, img = cap.read()  # Read a frame from the camera

    img = cv2.flip(img, 1)  # Flip horizontally to correct mirror image

    if not ret:
        break  # If no frame is captured, exit the loop
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)  # Draw rectangle around the face
        cv2.putText(img, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)  # Label the face

    cv2.imshow("Original Image", img)  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()  
cap.release()  # Release the video capture object