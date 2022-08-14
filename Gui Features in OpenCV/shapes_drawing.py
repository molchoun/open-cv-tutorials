import numpy as np
import cv2 as cv

# Create a grey noisy image
img = np.random.randint(235, 245, (512, 512, 3), np.uint8)

# To draw a line, you need to pass starting and ending coordinates of line
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# To draw a rectangle, you need top-left corner and
# bottom-right corner of rectangle
cv.rectangle(img, (410, 0), (510, 100), (0, 255, 0), 3)

# To draw a circle, you need its center coordinates and radius
cv.circle(img, (460, 50), 48, (0, 0, 255), -1)

# To draw the ellipse, you need to pass center location (x,y),
# axes lengths (major axis length, minor axis length),
# angle of rotation of ellipse in anti-clockwise direction
cv.ellipse(img, (120, 300), (100, 50), 340, 20, 360, 255, -1)

# To draw a polygon, first you need coordinates of vertices.
# Make those points into an array of shape ROWSx1x2 where ROWS are number of vertices
pts = np.array([[128,20],[210,55],[240,71],[128,5]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],False,(0,255,255))

# To put texts in images, you need specify text data, position coordinates
# font type, font size, color, thickness, lineType etc.
font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img,'OpenCV',(10,475), font, 3,(0,0,0),5,cv.LINE_AA)

cv.imshow("display image", img)
k = cv.waitKey(0)
