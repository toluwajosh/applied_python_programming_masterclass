# import needed libraries
import cv2 as cv  # we shorten cv2 as cv
import sys

# read the image, using cv.imread
path_to_image = "starry_night.jpg"  # path to the image
img = cv.imread(cv.samples.findFile(path_to_image))

# in case we cannot read the image
if img is None:
    sys.exit("Could not read the image.")

# if image is read successfully display the image
cv.imshow("Display window", img)

# pause the image display until the user presses a key
k = cv.waitKey(0)

# if the user presses the 's' key, save the image, using cv.imwrite
if k == ord("s"):
    image_save_path = "starry_night_saved.png"
    cv.imwrite(image_save_path, img)