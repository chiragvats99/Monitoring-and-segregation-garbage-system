import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import serial
from time import time
from time import sleep

# Try different camera indices (0, 1, 2, etc.) to access different cameras if available
video = cv2.VideoCapture(0)

# Check if the video capture object is successfully initialized
if not video.isOpened():
    print("Error: Failed to open webcam.")
    exit()

# Initialize serial connection (change port and baudrate as needed)
ser = serial.Serial('COM10', 9600)  # Change 'COM6' to your Arduino's port

# Initialize a variable to store the time when an animal was last detected
last_detection_time = 0

while True:
    ret, frame = video.read()
    
    # Check if frame is successfully read
    if not ret:
        print("Error: Failed to read frame from webcam.")
        break

    # Bounding box.
    bbox, label, conf = cv.detect_common_objects(frame)

    # Check if any animal is detected
    if "dog" in label or "cat" in label:  # Add more animal labels if needed
        print("Animal detected")
        ser.write(b'l') 
        sleep(2) # Rotate servo motor to 180 degrees
        last_detection_time = time()  # Update the time of last detection
    else:
        print("No animal detected")
        # Check if 2 minutes have passed since the last detection
        if time() - last_detection_time > 20:
            ser.write(b'u') 
            sleep(2) # Rotate servo motor to 0 degrees

    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Detection", output_image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close serial connection
video.release()
cv2.destroyAllWindows()
ser.close()
