import cv2

img = cv2.imread('Images/lena.jpg', 1)
cv2.imshow('Lena Image', img)
pressedKey = cv2.waitKey(0) & 0xFF

if pressedKey == 27:
    cv2.destroyAllWindows()
elif pressedKey == ord('s'):
    cv2.imwrite('Images/lena_copy.png', img)
    cv2.destroyAllWindows()
