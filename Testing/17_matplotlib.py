import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg',-1)
cv.imshow('Original Image', img)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # Convert BGR to RGB for correct color display in matplotlib

plt.imshow(img)
plt.xticks([]), plt.yticks([])  # Hide x & y ticks
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()