import cv2
import time


cap = cv2.VideoCapture('myVideo.mp4')

if not cap.isOpened():
    print("Error file not found or wrong codec uded!")

while cap.isOpened():
    ret, frame = cap.read()

    if ret:

        #WRITTER 20 FPS
        time.sleep(1/20)

        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

