import numpy as np
import cv2

#img = cv2.imread("Images/lena.jpg", 1)

# Creating image using numpy
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0, 0), (255, 255), (0, 255, 0), 10)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 0, 255), 5)

# Rectangle from top left to down right
img = cv2.rectangle(img, (255, 255), (415, 415), (255, 0, 0), 4)
img = cv2.rectangle(img, (415, 415), (455, 455), (255, 0, 0), -1)

img = cv2.circle(img, (335, 335), 60, (0, 255, 0), -1)

font = cv2.QT_FONT_BLACK
img = cv2.putText(img, 'RickHunter', (283, 340), font, 0.7, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("Image with line drawn", img)

cv2.waitKey(0)
cv2.destroyAllWindows()