#include <Servo.h>

Servo servo;
Servo binMotor;
Servo lockMotor;
const int trigPin1 = 2; // Trigger pin for wet waste bin
const int echoPin1 = 3; // Echo pin for wet waste bin
const int trigPin2 = 4; // Trigger pin for dry waste bin
const int echoPin2 = 5; // Echo pin for dry waste bin
const int soilMoisturePin = A0; // Analog pin for soil moisture sensor
const int servoPin = 9; // Digital pin for servo motor
const int binMotorPin = 10; // Digital pin for additional motor
const int lockMotorPin = 11;
const int moistureThreshold = 600; // Threshold for soil moisture level

int angle = 90; // initial position of servo

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set trigPins as output
  pinMode(trigPin1, OUTPUT);
  pinMode(trigPin2, OUTPUT);

  // Set echoPins as input
  pinMode(echoPin1, INPUT);
  pinMode(echoPin2, INPUT);

  // Attach servo to servoPin
  servo.attach(servoPin);

  // Attach bin motor to binMotorPin
  binMotor.attach(binMotorPin);

  lockMotor.attach(lockMotorPin);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 's') {
      // Clear the trigPin for wet waste bin
      digitalWrite(trigPin1, LOW);
      delayMicroseconds(2);

      // Set the trigPin on HIGH state for 10 microseconds for wet waste bin
      digitalWrite(trigPin1, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin1, LOW);

      // Read the echoPin for wet waste bin, returns the sound wave travel time in microseconds
      long duration1 = pulseIn(echoPin1, HIGH);

      // Convert the time into distance in centimeters for wet waste bin
      int distance1 = duration1 * 0.034 / 2;

      // Clear the trigPin for dry waste bin
      digitalWrite(trigPin2, LOW);
      delayMicroseconds(2);

      // Set the trigPin on HIGH state for 10 microseconds for dry waste bin
      digitalWrite(trigPin2, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin2, LOW);

      // Read the echoPin for dry waste bin, returns the sound wave travel time in microseconds
      long duration2 = pulseIn(echoPin2, HIGH);

      // Convert the time into distance in centimeters for dry waste bin
      int distance2 = duration2 * 0.034 / 2;

      if (distance1 > 15) {
        Serial.println("Wet waste bin: empty");
        
      } else if (distance1 > 5 && distance1 < 15) {
        Serial.println("Wet waste bin: partially filled");
      } else {
        Serial.println("Wet waste bin: filled");
      }
      if (distance2 > 15) {
        Serial.println("Dry waste bin: empty");
        
      } else if (distance2 > 5 && distance2 < 15) {
        Serial.println("Dry waste bin: partially filled");
      } else {
        Serial.println("Dry waste bin: filled");
      }
    } else if (command == 'o') { // 'o' for open
      binMotor.write(1);
      delay(1000); // adjust delay as needed
    } else if (command == 'c') { // 'c' for close
      binMotor.write(180);
      delay(1000); // adjust delay as needed
    }

    else if(command =='l'){
      lockMotor.write(180);
      delay(1000);
    }

    else if(command =='u'){
      lockMotor.write(1);
      delay(1000);
    }
  }

  // Read soil moisture level
  int moistureLevel = analogRead(soilMoisturePin);

  // Check if moisture level is above threshold
  if (moistureLevel > moistureThreshold) {
    // Rotate servo motor to a certain angle
    servo.write(125); // Adjust the angle as needed
    delay(1000); // Delay to allow servo to reach the position
  } else if (moistureLevel < moistureThreshold) {
    // If moisture level is below threshold, turn off the servo motor
    servo.write(45); // Rotate servo to initial position
  } else {
    servo.write(1);
  }

  // Add a delay to prevent rapid readings
  delay(1000); // Adjust delay as needed
}
