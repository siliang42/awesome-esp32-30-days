const int SENSOR_PIN = 34;
const char* DEVICE_ID = "esp32-desk-001";

void setup() {
  Serial.begin(115200);
  Serial.println("Day 22 - Cloud payload design");
}

void loop() {
  int sensor = analogRead(SENSOR_PIN);
  unsigned long uptime = millis() / 1000;
  Serial.printf("{\"deviceId\":\"%s\",\"sensor\":%d,\"uptime\":%lu,\"unit\":\"raw\"}\n",
                DEVICE_ID, sensor, uptime);
  delay(1000);
}
