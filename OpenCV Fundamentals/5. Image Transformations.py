
import  cv2 as cv

import  numpy as np


img=cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/fruit.jpeg')

#=========================================================================

# Translation :

'''
# Function to translate (shift) an image by x and y pixels
def translate(img, x, y):
    # Define the translation matrix
    transMat = np.float32([[1, 0, x], [0, 1, y]])

    # Set the output image dimensions (same as input)
    dimensions = (img.shape[1], img.shape[0])

    # Apply affine transformation to shift the image
    return cv.warpAffine(img, transMat, dimensions)


# Translation directions:
# +x -> move right
# -x -> move left
# +y -> move down
# -y -> move up

# Translate the image by (150, 150) pixels
translated_img = translate(img, 150, 150)

# Display the translated image
cv.imshow('translated_img', translated_img)

# Wait indefinitely until a key is pressed
cv.waitKey(0)

'''


#====================================================================
# Rotation :

'''
# Function to rotate an image by a given angle
def rotate(img, angle, rotPoint=None):
    # Get image height and width
    (height, width) = img.shape[:2]

    # Set the rotation point to the center of the image if not provided
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    # Generate the rotation matrix
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    # Set the dimensions of the output image
    dimensions = (width, height)

    # Apply affine transformation to rotate the image
    return cv.warpAffine(img, rotMat, dimensions)

# Rotate the image by 45 degrees
rotated_img = rotate(img, 45)

# Display the rotated image
cv.imshow('rotated_img', rotated_img)


# we can also rotate a rotated img further :
rotated_rotated_img=rotate(rotated_img,45)
cv.imshow('rotated_rotated',rotated_rotated_img)

# Wait indefinitely until a key is pressed
cv.waitKey(0)

'''


#================================================================
# Resize :

'''
# Resize the image to 300x300 pixels using cv.INTER_AREA (best for downscaling)
resized_img = cv.resize(img, (300, 300), interpolation=cv.INTER_AREA)

# Display the resized image
cv.imshow('resized_img', resized_img)

# Display the original image for comparison
cv.imshow('original_img', img)

# Wait indefinitely until a key is pressed
cv.waitKey(0)
'''



#==================================================================
# Flip img :

img=cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/cat1Small.jpg')

# Flip the image vertically (along the x-axis)
vertical_flip = cv.flip(img, 0)

# Flip the image horizontally (along the y-axis)
horizontal_flip = cv.flip(img, 1)

# Flip the image both vertically and horizontally (180-degree rotation)
both_vertical_horizontal_flip = cv.flip(img, -1)

# Display the original and flipped images
cv.imshow('original', img)
cv.imshow('vertical', vertical_flip)
cv.imshow('horizontal', horizontal_flip)
cv.imshow('both', both_vertical_horizontal_flip)


#==================================================================
# crop img :

cropped_img=img[200:300,300:400]
cv.imshow('cropped',cropped_img)
cv.waitKey(0)