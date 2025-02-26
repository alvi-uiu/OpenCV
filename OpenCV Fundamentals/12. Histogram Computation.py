import cv2 as cv
import  numpy as np
import matplotlib.pyplot as plt
img=cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/forest.jpg')


#==============================================================================
# Computing Grayscale Histogram :

'''
# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Compute the grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

# Plot the grayscale histogram
plt.figure('Grayscale Histogram')
plt.xlabel('Bins')  # X-axis: Intensity values (0-255)
plt.ylabel('Number of Pixels')  # Y-axis: Pixel count for each intensity
plt.plot(gray_hist, color='black')  # Plot the histogram with black color
plt.xlim([0, 256])  # Limit x-axis to 0-255 range
plt.show()

cv.waitKey(0)

'''


#========================================================================

# Compute grayscale to histogram of a musk :

'''
# Create a blank image with the same height and width as the original image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

# Create a circular mask at the center of the image with a radius of 100
mask = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 100, 255, thickness=-1)
cv.imshow('mask', mask)

# Apply the mask to the original image using bitwise AND operation
masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked_img', masked_img)

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Compute the grayscale histogram (using the mask to consider only the masked region)
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# Plot the grayscale histogram
plt.figure('Grayscale Histogram')
plt.xlabel('Bins')  # X-axis: Intensity values (0-255)
plt.ylabel('Number of Pixels')  # Y-axis: Pixel count for each intensity
plt.plot(gray_hist, color='black')  # Plot the histogram with black color
plt.xlim([0, 256])  # Limit x-axis to 0-255 range
plt.show()

cv.waitKey(0)

'''
#===========================================================================
# Colour histogram :

'''
# Create a figure for the color histogram plot
plt.figure('Colour Histogram')
plt.xlabel('Bins')  # X-axis: Intensity values (0-255)
plt.ylabel('Number of Pixels')  # Y-axis: Pixel count for each intensity

# Display the original image
cv.imshow('original', img)

# Define colors (blue, green, red) for the histogram plot
colours = ('b', 'g', 'r')

# Loop through the colors (Blue, Green, Red)
for i, col in enumerate(colours):
    # Calculate the histogram for each color channel (0: Blue, 1: Green, 2: Red)
    hist = cv.calcHist([img], [i], None, [256], [0, 256])

    # Plot the histogram for each color channel
    plt.plot(hist, color=col)
    plt.xlim([0, 256])  # Set the x-axis limits to the range of intensity values (0-255)

# Show the plot
plt.show()

# Wait indefinitely until a key is pressed
cv.waitKey(0)

'''


#==================================================================================

# Colour histogram on mask :

# Create a blank image with the same dimensions as the original image
blank = np.zeros(img.shape[:2], dtype='uint8')

# Draw a filled circle on the blank image to create a mask (centered in the image)
mask = cv.circle(blank.copy(), (blank.shape[1] // 2, blank.shape[0] // 2), 150, 255, thickness=-1)

# Apply the mask to the original image using bitwise AND operation
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

# Create a figure for the color histogram plot
plt.figure('Colour Histogram')
plt.xlabel('Bins')  # X-axis: Intensity values (0-255)
plt.ylabel('Number of Pixels')  # Y-axis: Pixel count for each intensity

# Display the original image
cv.imshow('original', img)

# Define colors (blue, green, red) for the histogram plot
colours = ('b', 'g', 'r')

# Loop through the colors (Blue, Green, Red)
for i, col in enumerate(colours):
    # Calculate the histogram for each color channel (0: Blue, 1: Green, 2: Red)
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])

    # Plot the histogram for each color channel
    plt.plot(hist, color=col)
    plt.xlim([0, 256])  # Set the x-axis limits to the range of intensity values (0-255)

# Show the plot
plt.show()

# Wait indefinitely until a key is pressed
cv.waitKey(0)

