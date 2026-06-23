const int LED_PIN = 23;
const int POT_PIN = 34;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int adc = analogRead(POT_PIN);
  bool led = digitalRead(LED_PIN) == HIGH;
  unsigned long uptime = millis() / 1000;

  Serial.print("{\"device\":\"esp32-demo\",");
  Serial.print("\"uptime\":");
  Serial.print(uptime);
  Serial.print(",\"adc\":");
  Serial.print(adc);
  Serial.print(",\"led\":");
  Serial.print(led ? "true" : "false");
  Serial.println("}");

  delay(1000);
}
