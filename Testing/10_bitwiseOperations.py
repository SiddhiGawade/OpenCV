import cv2

img1 = cv2.imread('img1.png', 1)
img2 = cv2.imread('img2.jpg', 1)

img1 = cv2.resize(img1, (460, 260))
img2 = cv2.resize(img2, (460, 260))


# bitAnd = cv2.bitwise_and(img1, img2)  # Bitwise AND operation
# bitOr = cv2.bitwise_or(img1, img2)    # Bitwise OR operation
# bitXor = cv2.bitwise_xor(img1, img2)  # Bitwise XOR operation
bitNot1 = cv2.bitwise_not(img1)  # Bitwise NOT operation on img1
bitNot2 = cv2.bitwise_not(img2)  # Bitwise NOT operation on img2
# Note: Uncomment the above lines to perform and display the other bitwise operations


cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
# cv2.imshow('Bitwise AND', bitAnd)  # Display the result of the AND operation
# cv2.imshow('Bitwise OR', bitOr)    # Display the result of the OR operation
# cv2.imshow('Bitwise XOR', bitXor)  # Display the result of the XOR operation
cv2.imshow('Bitwise NOT of Image 1', bitNot1)  # Display the result of the NOT operation
cv2.imshow('Bitwise NOT of Image 2', bitNot2)  # Display the result of the NOT operation


cv2.waitKey(0)
cv2.destroyAllWindows()