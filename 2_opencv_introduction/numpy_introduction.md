# Introduction to Numpy

Images are basically multidimensional arrays. If you check the properties of an image in your explorer, you will see something like; dimensions `800x600`, or width `800` height `600`. This means that this image has `800x600` pixels. And for a coloured image, that would be `800x600x3` because of the `3` colour channels (Red, Green, Blue). 

**Numpy** is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays. In our applications, we will usually use Numpy together with OpenCV.

## Arrays

A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. We can create arrays with Numpy as follows:

```python
import numpy as np # we shorten the name

# create a rank 1 array
# The number of dimensions is the rank of the array
a = np.array([1,2,3])

# create a rank 2 array
b = np.array([[1,2,3], [4,5,6]]) 
# note the difference from the first array

```

We can know the shape of the arrays by doing;

```python
>>> a.shape
(3,)
>>> b.shape
(2,3)
```

There are special functions to create arrays such as;

```python
# create an array of all zeros
a = np.zeors((2,2))

# create an array of all ones
b = np.ones((2,2))

# create an array of random values
c = np.random.random((2,2))
```

### Datatypes

Every numpy array is a grid of elements of the same type. Numpy provides a large set of numeric datatypes that you can use to construct arrays. Numpy tries to guess a datatype when you create an array, but functions that construct arrays usually also include an optional argument to explicitly specify the datatype. Here are examples:

```python
import numpy as np

x_int = np.array([1, 2])   # Numpy chooses an integer dataatype

x_float = np.array([1.0, 2.0])   # Numpy chooses a float datatype

# Explicitly declare a datatype: np.int64
x_int_explicit = np.array([1, 2], dtype=np.int64)
```

To check the datatype in numpy:

```python
>>> x_int.dtype
dtype('int64')
>>> x_float.dtype
dtype('float64')
>>> x_int_explicit.dtype
dtype('int64')
```

You can see [more Numpy datatypes here](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html).


### Array Math

Basic mathematical functions operate elementwise on arrays:

```python
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# sum of two arrays
print(x + y)
print(np.add)

# difference between two arrays
print(x - y)
print(np.subtract(x, y))

# product of two arrays
print(x * y)
print(np.multiply(x, y))

# division
print(x / y)
print(np.divide(x, y))

# square root
print(np.sqrt(x))
```

## Basic Image Manipulations

Now we will use our knowledge of OpenCV and Numpy libraries to perform operations such as cropping, flipping, resizing, brightening and darkening of images, and image masking. We will provide the codes to perform these operations and explanation in the code comments.

### Image Cropping

This referrers extracting a region of interest from an input image.

```python
import cv2

# read the image
image = cv2.imread("starry_night.jpg")

# obtain the shape of the image
# height, width, channels = image.shape

# we do not need channels so we can do instead
# height, width = image.shape[:2]

# to crop we specify the start and the end of the index
# in the ros and column
cropped = image[100:600, 100:600]

# Save the image. Follow this style for other code snippets in this section
cv2.imwrite("starry_night_cropped.jpg", cropped)
```

|          Original Image          |              Cropped Image               |
| :------------------------------: | :--------------------------------------: |
| ![color](codes/starry_night.jpg) | ![color](codes/starry_night_cropped.png) |


### Image flipping

This refers to flipping the array in left/right or up/down direction.

```python
import cv2
import numpy as np

# read the image
image = cv2.imread("starry_night.jpg")

# we can flip the image left/right using numpy's `fliplr`
image_flipped_lr = np.fliplr(image)

# we can flip the image up/down using numpy's `flipud`
image_flipped_ud = np.flipud(image)

```

|          Image flipped left/right           |            Image flipped up/down            |
| :-----------------------------------------: | :-----------------------------------------: |
| ![color](codes/starry_night_flipped_lr.png) | ![color](codes/starry_night_flipped_ud.png) |

## Image brightening and darkening

In OpenCV, adding or subtracting matrixes has effect on increasing or decreasing of brightness.

```python
import cv2
import numpy as np

# read the image
image = cv2.imread("starry_night.jpg")

# create a matrix of one's, then multiply it by a scaler of 100'
# np.ones gives a matrix with same dimension as of our image with all the values being 100 in this case
M = np.ones(image.shape, dtype=np.uint8) * 100
# np.unint8 is another data type in numpy. It means 8 bit unsigned integer
# the matrix M is added to our image
bright_image = cv2.add(image, M)

# subtracting the matrix creates a dark image
dark_image = cv2.subtract(image, M)
```

|              Bright Image               |              Dark Image               |
| :-------------------------------------: | :-----------------------------------: |
| ![color](codes/starry_night_bright.png) | ![color](codes/starry_night_dark.png) |

### Image masking

This refers to the process of hiding some portions of an image. This is useful in tasks such as background removal. Here we will only create a simple square masking. However, the idea is the same for other tasks.

```python
import cv2
import numpy as np

# read the image
image = cv2.imread("starry_night.jpg")

# create another array of zeros
# with the same shape as the input image
# by using np.zeros_like
zeros_image = np.zeros_like(image)
height, width, channels = zeros_image.shape

# change 600x600 square in the middle of the zeros_image to one
zeros_image[height//2-300:height//2+300, width//2-300:width//2+300] = 1

# we now mask the input image by
# multiplying the zeros_image and the input image
masked_image = image * zeros_image
```

|              Original Image               |              Masked Image               |
| :-------------------------------------: | :-----------------------------------: |
| ![color](codes/starry_night.jpg) | ![color](codes/starry_night_masked.png) |

## Bibliography

1. Numpy documentation - https://docs.scipy.org/doc/numpy/reference/index.html
2. CS231n: Convolutional Neural Networks for Visual Recognition, Python Numpy Tutorial - https://cs231n.github.io/python-numpy-tutorial/