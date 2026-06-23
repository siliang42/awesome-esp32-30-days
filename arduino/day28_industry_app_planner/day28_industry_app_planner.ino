const int SENSOR_PIN = 34;
const int LED_PIN = 23;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("Day 28 - Industry application probe");
  Serial.println("Scenario examples: smart home, agriculture, industrial data node, wearable.");
}

void loop() {
  int value = analogRead(SENSOR_PIN);
  bool alarm = value > 2600;
  digitalWrite(LED_PIN, alarm);
  Serial.printf("scenario=environment_monitor sensor=%d alarm=%s\n", value, alarm ? "true" : "false");
  delay(1000);
}
