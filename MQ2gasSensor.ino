// Arduino Uno Sketch

const int gasSensorPin = A0; // Analog pin connected to the gas sensor

void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 baud
}

void loop() {
  int sensorValue = analogRead(gasSensorPin); // Read analog sensor value
  
  Serial.print("Gas Sensor Value: ");
  Serial.println(sensorValue); // Send sensor value over serial
  
  delay(1000); // Delay for stability
}
