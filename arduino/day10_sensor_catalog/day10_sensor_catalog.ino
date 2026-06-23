const int ANALOG_SENSOR_PIN = 34;
const int DIGITAL_SENSOR_PIN = 27;

void setup() {
  Serial.begin(115200);
  pinMode(DIGITAL_SENSOR_PIN, INPUT_PULLUP);
  Serial.println("Day 10 - Sensor catalog probe");
  Serial.println("Use GPIO34 for analog modules and GPIO27 for digital threshold modules.");
}

void loop() {
  int analogValue = analogRead(ANALOG_SENSOR_PIN);
  int digitalValue = digitalRead(DIGITAL_SENSOR_PIN);
  Serial.printf("analog=%d, digital=%s\n", analogValue, digitalValue == LOW ? "ACTIVE" : "IDLE");
  delay(500);
}
