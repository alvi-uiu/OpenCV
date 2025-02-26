import  cv2 as cv

# rescaling video :

'''
# Function to rescale a video frame
def rescaleFrame(frame, scale=0.20):
    # Compute new dimensions
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    # Resize the frame
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Open the video file
capture = cv.VideoCapture('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/vid/vid1.mp4')

while True:
    # Read a frame from the video
    istrue, frame = capture.read()

    # Break the loop if the frame is not read correctly (end of video)
    if not istrue:
        break

    # Resize the frame
    frame_resized = rescaleFrame(frame)

    # Display the original and resized frames
    cv.imshow('video', frame)
    cv.imshow('rescaled video', frame_resized)

    # Exit the loop when 'x' is pressed
    if cv.waitKey(20) & 0xFF == ord('x'):
        break

# Release the video capture object
capture.release()

# Close all OpenCV windows
cv.destroyAllWindows()

'''




#=========================================================================

# resizing img :

# Function to rescale an image
def rescaleFrame(frame, scale=0.20):
    # Compute new dimensions
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    # Resize the image
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Load an image
img = cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/cat1Small.jpg')

# Resize the image
resized_img = rescaleFrame(img)

# Display the original and resized images
cv.imshow('original cat', img)
cv.imshow('resized cat', resized_img)

# Wait indefinitely until a key is pressed
cv.waitKey(0)
