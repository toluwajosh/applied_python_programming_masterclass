"""
ocr script
"""

import os

import cv2
import numpy as np
import pytesseract

# user packages
from process_frame import get_paper_corners
from east_text_detector import east_detector

# The next line is needed in windows only,
# so it only runs if the system is windows
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Users\joshu\AppData\Local\Tesseract-OCR\tesseract.exe"
    )

input_image = cv2.imread("lazy_sheet.jpg")  # hard-coded image path
gray_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

# detect paper edges
edge_image = cv2.Canny(gray_image, threshold1=100, threshold2=200)

# run the get paper corners function, and convert to numpy float32 type
paper_corners = np.float32(get_paper_corners(input_image))
print("paper corners: ", paper_corners)

new_corners = np.float32([[0, 0], [540, 0], [0, 720], [540, 720]])
print(input_image.shape)

# get the transformation matrix between the points
transform_matrix = cv2.getPerspectiveTransform(paper_corners, new_corners)
warped_image = cv2.warpPerspective(input_image, transform_matrix, (540, 720))

# detect text bounding boxes
boxes, confidences = east_detector(warped_image)
(H, W) = warped_image.shape[:2]

# set the new width and height and then determine the ratio in change
# for both the width and height
(newW, newH) = (640, 640)
rW = W / float(newW)
rH = H / float(newH)

# padding for bouding boxes
padding = 0.05

results = []
# loop over the bounding boxes
for (startX, startY, endX, endY) in boxes:
    # scale the bounding box coordinates based on the respective
    # ratios
    startX = int(startX * rW)
    startY = int(startY * rH)
    endX = int(endX * rW)
    endY = int(endY * rH)

    # use pytessaract to get text
    # in order to obtain a better OCR of the text we can potentially
    # apply a bit of padding surrounding the bounding box -- here we
    # are computing the deltas in both the x and y directions
    dX = int((endX - startX) * padding)
    dY = int((endY - startY) * padding)
    # apply padding to each side of the bounding box, respectively
    startX = max(0, startX - dX)
    startY = max(0, startY - dY)
    endX = min(540, endX + (dX * 2))
    endY = min(720, endY + (dY * 2))

    # extract the actual padded ROI
    roi = warped_image[startY:endY, startX:endX]

    # in order to apply Tesseract v4 to OCR text we must supply
    # (1) a language, (2) an OEM flag of 4, indicating that the we
    # wish to use the LSTM neural net model for OCR, and finally
    # (3) an OEM value, in this case, 7 which implies that we are
    # treating the ROI as a single line of text
    config = "-l eng --oem 1 --psm 7"
    text = pytesseract.image_to_string(roi, config=config)
    # add the bounding box coordinates and OCR'd text to the list
    # of results
    results.append(((startX, startY, endX, endY), text))

    # draw the bounding box on the image
    # cv2.rectangle(warped_image, (startX, startY), (endX, endY), (0, 255, 0), 2)

# sort the results bounding box coordinates from top to bottom
line_quantize = 40
image_height = 720
results = sorted(
    results, key=lambda r: r[0][1] * image_height // line_quantize + r[0][0]
)

# loop over the results
all_text = ""
for ((startX, startY, endX, endY), text) in results:
    # display the text OCR'd by Tesseract

    # print("OCR TEXT")
    # print("========")
    # print("{}\n".format(text))

    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV, then draw the text and a bounding box surrounding
    # the text region of the input image
    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
    all_text += " " + text
    # output = warped_image.copy()
    cv2.rectangle(warped_image, (startX, startY), (endX, endY), (0, 0, 255), 2)
    cv2.putText(
        warped_image,
        text,
        (startX, startY),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 0, 0),
        1,
    )

print(all_text)

# write output to file
output_file = open("scan_text.txt", "a")
output_file.write(all_text)
output_file.close()

# show the output image
cv2.imshow("Text Detection", warped_image)
cv2.waitKey(0)

# close all windows
cv2.destroyAllWindows()
