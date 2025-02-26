import  cv2 as cv
import  numpy as np

img=cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/forest.jpg')
cv.imshow('forest',img)


# BGR to Gray :
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# BGR to HSV :
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR to LAB :
lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)

# BGR to RGB :
rgb=cv.cvtColor(img,cv.COLOR_BGRA2RGB)
cv.imshow('rgb',rgb)

# HSV to BGR :
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv2bgr',hsv_bgr)


cv.waitKey(0)