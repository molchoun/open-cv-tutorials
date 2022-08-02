import cv2 as cv

cap = cv.VideoCapture('vtest.avi')
fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output.avi', fourcc, 24.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = cv.flip(frame, 0)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(gray)
    cv.imshow('frame', gray)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()

cv.destroyAllWindows()