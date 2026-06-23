#include <WiFi.h>
#include <WebServer.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

const char* SSID = "your_wifi_name";
const char* PASSWORD = "your_wifi_password";
const int LED_PIN = 23;
const int SENSOR_PIN = 34;
bool ledOn = false;

WebServer server(80);
Adafruit_SSD1306 display(128, 64, &Wire, -1);

String statusJson() {
  return String("{\"adc\":") + analogRead(SENSOR_PIN) +
         String(",\"led\":") + (ledOn ? "true" : "false") +
         String(",\"uptime\":") + (millis() / 1000) + "}";
}

void drawDisplay() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println("Week3 IoT Panel");
  display.print("IP: ");
  display.println(WiFi.localIP());
  display.print("ADC: ");
  display.println(analogRead(SENSOR_PIN));
  display.print("LED: ");
  display.println(ledOn ? "ON" : "OFF");
  display.display();
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Wire.begin(21, 22);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.setTextColor(SSD1306_WHITE);

  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.println(WiFi.localIP());

  server.on("/", []() {
    server.send(200, "text/html",
      "<h1>ESP32 IoT Panel</h1>"
      "<p><a href='/on'>LED ON</a> <a href='/off'>LED OFF</a></p>"
      "<p><a href='/status'>JSON Status</a></p>");
  });
  server.on("/status", []() { server.send(200, "application/json", statusJson()); });
  server.on("/on", []() { ledOn = true; digitalWrite(LED_PIN, HIGH); server.sendHeader("Location", "/"); server.send(302); });
  server.on("/off", []() { ledOn = false; digitalWrite(LED_PIN, LOW); server.sendHeader("Location", "/"); server.send(302); });
  server.begin();
}

void loop() {
  server.handleClient();
  static unsigned long lastDisplay = 0;
  if (millis() - lastDisplay >= 300) {
    lastDisplay = millis();
    drawDisplay();
  }
}
