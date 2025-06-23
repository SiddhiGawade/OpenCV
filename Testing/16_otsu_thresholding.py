import cv2 as c

# Load the image in grayscale
img = c.imread('sudoku.jpg', 0)

# Apply Otsu's thresholding
_, otsu_thresh = c.threshold(img, 0, 255, c.THRESH_BINARY + c.THRESH_OTSU)

# Resize for display
img = c.resize(img, (600, 400))
otsu_thresh = c.resize(otsu_thresh, (600, 400))

# Show the results
c.imshow('Original Image', img)
c.imshow('Otsu Thresholding', otsu_thresh)

c.waitKey(0)
c.destroyAllWindows()
