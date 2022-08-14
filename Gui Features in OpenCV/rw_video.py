import cv2 as cv

cap = cv.VideoCapture('assets/vtest.avi')
fourcc = cv.VideoWriter_fourcc(*'MJPG')
size = (576, 768)
out = cv.VideoWriter('assets/output.avi', fourcc, 24.0, size)

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = cv.flip(frame, 0)
    out.write(frame)
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()

cv.destroyAllWindows()