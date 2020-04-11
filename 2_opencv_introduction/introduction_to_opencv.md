# Introduction to OpenCV

OpenCV (Open Source Computer Vision Library) is an [open-source](https://en.wikipedia.org/wiki/Open_source) library that includes several hundreds of computer vision library. The library is provided in c++ and has [application programming interfaces (API)](https://en.wikipedia.org/wiki/Application_programming_interface) in Python and some other languages. In this class, we will focus on the Python APIs. Since OpenCV is a library for computer vision, it is necessary that we understand some computer vision concepts. We will only explain concepts that are used in this class. Please feel free to read about other concepts or theories that interest you.

> Note: If something is not clear or you need a deeper explanation of a concept. Please do not hesitate to request for the topic so that it can be added to instruction material.


## What is Computer Vision?

Computer vision is a field of science that deals with how computers can gain high-level understnading from digital images or videos. This field aims to understand and automate the tasks that the human visual system can do. Computer vision tasks includes but are not limited to the following;

1. Image processing
2. Scene reconstruction
3. Object recognition
4. Object tracking
5. 3D pose estimation
6. Learning
7. Indexing
8. Motion estimation
9. 3D scene modeling

The field of computer vision is very broad, furthermore the scope of this class is not to discuss the field but to apply the tools from the field to the specific problem. Therefore, we will not focus on understanding the theory of any methods we use but gain enough understanding to utilize the method. In case of further reading, see the Bibliography section.

### Installing OpenCV

At this stage you should have installed Python, VSCode. Use the following steps to install OpenCV.

1. Open the terminal or command line in VSCode.
   - You can use `ctrl + shift + @` for this, or click the `Terminal` menu, then 
2. Install OpenCV package
   - Type `pip install opencv-python`. This installs the package so that you can use it in your python program.

## Basic Operations in OpenCV

In this section we will introduce basic operations in OpenCV, such as reading and writing images, reading and writing videos, and image types conversion.

### Working with Images

Let us read and display an image. Explanations are included in code comments.

```python
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
```

We can save the image in [grayscale](https://whatis.techtarget.com/definition/grayscale) by adding the following line of code.

```python
if k == ord("s"):
    image_save_path = "starry_night_saved.png"
    image_gray = cv.cvt
    cv.imwrite(image_save_path, img)
```

Now if you open the saved image in your directory, it should be a grayscale image.

> Grayscale is a range of shades of gray without apparent color. The darkest possible shade is black, which is the total absence of transmitted or reflected light. The lightest possible shade is white, the total transmission or reflection of light at all visible wavelength s. Intermediate shades of gray are represented by equal brightness levels of the three primary colors (red, green and blue) for transmitted light, or equal amounts of the three primary pigments (cyan, magenta and yellow) for reflected light.



## Bibiliography

1. OpenCV Documentation - https://docs.opencv.org/4.3.0/d1/dfb/intro.html
2. [Dana H. Ballard; Christopher M. Brown (1982). Computer Vision. Prentice Hall. ISBN 978-0-13-165316-0.](https://www.e-booksdirectory.com/details.php?ebook=1124)
3. Grayscale - https://whatis.techtarget.com/definition/grayscale