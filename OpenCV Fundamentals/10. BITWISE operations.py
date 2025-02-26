import cv2 as cv
import  numpy as np

# Create a blank black image of size 400x400
blank = np.zeros((400, 400), dtype='uint8')

# Create a rectangle on a copy of the blank image
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

# Create a circle on another copy of the blank image
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

# Display the individual shapes
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Perform bitwise AND operation (intersection of rectangle and circle)
bitwiseAnd = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwiseAnd)

cv.waitKey(0)

