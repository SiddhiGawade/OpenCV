import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# img = cv2.imread('cd_pic.jpg')

cap = cv2.VideoCapture(0)  # Open the default camera

# Variables for sleep detection
sleep_threshold = 0.3  # Seconds without detecting eyes to consider as sleeping (reduced from 0.5)
eye_closed_time = None  # Time when eyes were first detected as closed
sleeping = False  # Initial state

# Status indicator text
status_text = "AWAKE"
status_color = (0, 255, 0)  # Green

while cap.isOpened():
    _, img = cap.read()  # Read a frame from the camera

    img = cv2.flip(img, 1)  # Flip horizontally to correct mirror image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Status to track if any eyes are detected in this frame
    eyes_detected = False    
    
    for (x, y, w, h) in faces:        
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)  # Draw rectangle around the face
        
        roi_gray = gray[y:y + h, x:x + w]  # Region of interest for eyes in grayscale
        roi_color = img[y:y + h, x:x + w]
        
        # Focus on just the upper half of the face where eyes are located
        eye_region_height = int(h * 0.5)  # Upper 50% of face
        eye_region_y_start = y + int(h * 0.15)  # Start 15% down from top of face rectangle
        
        # Extract eye region for detection
        eye_region_gray = gray[eye_region_y_start:eye_region_y_start + eye_region_height, x:x + w]
        
        # More sensitive eye detection parameters
        eyes = eye_cascade.detectMultiScale(
            eye_region_gray,
            scaleFactor=1.1,
            minNeighbors=1,  # Very low to increase sensitivity
            minSize=(15, 15)
        )
        
        # If eyes are detected in this face, update the status
        if len(eyes) > 0:
            eyes_detected = True
            eye_closed_time = None  # Reset timer
            sleeping = False
            status_text = "AWAKE"
            status_color = (0, 255, 0)  # Green
            
            # Draw rectangles around eyes
            for (ex, ey, ew, eh) in eyes:
                # Adjust coordinates relative to the full image
                ex_abs = ex + x
                ey_abs = ey + eye_region_y_start
                cv2.rectangle(img, (ex_abs, ey_abs), (ex_abs + ew, ey_abs + eh), (0, 255, 0), 2)
                
        # If no eyes detected
        else:
            # First frame with eyes closed/covered
            if eye_closed_time is None:
                eye_closed_time = time.time()
            # Check if eyes have been closed/covered long enough
            elif time.time() - eye_closed_time >= sleep_threshold:
                sleeping = True
                status_text = "SLEEPING"
                status_color = (0, 0, 255)  # Red
                
                # Draw text near the face to indicate eyes not detected
                cv2.putText(img, "Eyes not detected", (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    # If no faces detected, reset variables
    if len(faces) == 0:
        eye_closed_time = None
        sleeping = False
        status_text = "AWAKE"
        status_color = (0, 255, 0)  # Green
    
    # Display sleep status in top-left corner
    cv2.putText(img, status_text, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                1, status_color, 2, cv2.LINE_AA)

    cv2.imshow("Sleep Detection", img)  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()
