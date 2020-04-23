# OCR with OpenCV

Optical Character Recognition (OCR) is th electronic or mechanical conversion of images of typed, handwritten or printed text into machine-encoded text, whether from a scanned document, a photo of a document, a scene-photo or from subtitle text superimposed on an image.

In this section, we will try to understand the problem and learn the process of solving the problem using the tools we have learnt so far. Our object is to recognize characters in a  printed document using a webcam.

To solve the OCR problem, we have to do the following

1. Capture Image, from file or camera.
2. Recognize paper corners, edge detection
3. Preprocess Image; Smoothing, Cropping, Perspective Transform.
4. Recognize Text Regions: Thresholding and Contour extraction
5. Recognize individual characters in the text regions
6. Output the recognized text in a readable order.

Due to the length of the code used for this purpose. The code will be supplied in a different file. In order to finish the OCR task, we need two special functions. These functions were developed through a method called [Deep Learning](https://en.wikipedia.org/wiki/Deep_learning), which has become very popular recently for computer vision tasks. Because of its complexity will not learn about deep learning in this class. However, it is sufficient to know how to use this class of functions in OpenCV. The two function are;

1. **[The EAST text detector](https://arxiv.org/abs/1704.03155):** This function detects regions in the image where there are texts and it outputs bounding boxes of those text regions.

## Install Tesseract
Tesseract, a highly popular OCR engine, was originally developed by Hewlett Packard in the 1980s and was then open-sourced in 2005. Think of it as a special function that allows us to do OCR, however, to use it we need to install it in a special way.


## Bibliography

1. Pyimagesearch, OCR - https://www.pyimagesearch.com/category/optical-character-recognition-ocr/