# Awesome ESP32 in 30 Days

## 30-Day Beginner Hardware Programming Plan

[中文](../README.md) | English

A bilingual, beginner-friendly ESP32 hardware programming course for people who already have an ESP32 dev board, breadboard, LEDs, buttons, OLED display, and common accessories. The course connects ESP32, Arduino IDE / PlatformIO, GPIO, PWM, ADC, I2C, SPI, OLED, Wi-Fi, HTTP, MQTT, BLE, low power, and a final IoT project into a practical 30-day learning path.

This project is designed for beginners, software developers entering embedded systems, and makers who want to build real smart hardware prototypes instead of only copying isolated demos.

## Project Snapshot

| Item | Details |
|---|---|
| Course | ESP32 beginner course in 30 days |
| Hardware | ESP32 board, breadboard, jumper wires, LEDs, buttons, resistors, OLED, sensors |
| Tools | Arduino IDE, PlatformIO, Serial Monitor, Wokwi simulator |
| Topics | GPIO, PWM, ADC, I2C, SPI, OLED, Wi-Fi, HTTP, JSON, MQTT, BLE, low power |
| Outputs | 30 daily lessons, 1 summary report, 4 staged projects, 1 final IoT console |

## One-Sentence Citation

`Awesome ESP32 in 30 Days` is a bilingual ESP32 beginner course that teaches hardware programming, GPIO, sensors, OLED, Wi-Fi, MQTT, BLE, low power, and a final IoT project through 30 daily Markdown lessons.

## Keywords

ESP32 tutorial, ESP32 beginner course, ESP32 30 day learning plan, hardware programming, embedded systems, IoT development, Arduino ESP32, PlatformIO ESP32, GPIO, PWM, ADC, I2C, SPI, OLED, MQTT, BLE, low power, smart hardware.

## What You Get

- A 30-day path from component recognition to connected IoT prototypes.
- One Markdown document per day with goals, workflow, safety notes, debugging tips, and reflection prompts.
- A summary report that explains the full learning map.
- Useful official and community links for deeper study.

## 30-Day Table of Contents

| Day | Topic and Keywords | Outcome |
|---|---|---|
| Day&nbsp;01 | [ESP32 and the Hardware Programming Map](days/day01.md) | Understand the board, breadboard, power, GPIO, and safety boundaries. |
| Day&nbsp;02 | [Development Environment and Blink](days/day02.md) | Configure Arduino IDE / PlatformIO, serial port, board package, and LED upload. |
| Day&nbsp;03 | [Breadboards, Resistors, and LED Wiring](days/day03.md) | Build a safe LED circuit with polarity, current limiting, and shared ground. |
| Day&nbsp;04 | [GPIO Digital Output](days/day04.md) | Control multiple GPIO pins and start modeling behavior as states. |
| Day&nbsp;05 | [Button Input and Debouncing](days/day05.md) | Read buttons with pull-ups and handle mechanical bounce. |
| Day&nbsp;06 | [Serial Monitor Debugging](days/day06.md) | Use Serial logs to inspect variables, states, and errors. |
| Day&nbsp;07 | [Week 1 Project: Blinking Controller](days/day07.md) | Combine LEDs, buttons, and serial logs into an interactive device. |
| Day&nbsp;08 | [PWM Breathing LED](days/day08.md) | Control brightness with frequency, duty cycle, channel, and ESP32 LEDC. |
| Day&nbsp;09 | [ADC and Potentiometer Input](days/day09.md) | Read analog voltage and understand resolution, range, noise, and mapping. |
| Day&nbsp;10 | [Sensor Basics](days/day10.md) | Judge sensors by power, interface, signal level, and data sheet. |
| Day&nbsp;11 | [I2C Bus Scanning](days/day11.md) | Understand SDA, SCL, addresses, pull-ups, and multiple I2C devices. |
| Day&nbsp;12 | [OLED Dashboard](days/day12.md) | Drive SSD1306 OLED and show text, values, icons, and device status. |
| Day&nbsp;13 | [SPI Peripherals](days/day13.md) | Compare MOSI, MISO, SCLK, CS, and SPI versus I2C. |
| Day&nbsp;14 | [Buzzers, Relays, and Actuators](days/day14.md) | Expand output thinking to sound, relay control, and motion. |
| Day&nbsp;15 | [Week 2 Project: Environment Monitor](days/day15.md) | Combine OLED, button, ADC or sensor, and alert output. |
| Day&nbsp;16 | [Wi-Fi Basics](days/day16.md) | Connect to 2.4GHz Wi-Fi and understand SSID, IP, gateway, DNS, reconnects. |
| Day&nbsp;17 | [HTTP Client Requests](days/day17.md) | Use HTTP GET and understand URLs, status codes, response bodies, and timeouts. |
| Day&nbsp;18 | [ESP32 Web Server](days/day18.md) | Control GPIO from a phone browser through an ESP32-hosted page. |
| Day&nbsp;19 | [JSON Device State](days/day19.md) | Represent device state as structured JSON for network exchange. |
| Day&nbsp;20 | [MQTT Publish and Subscribe](days/day20.md) | Understand broker, topic, publish, subscribe, QoS, and keepalive. |
| Day&nbsp;21 | [BLE Nearby Communication](days/day21.md) | Learn BLE, GATT, services, characteristics, and near-field control. |
| Day&nbsp;22 | [Cloud Data and Dashboards](days/day22.md) | Trace data from device to cloud, database, and visualization. |
| Day&nbsp;23 | [Week 3 Project: Connected Control System](days/day23.md) | Combine Wi-Fi, Web, HTTP/MQTT, OLED, and LED into a closed loop. |
| Day&nbsp;24 | [Maintainable Code Structure](days/day24.md) | Split configuration, hardware drivers, business logic, display, and network code. |
| Day&nbsp;25 | [millis and Non-Blocking Programs](days/day25.md) | Replace delay-heavy code with millis-based periodic tasks. |
| Day&nbsp;26 | [Low Power and Deep Sleep](days/day26.md) | Estimate deep sleep, wake sources, battery capacity, and power budget. |
| Day&nbsp;27 | [Hardware Troubleshooting](days/day27.md) | Debug from power, wiring, serial logs, board settings, and code. |
| Day&nbsp;28 | [Industry Applications](days/day28.md) | Map ESP32 to smart home, industrial data, agriculture, and wearables. |
| Day&nbsp;29 | [Final Project Design](days/day29.md) | Design the desktop IoT console requirements, wiring, UI, data, and errors. |
| Day&nbsp;30 | [Final Project and Review](days/day30.md) | Finish local I/O, OLED, web control, status API, and portfolio review. |

## Summary Report

- [Learning Summary Report](report.md)

## Wiki and AI-Friendly Entrypoints

- [中文 Wiki 导航](../wiki/Home.md)
- [English Wiki Home](../wiki/English-Home.md)
- [llms.txt](../llms.txt): concise course index for AI tools and citation.
- [robots.txt](../robots.txt): crawler entrypoint.

## Useful Links

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
