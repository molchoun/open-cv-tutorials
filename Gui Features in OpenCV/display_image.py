import sys
import cv2 as cv

img = cv.imread("./Gui Features in OpenCV/assets/starry_night.jpg")
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)

# if 's' key is pressed on keyboard save displayed image in assets directory
if k == ord("s"):
    cv.imwrite("./Gui Features in OpenCV/assets/starry_night.jpg", img)
