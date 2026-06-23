#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>

BLECharacteristic* statusCharacteristic;

void setup() {
  BLEDevice::init("ESP32-BLE-Demo");
  BLEServer* server = BLEDevice::createServer();
  BLEService* service = server->createService("12345678-1234-1234-1234-1234567890ab");
  statusCharacteristic = service->createCharacteristic(
    "abcd1234-1234-1234-1234-abcdef123456",
    BLECharacteristic::PROPERTY_READ
  );
  statusCharacteristic->setValue("hello from esp32");
  service->start();
  BLEDevice::getAdvertising()->start();
}

void loop() {
}
