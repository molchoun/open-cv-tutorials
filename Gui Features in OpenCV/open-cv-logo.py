import numpy as np
import cv2 as cv


# replicating OpenCV logo with drawing functions
img = np.random.randint(254, 255, (512, 512, 3), np.uint8)

# Green circle
cv.ellipse(img, (205, 256), (50, 50), 0, 0, 300, (0, 255, 0), -1)
cv.ellipse(img, (205, 256), (25, 25), 0, 0, 360, (255, 255, 255), -1)
# Blue circle
cv.ellipse(img, (308, 256), (50, 50), 300, 0, 300, (255, 0, 0), -1)
cv.ellipse(img, (308, 256), (25, 25), 0, 0, 360, (255, 255, 255), -1)
# Red circle
cv.ellipse(img, (256, 165), (50, 50), 120, 0, 300, (0, 0, 255), -1)
cv.ellipse(img, (256, 165), (25, 25), 0, 0, 360, (255, 255, 255), -1)

cv.imshow("Display image", img)
k = cv.waitKey(0)
cv.imwrite("assets/open-cv-logo.png", img)
