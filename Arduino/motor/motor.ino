#include <Servo.h>

Servo servo;
int servoPin = 9;
int angle = 90; // initial position of servo

void setup() {
  servo.attach(servoPin);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'o') { // 'o' for open
      angle = 180;
    } else if (command == 'c') { // 'c' for close
      angle = 90;
    }
    servo.write(angle);
    delay(1000); // adjust delay as needed
  }
}
