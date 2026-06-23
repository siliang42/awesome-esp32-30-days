const int LED_PIN = 23;
const int SENSOR_PIN = 34;

struct DeviceState {
  bool ledOn;
  int sensorValue;
  unsigned long uptimeSeconds;
};

DeviceState state;

void setupHardware() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
}

void readInputs() {
  state.sensorValue = analogRead(SENSOR_PIN);
  state.uptimeSeconds = millis() / 1000;
}

void updateOutputs() {
  state.ledOn = state.sensorValue > 2500;
  digitalWrite(LED_PIN, state.ledOn);
}

void printState() {
  Serial.printf("adc=%d led=%s uptime=%lu\n",
    state.sensorValue,
    state.ledOn ? "on" : "off",
    state.uptimeSeconds);
}

void setup() {
  setupHardware();
}

void loop() {
  readInputs();
  updateOutputs();
  printState();
  delay(500);
}
