#include <Servo.h>

Servo servo; // Define servo object

int servoPin = 9; // Pin connected to servo
int state = 0; // Variable to store incoming state

void setup() {
  servo.attach(servoPin); // Attach servo to pin 9
  Serial.begin(9600); // Start serial communication
}

void loop() {
  if (Serial.available() > 0) {
    state = Serial.parseInt(); // Read incoming state
    if (state != 0) { // If state is valid
      moveServo(state); // Call function to move servo
    }
  }
}

void moveServo(int angle) {
  angle = constrain(angle, 0, 180); // Limit angle between 0 and 180
  servo.write(angle); // Move servo to specified angle
  delay(15); // Delay for servo to reach position
}
