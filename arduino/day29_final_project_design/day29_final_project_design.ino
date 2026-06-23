const int LED_PIN = 23;
const int BUTTON_PIN = 27;
const int SENSOR_PIN = 34;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.println("Day 29 - Final project design validation firmware");
  Serial.println("Modules: sensor input, button input, LED output, OLED display, web/API control.");
}

void loop() {
  int sensor = analogRead(SENSOR_PIN);
  bool buttonDown = digitalRead(BUTTON_PIN) == LOW;
  digitalWrite(LED_PIN, buttonDown || sensor > 2500);
  Serial.printf("sensor=%d button=%s led=%s\n",
                sensor,
                buttonDown ? "DOWN" : "UP",
                digitalRead(LED_PIN) ? "ON" : "OFF");
  delay(500);
}
