#include <WiFi.h>
#include <HTTPClient.h>

const char* SSID = "your_wifi_name";
const char* PASSWORD = "your_wifi_password";

void setup() {
  Serial.begin(115200);
  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) delay(500);

  HTTPClient http;
  http.begin("http://worldtimeapi.org/api/timezone/Asia/Shanghai");
  int code = http.GET();
  Serial.print("HTTP status: ");
  Serial.println(code);
  if (code > 0) {
    Serial.println(http.getString());
  }
  http.end();
}

void loop() {
}
