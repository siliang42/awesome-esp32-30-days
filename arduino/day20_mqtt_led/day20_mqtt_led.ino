#include <WiFi.h>
#include <PubSubClient.h>

const char* SSID = "your_wifi_name";
const char* PASSWORD = "your_wifi_password";
const char* MQTT_HOST = "broker.hivemq.com";
const int LED_PIN = 23;

WiFiClient wifiClient;
PubSubClient mqtt(wifiClient);

void callback(char* topic, byte* payload, unsigned int length) {
  String message;
  for (unsigned int i = 0; i < length; i++) message += (char)payload[i];
  digitalWrite(LED_PIN, message == "on" ? HIGH : LOW);
}

void reconnect() {
  while (!mqtt.connected()) {
    if (mqtt.connect("esp32-demo-client")) {
      mqtt.subscribe("esp32/demo/led");
    } else {
      delay(2000);
    }
  }
}

void setup() {
  pinMode(LED_PIN, OUTPUT);
  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  mqtt.setServer(MQTT_HOST, 1883);
  mqtt.setCallback(callback);
}

void loop() {
  if (!mqtt.connected()) reconnect();
  mqtt.loop();
  mqtt.publish("esp32/demo/status", "online");
  delay(2000);
}
