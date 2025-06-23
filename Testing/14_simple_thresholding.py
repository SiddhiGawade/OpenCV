import cv2 as c

img = c.imread('gradient.jpeg',1)
_, thresh = c.threshold(img, 140, 255, c.THRESH_BINARY)
_, thresh_inv = c.threshold(img, 140, 255, c.THRESH_BINARY_INV)
_, thresh_trunc = c.threshold(img, 140, 255, c.THRESH_TRUNC)
_, thresh_tozero = c.threshold(img, 140, 255, c.THRESH_TOZERO)
_, thresh_tozero_inv = c.threshold(img, 140, 255, c.THRESH_TOZERO_INV)

c.imshow('Original Image', img)
c.imshow('Thresholded Image', thresh)
c.imshow('Inverse Thresholded Image', thresh_inv)
c.imshow('Truncated Thresholded Image', thresh_trunc)
c.imshow('Tozero Thresholded Image', thresh_tozero)
c.imshow('Tozero Inverse Thresholded Image', thresh_tozero_inv)

c.waitKey(0)
c.destroyAllWindows()
