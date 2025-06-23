import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.jpg', 0)  # Load the image in grayscale
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)  # Apply Laplacian filter
lap = np.uint8(np.absolute(lap))  # Convert to uint8
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Sobel X
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Sobel Y
sobelX = np.uint8(np.absolute(sobelX))  # Convert to uint8
sobelY = np.uint8(np.absolute(sobelY))  # Convert to uint8
sobelCombined = cv2.bitwise_or(sobelX, sobelY)  # Combine Sobel X and Y
edges = cv2.Canny(img, 100, 200)  # Apply Canny edge detection
 

titles = ['Original Image', 'Laplacian', 'Sobel X', 'Sobel Y', 'Sobel Combined', 'Canny Edges']
images = [img, lap, sobelX, sobelY, sobelCombined, edges]

for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  # Hide x & y ticks
plt.show()