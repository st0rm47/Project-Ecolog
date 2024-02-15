import cv2
import numpy as np

# Open the camera
opencam = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not opencam.isOpened():
    print("Error opening the camera")
    exit()

# Capture a frame from the camera
ret, image = opencam.read()

# Resize the raw image into (500-height,500-width) pixels
image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)

# Make the image a numpy array and reshape it to the model's input shape.
image = np.asarray(image, dtype=np.float32).reshape(1, 500, 500, 3)

# Normalize the image array
image = (image / 127.5) - 1
save_image = ((image[0] + 1) * 127.5).astype(np.uint8)

# Save the image in the current working directory
save_path = "captured_frame.jpg"
cv2.imwrite(save_path, save_image)

# Check if the frame is captured successfully
if not ret:
    print("Error capturing the frame")
    exit()

# Display the captured frame
cv2.imshow("Camera", save_image)

# Wait for a key press to close the window
cv2.waitKey(0)

# Release the camera and close the window
opencam.release()
cv2.destroyAllWindows()
