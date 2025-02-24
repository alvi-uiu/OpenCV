import cv2
import numpy as np
from numpy.distutils.misc_util import colour_text

# Reads an image from the specified path and stores it in 'img'
img = cv2.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV/img/fruit.jpeg')


#============================================================================
# read the img and print the img :

'''
# Prints the type of 'img' (it's a NumPy array)
print(type(img))  # Output: <class 'numpy.ndarray'>

# Prints the shape of 'img' (Height, Width, Channels for an RGB image)
print(img.shape)

# Displays the image in a window named 'fruit'
cv2.imshow('fruit', img)

# Waits indefinitely for a key press before closing the window
cv2.waitKey(0)

'''





#===========================================================================
# Convert an rgb img to grayscale :

'''
# Converts the image 'img' to grayscale using OpenCV's color conversion function  
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

# Prints the shape of the grayscale image (Height, Width) since it's a single-channel image  
print(imgGray.shape)  

# Displays the grayscale image in a window named 'fruitGray'  
cv2.imshow('fruitGray', imgGray)  

# Waits indefinitely for a key press before closing the window  
cv2.waitKey(0)  


'''

#============================================================
# removing green from rgb img :

'''
# B=0, G=1, R=2 (BGR format in OpenCV)  

# Sets the green channel (channel index 1) of the image 'img' to 0, removing green from the image  
img[:, :, 1] = 0  

# Displays the modified image in a window named 'fruits'  
cv2.imshow('fruits', img)  

# Waits indefinitely for a key press before closing the window  
cv2.waitKey(0)  

'''

#====================================================================
# Removing blue, green, and red channels separately to create three new images

'''
# Copy the original image before modifying
imgBlueRemoved = img.copy()
imgGreenRemoved = img.copy()
imgRedRemoved = img.copy()

# Remove the blue channel (set blue to 0)
imgBlueRemoved[:, :, 0] = 0

# Remove the green channel (set green to 0)
imgGreenRemoved[:, :, 1] = 0

# Remove the red channel (set red to 0)
imgRedRemoved[:, :, 2] = 0

# Stack the three images horizontally
new_img = np.hstack((imgBlueRemoved, imgGreenRemoved, imgRedRemoved))

# Display the stacked images
cv2.imshow('imgWin', new_img)

# Wait indefinitely for a key press before closing the window
cv2.waitKey(0)


'''


#===================================================================

# resizing img :

'''
# Resizes the image 'img' to 256x256 pixels  
img_resize = cv2.resize(img, (256, 256))  

# Prints the shape of the resized image (Height, Width, Channels)  
print(img_resize.shape)  

# Displays the resized image in a window named 'img'  
cv2.imshow('img', img_resize)  

# Waits indefinitely for a key press before closing the window  
cv2.waitKey(0)  

'''

#=========================================================================
# Flipping the image in different directions

'''
# Flips the image vertically (along the x-axis)
img_vertical_flip = cv2.flip(img, 0)

# Flips the image horizontally (along the y-axis)
img_horizontal_flip = cv2.flip(img, 1)

# Flips the image both vertically and horizontally (along both axes)
img_horizontal_vertical_flip = cv2.flip(img, -1)

# Displays the flipped images in separate windows
cv2.imshow('window', img_vertical_flip)
cv2.imshow('window2', img_horizontal_flip)
cv2.imshow('window3', img_horizontal_vertical_flip)

# Waits indefinitely for a key press before closing the windows
cv2.waitKey(0)
'''



#=======================================================================
# Cropping a region from the image (rows 100 to 300, columns 200 to 500)

'''
cropped_img = img[100:300, 200:500]  

# Displays the cropped image in a window named 'window'  
cv2.imshow('window', cropped_img)  

# Waits indefinitely for a key press before closing the window  
cv2.waitKey(0)  

'''

#============================================================================
# saving an img :

'''
# Cropping a region from the image (rows 100 to 300, columns 200 to 500)
cropped_img = img[100:300, 200:500]

# Saves the cropped image as 'croppedImg.png'
cv2.imwrite('croppedImg.png', cropped_img)

# Displays the cropped image in a window named 'window'
cv2.imshow('window', cropped_img)

# Waits indefinitely for a key press before closing the window
cv2.waitKey(0)
'''


#=======================================================================
# Drawing shapes and texts :

