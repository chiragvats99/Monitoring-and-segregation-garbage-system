import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import serial

# Function to control LED
def control_led(ser, led_status):
    if led_status:
        ser.write(b'1')  # Send '1' to turn on LED
    else:
        ser.write(b'0')  # Send '0' to turn off LED

# Try different camera indices (0, 1, 2, etc.) to access different cameras if available
video = cv2.VideoCapture(0)

# Check if the video capture object is successfully initialized
if not video.isOpened():
    print("Error: Failed to open webcam.")
    exit()

# Initialize serial connection (change port and baudrate as needed)
ser = serial.Serial('COM6', 9600)  # Change 'COM3' to your Arduino's port

while True:
    ret, frame = video.read()
    
    # Check if frame is successfully read
    if not ret:
        print("Error: Failed to read frame from webcam.")
        break

    # Bounding box.
    bbox, label, conf = cv.detect_common_objects(frame)

    # Check if "dog" is detected
    if "dog" in label:
        print("Dog found")
        control_led(ser, True)  # Turn on LED
    else:
        print("No dog detected")
        control_led(ser, False)  # Turn off LED

    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Detection", output_image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close serial connection
video.release()
cv2.destroyAllWindows()
ser.close()
