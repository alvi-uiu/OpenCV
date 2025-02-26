import cv2 as cv
import  numpy as np

img = cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/Trump.jpg')

#==================================================================
# Contours :

'''
# Convert the image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray_img)

# Detect edges using the Canny edge detector
canny = cv.Canny(img, 125, 175)
cv.imshow('canny_edges', canny)

# Find contours from the edges detected by Canny
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# Print the number of contours found
print(f'{len(contours)} contours found!')

# Wait indefinitely until a key is pressed
cv.waitKey(0)

'''



#====================================================================
# reducing contours by blur :

'''
# Convert the image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray_img)

# Apply Gaussian blur to reduce noise and unwanted details
blur_img = cv.GaussianBlur(gray_img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur_img)

# Detect edges using the Canny edge detector on the blurred image
canny = cv.Canny(blur_img, 125, 175)
cv.imshow('canny_edges', canny)

# Find contours from the edges detected by Canny
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# Print the number of contours found
print(f'{len(contours)} contours found!')

# Wait indefinitely until a key is pressed
cv.waitKey(0)

'''



#===============================================================
# Thresholding img -> binarize/black and white :

'''
# Convert the image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply binary thresholding: pixels > 125 become 255 (white), others become 0 (black)
ret, thresh = cv.threshold(gray_img, 125, 255, cv.THRESH_BINARY)
cv.imshow('threshold', thresh)

# Wait indefinitely until a key is pressed
cv.waitKey(0)
'''


#===================================================================
# drawing contours in new blank img :

# Create a blank image with the same shape as the original image
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

# Detect edges using the Canny edge detector
canny = cv.Canny(img, 125, 175)
cv.imshow('canny_edges', canny)

# Find contours from the edges detected by Canny
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# Print the number of contours found
print(f'{len(contours)} contours found!')

# Draw contours on the blank image
cv.drawContours(blank, contours, -1, (0, 255, 255), thickness=1)
cv.imshow('contours_drawn', blank)

# Wait indefinitely until a key is pressed
cv.waitKey(0)


