import cv2 as c
from matplotlib import pyplot as plt

img = c.imread('gradient.jpeg',1)
_, thresh = c.threshold(img, 20, 255, c.THRESH_BINARY)
_, thresh_inv = c.threshold(img, 20, 255, c.THRESH_BINARY_INV)
_, thresh_trunc = c.threshold(img, 120, 255, c.THRESH_TRUNC)
_, thresh_tozero = c.threshold(img, 120, 255, c.THRESH_TOZERO)
_, thresh_tozero_inv = c.threshold(img, 120, 255, c.THRESH_TOZERO_INV)


titles = ['Original', 'Thresholded', 'Inverse Thresholded',
          'Truncated', 'Tozero', 'Tozero Inverse']

images = [img, thresh, thresh_inv, thresh_trunc, thresh_tozero, thresh_tozero_inv]


for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  # Hide x & y ticks
plt.show()

# c.imshow('Original Image', img)   
# c.imshow('Thresholded Image', thresh)
# c.imshow('Inverse Thresholded Image', thresh_inv)
# c.imshow('Truncated Thresholded Image', thresh_trunc)
# c.imshow('Tozero Thresholded Image', thresh_tozero)
# c.imshow('Tozero Inverse Thresholded Image', thresh_tozero_inv)

# c.waitKey(0)
# c.destroyAllWindows()
