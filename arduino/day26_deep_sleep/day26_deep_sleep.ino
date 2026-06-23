#define uS_TO_S_FACTOR 1000000ULL
#define TIME_TO_SLEEP 10

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("ESP32 woke up, doing short work...");
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  Serial.println("Going to deep sleep");
  esp_deep_sleep_start();
}

void loop() {
}
