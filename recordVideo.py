import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#WINDOWS -- *'DIVX'
# MACOS or LINUX *'XVID' to save files
writer= cv2.VideoWriter('myVideo.mp4', cv2.VideoWriter_fourcc(*"XVID"), 20, (width,height))


while True:

    ret, frame = cap.read()

    #OPERATIONS(DRAWING)
    writer.write(frame)

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()