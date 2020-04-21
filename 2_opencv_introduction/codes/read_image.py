# import needed libraries
import cv2 # import opencv
import sys
import numpy as np

# read the image, using cv2.imread
path_to_image = "starry_night.jpg"  # path to the image
img = cv2.imread(cv2.samples.findFile(path_to_image))

# in case we cannot read the image
if img is None:
    sys.exit("Could not read the image.")

# image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# image_gray = np.fliplr(image_gray)

# edges = cv2.Canny(image_gray, threshold1=100, threshold2=200)

# cropped = img[100:600, 100:600]

# image_flipped_lr = np.fliplr(img)
# image_flipped_ud = np.flipud(img)

# M = np.ones(img.shape, dtype=np.uint8) * 100

# bright_image = cv2.add(img, M)
# dark_image = cv2.subtract(img, M)

zeros_image = np.zeros_like(img)
height, width, _ = zeros_image.shape
# change 600x600 square in the middle of the zeros_image to one
zeros_image[height//2-300:height//2+300, width//2-300:width//2+300] = 1

masked_image = img * zeros_image

# if image is read successfully display the image
cv2.imshow("Display window", masked_image)

# pause the image display until the user presses a key
k = cv2.waitKey(0)

# if the user presses the 's' key, save the image, using cv2.imwrite
if k == ord("s"):
    image_save_path = "starry_night_masked.png"
    # we convert the image to another color format 
    # by using the `cv2.cvtColor` function
    # We choose the grayscale format by using the `cv2.COLOR_BGR2GRAY` object.
    
    cv2.imwrite(image_save_path, masked_image)
