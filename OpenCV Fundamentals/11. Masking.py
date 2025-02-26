import  cv2 as cv
import  numpy as np

img=cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/forest.jpg')
cv.imshow('original',img)


# Create a blank image with the same height and width as the original image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

# Create a circular mask at the center of the image
mask = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, 255, thickness=-1)
cv.imshow('mask', mask)

# Apply the mask to the original image using bitwise AND
masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked_img', masked_img)

cv.waitKey(0)
