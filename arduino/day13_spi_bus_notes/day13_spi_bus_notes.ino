#include <SPI.h>

const int CS_PIN = 5;

void setup() {
  Serial.begin(115200);
  pinMode(CS_PIN, OUTPUT);
  digitalWrite(CS_PIN, HIGH);
  SPI.begin(18, 19, 23, CS_PIN); // SCK, MISO, MOSI, CS
  Serial.println("Day 13 - SPI bus wiring check");
  Serial.println("Default demo only toggles CS. Connect a real SPI device before data transfer.");
}

void loop() {
  digitalWrite(CS_PIN, LOW);
  delay(100);
  digitalWrite(CS_PIN, HIGH);
  Serial.println("CS pulse sent on GPIO5");
  delay(1000);
}
