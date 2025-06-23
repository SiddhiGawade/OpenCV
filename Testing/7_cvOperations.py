import cv2

img = cv2.imread('lena.jpg')

print(img.shape) # returns the tuple of no. of rows, columns and channels
print(img.size)  # returns the total number of pixels (rows * columns * channels)
print(img.dtype) # returns the data type of the image array
print(img.ndim)  # returns the number of dimensions of the image array
print(img.item(10, 10, 2))  # returns the value of the pixel at (10, 10) in the 2nd channel (BGR)
print(img[10, 10])  # returns the value of the pixel at (10, 10) in all channels (BGR)
print(img[10, 10, 2])  # returns the value of the pixel at (10, 10) in the 3rd channel (BGR)
print(img[10, 10, 0])  # returns the value of the pixel at (10, 10) in the 1st channel (BGR)
print(img[10, 10, 1])  # returns the value of the pixel at (10, 10) in the 2nd channel (BGR)
print(img[10, 10, 0:2])  # returns the values of the pixel at (10, 10) in the 1st and 2nd channels (BGR)
print(img[10, 10, :])  # returns the values of the pixel at (10, 10) in all channels (BGR)
print(img[10, 10])  # returns the value of the pixel at (10, 10) in all channels (BGR)
print(img[10, 10, 0:3])  # returns the values of the pixel at (10, 10) in the 1st, 2nd and 3rd channels (BGR)


b,g,r = cv2.split(img)  # Split the image into its B, G, R channels
img = cv2.merge((b, g, r))  # Merge the channels back into a single image

# cv2.imshow('Blue Channel', b)
# cv2.imshow('Green Channel', g)
# cv2.imshow('Red Channel', r)

cv2.imshow('image', img)  
cv2.waitKey(0) 
cv2.destroyAllWindows()  