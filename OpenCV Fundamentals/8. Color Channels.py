import  cv2 as cv
import  numpy as np

img=cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/forest.jpg')


#==========================================================================

# split the img :

'''
# Split the image into its Blue, Green, and Red channels
b, g, r = cv.split(img)

# Display the original and individual color channels
cv.imshow('original', img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

# Print the shapes of the original and split images
print(img.shape)  # (height, width, 3)
print(b.shape)    # (height, width)
print(g.shape)    # (height, width)
print(r.shape)    # (height, width)

# Merge the split channels back into a single image
merged = cv.merge([b, g, r])
cv.imshow('merged', merged)

cv.waitKey(0)
'''



#====================================================================
# spliting the img and showing actual splitting colours in blank img :

# Create a blank image with the same height and width as the original image
blank = np.zeros(img.shape[:2], dtype='uint8')

# Split the image into Blue, Green, and Red channels
b, g, r = cv.split(img)

# Merge each channel with blank images to visualize actual colors
blue = cv.merge([b, blank, blank])   # Blue channel
green = cv.merge([blank, g, blank])  # Green channel
red = cv.merge([blank, blank, r])    # Red channel

# Display the original image and the individual color channels
cv.imshow('original', img)
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

cv.waitKey(0)
