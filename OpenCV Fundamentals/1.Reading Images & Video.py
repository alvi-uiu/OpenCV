
import  cv2 as cv
from numpy.f2py.auxfuncs import istrue

#====================================================================================
# reading images :

'''
img = cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/cat1Small.jpg')

cv.imshow('cat window',img)

cv.waitKey(0)
'''

#====================================================================================
# Reading a video using OpenCV

# Open the video file
capture = cv.VideoCapture('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/vid/vid1.mp4')

while True:
    # Read a frame from the video
    istrue, frame = capture.read()

    # If the frame is not read correctly (end of video), break the loop
    if not istrue:
        break

    # Display the frame in a window named 'video'
    cv.imshow('video', frame)

    # Exit the loop when 'x' is pressed
    if cv.waitKey(20) & 0xFF == ord('x'):
        break

# Release the video capture object
capture.release()

# Close all OpenCV windows
cv.destroyAllWindows()
