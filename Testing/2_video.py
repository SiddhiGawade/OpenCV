import cv2
import datetime

#cap = cv2.VideoCapture('sample_video.mp4')  # Open a video file or capture device   
cap = cv2.VideoCapture(0)  # Open the default camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define the codec
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Create a VideoWriter object

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Print frame dimensions

# cap.set(3,2200)
# cap.set(4,120)  # Set the frame width and height

# print(cap.get(3))
# print(cap.get(4))
    
print(cap.isOpened())

while(cap.isOpened):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally


    # datet = str(datetime.datetime.now())  # Get the current date and time

    datet = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    frame = cv2.putText(frame, datet, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)  # Add date and time to the frame
    
    cv2.imshow('video frame',frame)  # Display the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
