const int BUTTON_PIN = 27;
const int LED_PIN = 23;
bool ledOn = false;
int previous = HIGH;

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("Serial button demo started");
}

void loop() {
  int current = digitalRead(BUTTON_PIN);
  if (previous == HIGH && current == LOW) {
    ledOn = !ledOn;
    digitalWrite(LED_PIN, ledOn);
    Serial.print("LED state changed: ");
    Serial.println(ledOn ? "ON" : "OFF");
    delay(50);
  }
  previous = current;
}
