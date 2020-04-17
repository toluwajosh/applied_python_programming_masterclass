"""
ocr script
"""

import cv2
import numpy as np

input_image = cv2.imread("blank_paper.jpg")
gray_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

# detect paper edges
edge_image = cv2.Canny(gray_image, threshold1=100, threshold2=200)

# detect corners
gray_image = np.float32(gray_image)
dst = cv2.cornerHarris(gray_image, 2, 3, 0.04)

# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image.
input_image[dst > 0.01 * dst.max()] = [0, 0, 255]


# detect lines
lines = cv2.HoughLines(edge_image, 1, np.pi / 90, 100)
for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(input_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# minLineLength = 100
# maxLineGap = 100
# lines = cv2.HoughLinesP(
#     edge_image, 1, np.pi / 180, 200, minLineLength, maxLineGap
# )
# for x1, y1, x2, y2 in lines[0]:
#     cv2.line(input_image, (x1, y1), (x2, y2), (0, 255, 0), 2)


cv2.imshow("display", input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
