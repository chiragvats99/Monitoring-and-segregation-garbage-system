// Define pins for ultrasonic sensor
const int trigPin = 2; // Trigger pin
const int echoPin = 3; // Echo pin

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set trigPin as output
  pinMode(trigPin, OUTPUT);
  // Set echoPin as input
  pinMode(echoPin, INPUT);
}

void loop() {
  // Clear the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Set the trigPin on HIGH state for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echoPin, returns the sound wave travel time in microseconds
  long duration = pulseIn(echoPin, HIGH);

  // Convert the time into distance in centimeters
  // Speed of sound is 340 m/s or 0.034 cm/microsecond
  int distance = duration * 0.034 / 2;

  if(distance > 10)
  {
    Serial.println("Dustbin is empty");
  }
  else if(distance > 5 && distance < 10)
  {
    Serial.println("Dustbin is partially filled");
  }
  else
  {
    Serial.println("Dustbin is full");
  }
  // Print the distance to Serial Monitor
  //Serial.print("Distance: ");
  //Serial.print(distance);
  //Serial.println(" cm");

  // Add a small delay before the next measurement
  delay(1000); // Adjust delay as needed
}
