# Day 29: Final Project Design: Desktop IoT Console

## Goal

Design requirements, wiring, UI, data, errors, and acceptance criteria before implementation.

## What You Will Understand

Today is about turning abstract ESP32 concepts into something observable. Hardware programming becomes easier when you always connect code, voltage, wiring, and feedback together.

## Hands-On Project

**Project:** Write the final project design document.

## Workflow

1. Restate the goal in one sentence.
2. Draw the wiring before touching the breadboard.
3. Build the smallest possible circuit first.
4. Upload a minimal sketch and observe one clear output.
5. Open the Serial Monitor and inspect state, values, or errors.
6. Change exactly one parameter and verify the behavior changes.
7. Record wiring, code changes, mistakes, and one open question.

## Safety and Wiring Notes

- ESP32 GPIO uses 3.3V logic. Do not feed 5V signals directly into GPIO pins.
- Use a 220Ω or 330Ω resistor in series with each LED.
- Prefer `INPUT_PULLUP` for beginner button circuits.
- Disconnect power before changing wiring.
- Keep a wiring table: module, VCC, GND, signal pin, ESP32 GPIO, notes.

## Common Problems

- Upload fails: check the USB data cable, selected board, selected port, and BOOT button timing.
- LED does not light: check polarity, current-limiting resistor, GND, and GPIO number.
- Button behaves randomly: use INPUT_PULLUP, add debounce, and shorten long jumper wires.
- OLED is blank: check VCC/GND/SDA/SCL and run an I2C scanner for 0x3C or 0x3D.
- Wi-Fi fails: use 2.4GHz Wi-Fi, verify SSID/password, and check signal strength.
- Complex project fails: return to the smallest single-module test before combining modules again.

## Reflection

- What did the ESP32 sense, decide, display, or control today?
- Which symptom surprised you, and how did you debug it?
- What would this feature become in a real product?
- What is one question to research before the next session?

## Further Reading

- [ESP32 Arduino Core](https://docs.espressif.com/projects/arduino-esp32/en/latest/)
- [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [ESP32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)
- [ESP32 Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf)
- [PlatformIO ESP32](https://docs.platformio.org/en/latest/platforms/espressif32.html)
- [Wokwi ESP32 Simulator](https://docs.wokwi.com/guides/esp32)
- [Random Nerd Tutorials ESP32](https://randomnerdtutorials.com/projects-esp32/)
- [Adafruit SSD1306 Guide](https://learn.adafruit.com/monochrome-oled-breakouts)
- [PubSubClient MQTT](https://pubsubclient.knolleary.net/)
- [MQTT Essentials](https://www.hivemq.com/mqtt-essentials/)
