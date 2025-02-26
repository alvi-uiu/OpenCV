import cv2 as cv
import numpy as np

img=cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/Trump.jpg')
cv.imshow('original',img)


# Apply different types of blurring techniques to the image

# Average blur (takes the average of surrounding pixels)
average = cv.blur(img, (7, 7))
cv.imshow('averageBlur', average)

# Gaussian blur (uses a weighted average, reducing noise while maintaining edges)
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('gaussianBlur', gaussian)

# Median blur (uses the median value of the surrounding pixels, good for salt-and-pepper noise)
median = cv.medianBlur(img, 7)
cv.imshow('medianBlur', median)

# Bilateral filter (preserves edges while reducing noise, best for detail retention)
bilateral = cv.bilateralFilter(img, 7, 15, 15)
cv.imshow('bilateralBlur', bilateral)

cv.waitKey(0)
