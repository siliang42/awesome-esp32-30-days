const int LEDS[] = {18, 19, 23};
const int LED_COUNT = 3;

void setup() {
  for (int i = 0; i < LED_COUNT; i++) {
    pinMode(LEDS[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < LED_COUNT; i++) {
    digitalWrite(LEDS[i], HIGH);
    delay(180);
    digitalWrite(LEDS[i], LOW);
  }
}
