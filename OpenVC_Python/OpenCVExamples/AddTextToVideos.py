import cv2
import datetime

cap = cv2.VideoCapture(4)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Changing the resolution of the camera to a small one.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        font = cv2.QT_FONT_BLACK
        text = 'Width: ' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + \
               ' Height: ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        dateTime = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (30, 30), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
        frame = cv2.putText(frame, dateTime, (30, 60), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('Video Image', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.read()
cv2.destroyAllWindows()
