import cv2

img = cv2.imread('messi.jpg')

dup = img[592:667, 631:759]  # Define the ROI (Region of Interest)
img[592:667, 500:628] = dup  # target area must be same size (75x128)


cv2.imshow('image', img)  # Display the modified image

cv2.waitKey(0)  
cv2.destroyAllWindows()