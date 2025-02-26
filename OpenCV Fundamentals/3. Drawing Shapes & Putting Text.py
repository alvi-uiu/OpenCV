from pickletools import uint8

import cv2 as cv
import  numpy as np

#======================================================================

# generating an img :

'''
black_img=np.zeros((500,500,3),dtype='uint8')

# generating img :
# Create a black image (default is all zeros)  
black_img = np.zeros((512, 512, 3), dtype=np.uint8)  

# Display the black image  
cv.imshow('black', black_img)  

# Change the entire image to yellow (BGR format: Blue=0, Green=255, Red=255)  
black_img[:] = 0, 255, 255  
cv.imshow('yellow', black_img)  

# Modify a portion of the image to green (BGR format: Blue=0, Green=255, Red=0)  
black_img[200:300, 300:400] = 0, 255, 0  
cv.imshow('green portion', black_img)  

# Wait indefinitely until a key is pressed  
cv.waitKey(0)  

'''



#=============================================================

# drawing a rectangle:

'''
# Create a black image of size 500x500 with 3 color channels (RGB)
black_img = np.zeros((500, 500, 3), dtype='uint8')

# Draw a blue rectangle (only border)
cv.rectangle(black_img, (0, 0), (300, 300), (255, 0, 0), thickness=3)
cv.imshow('rectangle', black_img)

# Fill the rectangle completely with blue
cv.rectangle(black_img, (0, 0), (300, 300), (255, 0, 0), thickness=-1)
cv.imshow('rectangle2', black_img)

# Draw another filled blue rectangle covering the top-left quarter of the image
cv.rectangle(black_img, (0, 0), (black_img.shape[1] // 2, black_img.shape[0] // 2), (255, 0, 0), thickness=-1)
cv.imshow('rectangle3', black_img)

# Wait indefinitely until a key is pressed
cv.waitKey(0)

'''

#======================================================================================

# drawing a circle :

'''
black=np.zeros((500,500,3),dtype='uint8')

cv.circle(black,(black.shape[1]//2,black.shape[0]//2),50,(0,255,255),thickness=3)

cv.imshow('cicile',black)

cv.waitKey(0)
'''

#===============================================================================
# drawing a line :

'''
black_img=np.zeros((500,500,3),dtype='uint8')

cv.line(black_img,(0,0),(500,500),(255,255,255),thickness=5)

cv.imshow('cicile',black_img)

cv.waitKey(0)

'''


#==============================================================================
# writing text on img :

black_img=np.zeros((500,500,3),dtype='uint8')

cv.putText(black_img,'Hola Im ALVI :)',(black_img.shape[1]//2,black_img.shape[0]//2),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),thickness=4,lineType=cv.LINE_AA)

cv.imshow('text',black_img)

cv.waitKey(0)
