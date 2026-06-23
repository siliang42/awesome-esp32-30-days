const int POT_PIN = 34;
const int LED_PIN = 23;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int raw = analogRead(POT_PIN);
  int duty = map(raw, 0, 4095, 0, 255);
  analogWrite(LED_PIN, duty);
  Serial.printf("ADC=%d, duty=%d\n", raw, duty);
  delay(100);
}
