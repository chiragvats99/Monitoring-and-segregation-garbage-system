// Define pin for IR sensor
const int irSensorPin = 2; // Change the pin number as per your connection

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set IR sensor pin as input
  pinMode(irSensorPin, INPUT);
}

void loop() {
  // Read the state of the IR sensor
  int irSensorState = digitalRead(irSensorPin);

  // Check if object is detected
  if (irSensorState == LOW) {
    Serial.println("Object detected");
  } else {
    Serial.println("No object detected");
  }

  // Add a small delay before the next reading
  delay(1000); // Adjust delay as needed
}
