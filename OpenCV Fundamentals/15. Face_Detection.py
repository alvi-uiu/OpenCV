import cv2 as cv
import  numpy as np

img=cv.imread('/home/alvi/PycharmProjects/pythonProject/OpenCV Fundamentals/img/people.jpg')

# Convert the input image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convert the image from BGR to grayscale for face detection

# Display the grayscale image
cv.imshow('gray', gray)  # Show the grayscale image in a window

# Load the Haar Cascade Classifier for face detection
haar_cascade = cv.CascadeClassifier('haar_face.xml')  # Load the pre-trained Haar Cascade classifier

# Detect faces in the grayscale image using the detectMultiScale function
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)  # Detect faces with specified parameters

# Print the number of faces detected
print(f'Number of Faces Detected => {len(faces_rect)}')  # Display the count of detected faces

# Loop through the detected faces and draw rectangles around them
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)  # Draw a green rectangle around each detected face

# Display the image with the detected faces
cv.imshow('Detected Faces', img)  # Show the image with rectangles around faces

cv.waitKey(0)  # Wait indefinitely until a key is pressed
