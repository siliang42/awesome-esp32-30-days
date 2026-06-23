#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 display(128, 64, &Wire, -1);
const int POT_PIN = 34;
const int LED_PIN = 23;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Wire.begin(21, 22);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.setTextColor(SSD1306_WHITE);
}

void loop() {
  int value = analogRead(POT_PIN);
  digitalWrite(LED_PIN, value > 2500 ? HIGH : LOW);
  display.clearDisplay();
  display.setCursor(0, 0);
  display.setTextSize(1);
  display.println("Desk Monitor");
  display.print("Sensor: ");
  display.println(value);
  display.print("Alert: ");
  display.println(value > 2500 ? "YES" : "NO");
  display.display();
  delay(250);
}
