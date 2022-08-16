import numpy as np
import cv2 as cv

### Directly drawing on image with the mouse

## Draw a circle with the left click of mouse
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img_grey, (x, y), 25, (0, 255, 0), -1)


cv.namedWindow(winname='Mouse_drawing')
cv.setMouseCallback('Mouse_drawing', draw_circle)

img_grey = np.zeros((512, 512, 3), np.int8)

while True:
    cv.imshow('Mouse_drawing', img_grey)

    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()


## Draw a rectangle when left click of mouse is pressed and stop drawing when its released

# True while mouse button down, False while mouse button up
drawing = False
ix, iy = -1, -1


def draw_rectangle(event, x, y, flags, param):

    global ix, iy, drawing

    if event == cv.EVENT_RBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.rectangle(img_black, (ix, iy), (x, y), (0, 255, 0), -1)
    elif event == cv.EVENT_RBUTTONUP:
        drawing = False
        cv.rectangle(img_black, (ix, iy), (x, y), (0, 255, 0), -1)


cv.namedWindow(winname='Rect_drawing')
cv.setMouseCallback('Rect_drawing', draw_rectangle)

img_black = np.zeros((512, 512, 3))
cv.namedWindow(winname='Rect_drawing')

while True:
    cv.imshow('Rect_drawing', img_black)

    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()
