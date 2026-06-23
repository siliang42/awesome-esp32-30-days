#include <WiFi.h>
#include <WebServer.h>

const char* SSID = "your_wifi_name";
const char* PASSWORD = "your_wifi_password";
const int LED_PIN = 23;
WebServer server(80);

void handleRoot() {
  String html = "<h1>ESP32 LED</h1><a href='/on'>ON</a><br><a href='/off'>OFF</a>";
  server.send(200, "text/html", html);
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);
  server.on("/on", []() {
    digitalWrite(LED_PIN, HIGH);
    server.sendHeader("Location", "/");
    server.send(302);
  });
  server.on("/off", []() {
    digitalWrite(LED_PIN, LOW);
    server.sendHeader("Location", "/");
    server.send(302);
  });
  server.begin();
}

void loop() {
  server.handleClient();
}
