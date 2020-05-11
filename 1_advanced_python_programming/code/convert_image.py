# import needed libraries
import cv2  # import opencv
import sys
import numpy as np

import argparse  # needed for passing terminal arguments


# this is argparse section. Note the syntax of the module
parser = argparse.ArgumentParser()
# pass image name
parser.add_argument(
    "-i",  # this is a short form of argument identifier
    "--image_path",  # this is the full argument identifier
    type=str,  # the data type of the argument
    required=True,  # to ensure the user provides this argument
    help="specify path to input image",  # A help message to help the user
)

# we can also specify a default using default="starry_night.jpg"
parser.add_argument(
    "-o",
    "--operation",
    type=int,
    required=True,
    help="choose an operation [1=grayscale, 2=fliplr, "  # break string
    "3=canny, 4=brighten, 5=darken]",
)

# let us add the ability to choose an output image name, with a default
# if the user does not specify a value, the default value is used.
parser.add_argument(
    "-s",
    "--save_as",
    type=str,
    help="path to save output image",
    default="output_image.jpg",
)

arguments = parser.parse_args()  # we need the line to finish passing arguments
# now we can use the arguments in out program
# note the use of `arguments.[identifier]` in the script

# read the image, using cv2.imread
path_to_image = arguments.image_path  # path to the image, from arguments
img = cv2.imread(cv2.samples.findFile(path_to_image))

# in case we cannot read the image
if img is None:
    sys.exit("Could not read the image.")


# we want to perform several operations on the image ##############
# depending on what the user chooses ##############
# for brightness and darkening
pixel_change = np.ones(img.shape, dtype=np.uint8) * 100

# multiple operations will use grayscale image, so we do it once
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Using if condition
if arguments.operation == 1:  # convert to grayscale
    converted_image = gray_image
elif arguments.operation == 2:  # flip image
    converted_image = np.fliplr(img)
elif arguments.operation == 3:  # edge detection
    converted_image = cv2.Canny(gray_image, threshold1=100, threshold2=200)
elif arguments.operation == 4:  # brighten image
    converted_image = cv2.add(img, pixel_change)
elif arguments.operation == 5:  # darken image
    dark_image = cv2.subtract(img, pixel_change)


# image_flipped_lr = np.fliplr(img)
# image_flipped_ud = np.flipud(img)
# cropped = img[100:600, 100:600]

# zeros_image = np.zeros_like(img)
# height, width, _ = zeros_image.shape
# # change 600x600 square in the middle of the zeros_image to one
# zeros_image[
#     height // 2 - 300 : height // 2 + 300, width // 2 - 300 : width // 2 + 300
# ] = 1

# masked_image = img * zeros_image

# if image is read successfully display the image
cv2.imshow("Display window", converted_image)

# pause the image display until the user presses a key
k = cv2.waitKey(0)

# if the user presses the 's' key, save the image, using cv2.imwrite
if k == ord("s"):
    image_save_path = argparse.save_as
    # we convert the image to another color format
    # by using the `cv2.cvtColor` function
    # We choose the grayscale format by using the `cv2.COLOR_BGR2GRAY` object.

    cv2.imwrite(image_save_path, converted_image)
