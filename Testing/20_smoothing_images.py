import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Noise_salt_and_pepper.png')  # Load the image
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # Convert BGR to RGB for correct color display in matplotlib

kernel = np.ones((5, 5), np.float32) / 25  # Create a kernel for averaging 
dst = cv.filter2D(img, -1, kernel)  # Apply filter2D for Gaussian Blur
blur = cv.blur(img, (5, 5))  # Apply Blur
gblur = cv.GaussianBlur(img, (5, 5), 0)  # Apply Gaussian Blur
median = cv.medianBlur(img, 5)  # Apply Median Blur
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)  # Apply Bilateral Filter

titles = ['Original Image', '2D Convolution', 'Blur', 'Gaussian Blur','medianBlur', 'Bilateral Filter']
images = [img, dst, blur, gblur, median, bilateralFilter]
  
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  # Hide x & y ticks
plt.show()
