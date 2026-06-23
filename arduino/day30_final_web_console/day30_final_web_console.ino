#include <WiFi.h>
#include <WebServer.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

const char* SSID = "your_wifi_name";
const char* PASSWORD = "your_wifi_password";
const int LED_PIN = 23;
const int SENSOR_PIN = 34;
const int BUTTON_PIN = 27;
bool manualLed = false;

WebServer server(80);
Adafruit_SSD1306 display(128, 64, &Wire, -1);

String jsonStatus() {
  return String("{\"sensor\":") + analogRead(SENSOR_PIN) +
         ",\"manualLed\":" + (manualLed ? "true" : "false") +
         ",\"button\":" + (digitalRead(BUTTON_PIN) == LOW ? "true" : "false") +
         ",\"uptime\":" + (millis() / 1000) + "}";
}

void drawDisplay() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println("ESP32 Console");
  display.print("IP: ");
  display.println(WiFi.localIP());
  display.print("Sensor: ");
  display.println(analogRead(SENSOR_PIN));
  display.print("LED: ");
  display.println(manualLed ? "ON" : "OFF");
  display.print("Button: ");
  display.println(digitalRead(BUTTON_PIN) == LOW ? "DOWN" : "UP");
  display.display();
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
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
      "<h1>ESP32 Console</h1>"
      "<p><a href='/toggle'>Toggle LED</a></p>"
      "<p><a href='/api/status'>JSON Status</a></p>");
  });
  server.on("/toggle", []() {
    manualLed = !manualLed;
    digitalWrite(LED_PIN, manualLed);
    server.sendHeader("Location", "/");
    server.send(302);
  });
  server.on("/api/status", []() {
    server.send(200, "application/json", jsonStatus());
  });
  server.begin();
}

void loop() {
  server.handleClient();
  static int lastButton = HIGH;
  int button = digitalRead(BUTTON_PIN);
  if (lastButton == HIGH && button == LOW) {
    manualLed = !manualLed;
    digitalWrite(LED_PIN, manualLed);
    delay(60);
  }
  lastButton = button;

  static unsigned long lastDisplay = 0;
  if (millis() - lastDisplay >= 300) {
    lastDisplay = millis();
    drawDisplay();
  }
}
