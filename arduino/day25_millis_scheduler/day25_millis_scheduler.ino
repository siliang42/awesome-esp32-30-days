const int LED_PIN = 23;
const int BUTTON_PIN = 27;
unsigned long lastLedTick = 0;
unsigned long lastLogTick = 0;
bool ledState = false;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
  unsigned long now = millis();

  if (now - lastLedTick >= 500) {
    lastLedTick = now;
    ledState = !ledState;
    digitalWrite(LED_PIN, ledState);
  }

  if (now - lastLogTick >= 1000) {
    lastLogTick = now;
    Serial.print("button=");
    Serial.println(digitalRead(BUTTON_PIN) == LOW ? "down" : "up");
  }
}
