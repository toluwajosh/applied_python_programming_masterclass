# Passing Arguments from Terminal

An argument is a value that is passed between programs, subroutines or functions.
They are independent items, or variables, that contain data or codes. When an argument is used to customize a program for a user, it is typically called a "parameter."

So far, we have seen how to pass arguments through a function. It is also possible to pass an argument from the terminal to a python `script`.

> Sometimes, we refer to a python file as a script. A `python file` and `script` can be used interchangeably most of the time.

`argparse` is the “recommended command-line parsing module in the Python standard library.” It’s what you use to get command line arguments into your program.

We will explain this module through an example. Below, we have a script to load an image and save it in a different `colour format`. We can `hard-code` the script such that the name of the image file is fixed and if we want to apply the script on another file, we have to edit the script.

> If you do not know anything about colour formats, do not worry as we will treat this in a future section. Right now, we will focus on argparse. However, you can skip this section for now, then come back after you have learnt about OpenCV functions and colour formats.

```python
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

image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# if image is read successfully display the image
cv2.imshow("Display window", image_gray)

# pause the image display until the user presses a key
k = cv2.waitKey(0)

# if the user presses the 's' key, save the image, using cv2.imwrite
if k == ord("s"):
    image_save_path = "starry_night_gray.png"
    # we convert the image to another color format 
    # by using the `cv2.cvtColor` function
    # We choose the grayscale format by using the `cv2.COLOR_BGR2GRAY` object.
    cv2.imwrite(image_save_path, image_gray)

```

In reality, it is not desirable to edit our code every time we want to run it for a different image. This is where `argparse` comes in handy. We can use this module to pass the name of the image into the program such that we can run the program like so;

```bash
python convert_image.py starry_night.jpg
```

Here, `convert_image.py` is our python file while `starry_night.jpg` is the name of the image we want to convert. So, in case we want to run our program on a different image, we will just run;

```bash
python convert_image.py picasso.jpg
```

We can also use the argparse module to do more than just pass the name of the image into our program. We can use it for `integers`, `float` and `bool` arguments. `starry_night.jpg` above is a `string` argument. See how it is used in the following code snippet.

```python
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
```

Now to run the program we do like so;

```bash
python convert_image.py -i messi.jpg -o 1
```

If we do not supply these arguments, we get an error and the program prints a gentle help message.

```bash
usage: read_image.py [-h] -i IMAGE_PATH -o OPERATION [-s SAVE_AS]
read_image.py: error: the following arguments are required: -i/--image_path, -o/--operation
```

We could do more with this, but that is enough for now.

> If you are able to use this module very well, I want to **congratulate** you as you have learnt something the most python programmers do not do but makes running your program 10 time easier.

## Bibiography

1. Argument, PCMag - https://www.pcmag.com/encyclopedia/term/argument
2. Learn Enough Python to be Useful: argparse - https://towardsdatascience.com/learn-enough-python-to-be-useful-argparse-e482e1764e05