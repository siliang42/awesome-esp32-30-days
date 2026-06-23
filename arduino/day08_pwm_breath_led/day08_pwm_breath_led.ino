const int LED_PIN = 23;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  for (int duty = 0; duty <= 255; duty++) {
    analogWrite(LED_PIN, duty);
    delay(8);
  }
  for (int duty = 255; duty >= 0; duty--) {
    analogWrite(LED_PIN, duty);
    delay(8);
  }
}
