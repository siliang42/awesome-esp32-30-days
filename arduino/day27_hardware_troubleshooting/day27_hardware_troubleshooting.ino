const int LED_PIN = 23;
const int BUTTON_PIN = 27;
const int ADC_PIN = 34;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.println("Day 27 - Hardware troubleshooting probe");
  Serial.println("Check: power -> GND -> pin number -> minimal code -> library/network.");
}

void loop() {
  static bool led = false;
  led = !led;
  digitalWrite(LED_PIN, led);
  Serial.printf("LED=%s, button=%s, adc=%d\n",
                led ? "ON" : "OFF",
                digitalRead(BUTTON_PIN) == LOW ? "DOWN" : "UP",
                analogRead(ADC_PIN));
  delay(1000);
}
