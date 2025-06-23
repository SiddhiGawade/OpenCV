import cv2 as c

img = c.imread('sudoku.jpg',0)
_,thresh = c.threshold(img, 140, 255, c.THRESH_BINARY)

thresh2 = c.adaptiveThreshold(img, 255, c.ADAPTIVE_THRESH_MEAN_C, c.THRESH_BINARY,11,2)
thresh3 = c.adaptiveThreshold(img, 255, c.ADAPTIVE_THRESH_GAUSSIAN_C, c.THRESH_BINARY,11,2)

img = c.resize(img, (600,400))
thresh = c.resize(thresh,(600,400))
thresh2 = c.resize(thresh2,(600,400))
thresh3 = c.resize(thresh3,(600,400))

c.imshow('Original Image', img)
c.imshow('Thresholded Image', thresh)
c.imshow('Adaptive Mean Thresholded Image', thresh2)
c.imshow('Adaptive Gaussian Thresholded Image', thresh3)

c.waitKey(0)
c.destroyAllWindows()