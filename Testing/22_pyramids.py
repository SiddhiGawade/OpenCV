import cv2

# img = cv2.imread('lena.jpg')  # Load the image in grayscale
# lr = cv2.pyrDown(img)  # Reduce the image size by half
# lr2 = cv2.pyrDown(lr) # Further reduce the size by half again
# hr2 = cv2.pyrUp(lr2) # Upscale the reduced image back to a larger size
# hr3 = cv2.pyrUp(lr)  # Upscale again to the original size

# cv2.imshow('Original Image', img)  # Display the original image
# cv2.imshow('Pyramid Down', lr)  # Display the reduced image
# cv2.imshow('Pyramid Down 2', lr2)  # Display the further reduced image
# cv2.imshow('Pyramid Up', hr2)  # Display the upscaled image
# cv2.imshow('Pyramid Up 2', hr3)  # Display the upscaled image again


# Abvove code is commented out, uncommenting it will show the pyramid operations on the image 'lena.jpg'.
# Above approach has below alternative approach using pyramid functions.


img = cv2.imread('Lena.jpg') # Loads the colorful image by default
layer = img.copy() # Create a copy of the original image
gp = [layer] # Initialize a list to store the pyramids Layer


for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)  # Append the downsampled layer to the list
    # cv2.imshow(str(i),layer)

layer = gp[5]  # Get the last or upper layer from the pyramid
cv2.imshow('Upper Layer Gaussian Pyramid', layer)  # Display the upper layer of the pyramid
lp = [layer] # Initialize a list for Laplacian Pyramid

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])  # Upscale the Gaussian layer
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)  # Calculate the Laplacian layer
    cv2.imshow(str(i), laplacian)  # Display the Laplacian layer

cv2.imshow('Original Image', img) # Display the original image

cv2.waitKey(0)
cv2.destroyAllWindows()
