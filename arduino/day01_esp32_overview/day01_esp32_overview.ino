const int LED_PIN = 2;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println();
  Serial.println("Day 01 - ESP32 hardware overview");
  Serial.println("Check board, USB data cable, 3.3V, GND, GPIO labels, and breadboard rails.");
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  Serial.println("ESP32 is running. If this blinks, upload and power are OK.");
  delay(500);
  digitalWrite(LED_PIN, LOW);
  delay(1500);
}
