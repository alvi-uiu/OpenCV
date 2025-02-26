import cv2 as cv
import numpy as np

img=cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/Trump.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


# Compute the Laplacian of the image
lap = cv.Laplacian(gray, cv.CV_64F)  # Apply Laplacian operator on the grayscale image

# Convert the result to an 8-bit unsigned integer type and take the absolute value
lap = np.uint8(np.absolute(lap))  # Absolute value is taken to ensure all values are positive

# Display the Laplacian image
cv.imshow('laplacian', lap)  # Show the processed Laplacian image in a window)



# Sobel :
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Combined Sobel',combined_sobel)


# Canny :

canny=cv.Canny(gray,150,175)
cv.imshow('Canny',canny)

cv.waitKey(0)