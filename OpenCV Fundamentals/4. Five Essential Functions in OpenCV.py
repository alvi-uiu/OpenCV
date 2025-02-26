import  cv2 as cv
import  numpy as np
from numpy.ma.core import resize

img = cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/cat1Small.jpg')


#=============================================================================
# converting img into grayscale img :

'''
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('grayImg',gray_img)
cv.imshow('cat',img)
cv.waitKey(0)

'''


#=============================================================================
# making the img blur :

'''
blur_img=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)

cv.imshow('blured_img',blur_img)

cv.waitKey(0)
'''



#==============================================================================
# Detecting Edges of the img :

'''
# Apply Gaussian blur to reduce noise and smooth the image
blur_img = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)

# Detect edges using Canny edge detection on the original image
canny_img = cv.Canny(img, 125, 175)  # Extracts all edges

# Detect edges using Canny after applying Gaussian blur (reduces noise, extracts fewer edges)
canny_blur = cv.Canny(blur_img, 125, 175)

# Display the edge-detected images
cv.imshow('Canny_Edges', canny_img)
cv.imshow('Less_Canny_Edges', canny_blur)

# Wait indefinitely until a key is pressed
cv.waitKey(0)

'''

#==========================================================================
# Dialating img : increases white

'''
# Apply Canny edge detection to extract edges
canny_img = cv.Canny(img, 125, 175)

# Dilate the edges to make them thicker (expands white regions)
dilated_img = cv.dilate(canny_img, (3, 3), iterations=5)

# Display the Canny edge-detected image
cv.imshow('cannyEdge', canny_img)

# Display the dilated image
cv.imshow('dilated_img', dilated_img)

# Erode the dilated image to shrink the white regions, bringing it back closer to the original edges
eroded_img = cv.erode(dilated_img, (3, 3), iterations=5)

# Display the eroded image
cv.imshow('eroded_img', eroded_img)

# Wait indefinitely until a key is pressed
cv.waitKey(0)
'''



#=============================================================================
# resize and crop :

# Resize the image to 500x500 pixels using cv.INTER_AREA (best for downscaling)
resize_img = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)

# Display the resized image
cv.imshow('resized_img', resize_img)

# Display the original image for comparison
cv.imshow('original_img', img)

# Crop a portion of the image from y=50 to 200 and x=200 to 400
cropped_img = img[50:200, 200:400]

# Display the cropped image
cv.imshow('cropped_img', cropped_img)

# Wait indefinitely until a key is pressed
cv.waitKey(0)
