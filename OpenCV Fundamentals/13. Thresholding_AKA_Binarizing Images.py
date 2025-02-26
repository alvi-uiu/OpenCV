import cv2 as cv
import  numpy as np

img=cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/Trump.jpg')
cv.imread('original',img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Converts the image from BGR to grayscale
cv.imshow('gray', gray)

# Simple Thresholding:
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)  # Applies a binary threshold (values > 150 become 255, others become 0)
cv.imshow('Simple_Thresh', thresh)

# Inverse Thresholding:
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)  # Inverts the binary threshold (values > 150 become 0, others become 255)
cv.imshow('Simple_Thresh_inv', thresh)

# Adaptive Thresholding:
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# Applies adaptive thresholding with a block size of 11 and a constant value of 3, adjusting based on local image regions
cv.imshow('Adaptive_Thresh', adaptive_thresh)

#


cv.waitKey(0)  # Waits for any key press to close the window
