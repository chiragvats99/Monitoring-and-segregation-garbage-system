import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import serial


# Function to rotate servo motor to a specified angle
def rotate_servo(ser, angle):
    ser.write(str(angle).encode())  # Send angle to Arduino

# Try different camera indices (0, 1, 2, etc.) to access different cameras if available
video = cv2.VideoCapture(0)

# Check if the video capture object is successfully initialized
if not video.isOpened():
    print("Error: Failed to open webcam.")
    exit()

# Initialize serial connection (change port and baudrate as needed)
ser = serial.Serial('COM10', 9600)  # Change 'COM6' to your Arduino's port

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
        rotate_servo(ser, 180)  # Rotate servo motor to 180 degrees
    else:
        print("No animal detected")
        rotate_servo(ser,1)

    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Detection", output_image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close serial connection
video.release()
cv2.destroyAllWindows()
ser.close()
