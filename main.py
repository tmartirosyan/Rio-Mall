import cv2
from matplotlib import pyplot as plt
import numpy as np
import RioDatas as RD
import functionality as functional


path = "1.png"#'C:\\Users\\tigran.martirosyan\\Desktop\\1.png'
img = cv2.imread(path)
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    area = img.shape[0] * img.shape[1]
    coordinates = approx.ravel()
    cooeds_area = (coordinates[0] - coordinates[-2]) * (coordinates[1] - coordinates[-1])
    if len(approx.ravel()) == 8 and cooeds_area > area - 100:  # or cooeds_area < 30:
        print(approx.ravel())
        continue
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

line_thickness = 2
for point in RD.pointRectanglesWayFirstStage:#range(len(point_rectangles_way)):
    cv2.rectangle(img, point[0], point[1], (0, 255, 0), line_thickness)

for point in RD.shopsWithCoordinates1Stage.values():#range(len(point_rectangles_way)):
    cv2.rectangle(img, point[0], point[1], (0, 0, 255), line_thickness)

cv2.imshow("path", img)
cv2.waitKey(0)
cv2.destroyAllWindows()