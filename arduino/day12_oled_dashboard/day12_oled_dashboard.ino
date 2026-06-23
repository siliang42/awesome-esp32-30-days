#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 display(128, 64, &Wire, -1);
const int BUTTON_PIN = 27;
const int POT_PIN = 34;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Wire.begin(21, 22);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
}

void loop() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println("ESP32 Dashboard");
  display.print("Seconds: ");
  display.println(millis() / 1000);
  display.print("Button: ");
  display.println(digitalRead(BUTTON_PIN) == LOW ? "DOWN" : "UP");
  display.print("ADC: ");
  display.println(analogRead(POT_PIN));
  display.display();
  delay(200);
}
