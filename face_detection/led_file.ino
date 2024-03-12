// Define the pin connected to the LED
int ledPin = 13; // Change this pin according to your setup

void setup() {
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);

  // Set the LED pin as an output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Check if data is available to read from serial port
  if (Serial.available() > 0) {
    // Read the incoming byte
    char command = Serial.read();

    // If command is '1', turn on LED; if '0', turn it off
    if (command == '1') {
      digitalWrite(ledPin, HIGH);
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);
    }
  }
}
