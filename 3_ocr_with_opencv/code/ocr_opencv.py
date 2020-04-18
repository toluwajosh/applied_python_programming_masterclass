"""
ocr script
"""

import cv2
import numpy as np

input_image = cv2.imread("afam_paper.jpg")
gray_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

# detect paper edges
edge_image = cv2.Canny(gray_image, threshold1=100, threshold2=200)

# detect corners
gray_image = np.float32(gray_image)
dst = cv2.cornerHarris(gray_image, 2, 3, 0.04)

# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image.
# input_image[dst > 0.01 * dst.max()] = [0, 0, 255]


def get_paper_corners():
    corners = []

    def get_click_coord(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(corners) > 4:
                corners.pop()
            corners.append([x, y])
            print(corners)
        elif event == cv2.EVENT_MBUTTONDOWN:
            if len(corners) > 0:
                corners.pop()
                print(corners)

    # give our window a name
    cv2.namedWindow("display")
    cv2.setMouseCallback("display", get_click_coord)

    cv2.imshow("display", input_image)
    cv2.waitKey(0)

    # raise an error if the number of corners supplied is no up to 4
    assert len(corners) > 3, "Corner points are not complete. Must be 4!"
    return corners


new_corners = np.float32([[0, 0], [540, 0], [0, 720], [540, 720]])
print(input_image.shape)

# run the get paper corners function
paper_corners = np.float32(get_paper_corners())
print(paper_corners)

transform_matrix = cv2.getPerspectiveTransform(paper_corners, new_corners)
warped_image = cv2.warpPerspective(input_image, transform_matrix, (540, 720))


cv2.imshow("display", input_image)
cv2.imshow("transformed", warped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
