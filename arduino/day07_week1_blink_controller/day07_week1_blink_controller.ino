const int BUTTON_PIN = 27;
const int LED_PIN = 23;
int mode = 0;
unsigned long lastBlink = 0;
bool ledState = false;

int intervalForMode() {
  if (mode == 0) return 1000;
  if (mode == 1) return 300;
  return 100;
}

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  static int lastButton = HIGH;
  int currentButton = digitalRead(BUTTON_PIN);
  if (lastButton == HIGH && currentButton == LOW) {
    mode = (mode + 1) % 3;
    Serial.print("Mode: ");
    Serial.println(mode);
    delay(60);
  }
  lastButton = currentButton;

  if (millis() - lastBlink >= intervalForMode()) {
    lastBlink = millis();
    ledState = !ledState;
    digitalWrite(LED_PIN, ledState);
  }
}
