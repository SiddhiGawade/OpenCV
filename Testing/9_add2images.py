import cv2

img = cv2.imread('messi.jpg')
img2 = cv2.imread('openCV_Logo.png')

# Resize img2 to match the size of img
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))


# dest = cv2.add(img, img2)   # Add the two images together
dest = cv2.addWeighted(img, 0.4, img2, 0.6, 0)  # Blend the two images

cv2.imshow("Siddhi's Window", dest)  # Display the result

cv2.waitKey(0)
cv2.destroyAllWindows()