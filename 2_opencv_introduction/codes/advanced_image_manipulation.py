# import needed libraries
import cv2 # import opencv
import sys
import numpy as np

# read the image, using cv2.imread
path_to_image = "messi.jpg"  # path to the image
img = cv2.imread(cv2.samples.findFile(path_to_image))

# in case we cannot read the image
if img is None:
    sys.exit("Could not read the image.")

image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# image_gray = np.fliplr(image_gray)

# canny_edges = cv2.Canny(image_gray, threshold1=50, threshold2=250)

blurred_image = cv2.blur(img, (23,23))

# bilateral=cv2.bilateralFilter(image,9,75,75)



# if image is read successfully display the image
cv2.imshow("Display window", blurred_image)

# pause the image display until the user presses a key
k = cv2.waitKey(0)

# if the user presses the 's' key, save the image, using cv2.imwrite
if k == ord("s"):
    image_save_path = "messi_blurred_image.png"
    # we convert the image to another color format 
    # by using the `cv2.cvtColor` function
    # We choose the grayscale format by using the `cv2.COLOR_BGR2GRAY` object.
    
    cv2.imwrite(image_save_path, blurred_image)