'''
# Creating a blank black image of size 512x512 with 3 color channels (RGB)
new_img = np.zeros((512, 512, 3), dtype=np.uint8)

# Drawing a rectangle (blue) from point (100,100) to (300,300) with a thickness of 3
cv2.rectangle(new_img, pt1=(100, 100), pt2=(300, 300), color=(255, 0, 0), thickness=3)

# Drawing a circle (red) at center (100,400) with radius 50 and anti-aliased edges
cv2.circle(new_img, center=(100, 400), radius=50, color=(0, 0, 255), thickness=3, lineType=cv2.LINE_AA, shift=0)

# Drawing a diagonal line (green) from (0,0) to (512,512) with a thickness of 3
cv2.line(new_img, pt1=(0, 0), pt2=(512, 512), color=(0, 255, 0), thickness=3, lineType=cv2.LINE_AA, shift=0)

# Adding text 'Hello World' at position (200,200) using the SIMPLEX font, blue color, and thickness 3
cv2.putText(new_img, text='Hello World', org=(200, 200), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA)

# Displaying the image with drawn shapes and text
cv2.imshow('window', new_img)
cv2.waitKey(0)

'''

#=============================================================================================

# OpenCV Mouse Event Handling :
# draw a circle when the left mouse button is clicked :
'''
# Function to draw a circle when the left mouse button is clicked
def draw(event, x, y, flags, params):
    if event == 1:  # Left mouse button click event
        cv2.circle(black_img, center=(x, y), radius=30, color=(0, 255, 255), thickness=-1, lineType=cv2.LINE_AA, shift=0)

# Creating a named window
cv2.namedWindow(winname='window')

# Setting the mouse callback function to 'draw'
cv2.setMouseCallback('window', draw) # event listener

# Creating a black image of size 512x512
black_img = np.zeros((512, 512, 3))

# Infinite loop to keep the window open until 'x' is pressed
while True:
    cv2.imshow('window', black_img)
    if cv2.waitKey(1) & 0xFF == ord('x'):  # Press 'x' to exit
        break

# Destroys all OpenCV windows
cv2.destroyAllWindows()
'''



#=============================================================================================
# draw a rectange by dragging mouse from point A to point B :

'''
# Variables to store the initial point and flag
flag = False
ix, iy = -1, -1

# Mouse callback function
def drawing(event, x, y, flags, params):
    global flag, ix, iy, black_img

    if event == cv2.EVENT_LBUTTONDOWN:  # Mouse click
        flag = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:  # Mouse drag
        if flag:
            temp_img = black_img.copy()  # Create a copy to avoid overwriting
            cv2.rectangle(temp_img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 255), thickness=-1, lineType=cv2.LINE_AA)
            cv2.imshow('window', temp_img)  # Show updated image

    elif event == cv2.EVENT_LBUTTONUP:  # Mouse release
        flag = False
        cv2.rectangle(black_img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 255), thickness=-1, lineType=cv2.LINE_AA)
        cv2.imshow('window', black_img)  # Show final rectangle

# Create window and set mouse callback
cv2.namedWindow('window')
cv2.setMouseCallback('window', drawing)

# Create a black image
black_img = np.zeros((512, 512, 3), dtype=np.uint8)

# Infinite loop to keep window open
while True:
    cv2.imshow('window', black_img)
    if cv2.waitKey(1) & 0xFF == ord('x'):  # Press 'x' to exit
        break

cv2.destroyAllWindows()


'''

#=========================================================================
# Crop an image using mouse events

# Variables to store the initial point and flag
flag = False
ix, iy = -1, -1


# Mouse callback function
def drawing(event, x, y, flags, params):
    global flag, ix, iy, img1

    if event == cv2.EVENT_LBUTTONDOWN:  # Mouse click
        flag = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:  # Mouse release
        flag = False
        fx, fy = x, y

        # Draw a rectangle on the selected region
        cv2.rectangle(img1, pt1=(ix, iy), pt2=(fx, fy), color=(0, 0, 0), thickness=3, lineType=cv2.LINE_AA, shift=0)

        # Crop the selected region
        cropped_img = img1[iy:fy, ix:fx]  # Note: y-coordinates first, then x-coordinates

        # Display the cropped image in a new window
        cv2.imshow('new_window', cropped_img)
        cv2.waitKey(0)

    # Create a window and set the mouse callback function


cv2.namedWindow('window')
cv2.setMouseCallback('window', drawing)

# Load an image
img1 = cv2.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV/img/fruit.jpeg')

# Infinite loop to keep the window open
while True:
    cv2.imshow('window', img1)
    if cv2.waitKey(1) & 0xFF == ord('x'):  # Press 'x' to exit
        break

    # Destroy all OpenCV windows
cv2.destroyAllWindows()



