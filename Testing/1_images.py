import cv2

img = cv2.imread('lena.jpg',-1)
cv2.imshow('siddhi',img)
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('imag_copy.png',img)