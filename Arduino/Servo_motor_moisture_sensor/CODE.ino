#include <Servo.h>

// Define analog pin for soil moisture sensor
const int soilMoisturePin = A0;

// Define digital pin for servo motor
const int servoPin = 9;

// Define threshold for soil moisture level
const int moistureThreshold = 200; // Adjust this value based on your sensor calibration

Servo servoMotor;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Attach servo to the servo pin
  servoMotor.attach(servoPin);
}

void loop() {
  // Read soil moisture level
  int moistureLevel = analogRead(soilMoisturePin);

  // Print moisture level (for debugging)
  Serial.print("Moisture Level: ");
  Serial.println(moistureLevel);

  // Check if moisture level is above threshold
  if (moistureLevel > moistureThreshold) {
    // Rotate servo motor to a certain angle
    servoMotor.write(90); // Adjust the angle as needed
    delay(1000); // Delay to allow servo to reach the position
  } else {
    // If moisture level is below threshold, turn off the servo motor
    servoMotor.write(0); // Rotate servo to initial position
  }

  // Add a delay to prevent rapid readings
  delay(1000); // Adjust delay as needed
}
