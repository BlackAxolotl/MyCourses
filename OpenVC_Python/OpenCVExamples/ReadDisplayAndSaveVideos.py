import cv2

cap = cv2.VideoCapture(4)
# Parameter 4 is because my usb camera.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# FourCC is used to specify the video codec to be used.
videoOutput = cv2.VideoWriter('Videos/output_2.avi', fourcc, 3.0, (2304, 1536))
# Size argument has to match the one of the camera itself. VideoWriter is not converting the video to another size.

print(cap.isOpened())
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        videoOutput.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("My Video Frame", gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
videoOutput.release()
cv2.destroyAllWindows()