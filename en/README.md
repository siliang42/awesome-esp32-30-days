# Awesome ESP32 in 30 Days

## 30-Day Beginner Hardware Programming Plan

[中文](../README.md) | English

A bilingual, beginner-friendly ESP32 learning path for people who already have an ESP32 dev board, breadboard, LEDs, buttons, OLED display, and common accessories.

## What You Get

- A 30-day path from component recognition to connected IoT prototypes.
- One Markdown document per day with goals, workflow, safety notes, debugging tips, and reflection prompts.
- A summary report that explains the full learning map.
- Useful official and community links for deeper study.

## 30-Day Table of Contents

| Day | Topic | Goal |
|---|---|---|
| Day 01 | [ESP32, Dev Boards, and the Hardware Programming Map](days/day01.md) | Build the mental map for ESP32 learning: board, breadboard, jumper wires, power, GPIO, and safety boundaries. |
| Day 02 | [Development Environment and Your First Blink](days/day02.md) | Install Arduino IDE or PlatformIO, configure the board and port, upload firmware, and blink an LED. |
| Day 03 | [Breadboards, Resistors, LEDs, and Safe Wiring](days/day03.md) | Understand closed circuits, LED polarity, current-limiting resistors, and safe wiring habits. |
| Day 04 | [GPIO Digital Output and Chaser LEDs](days/day04.md) | Control multiple GPIO outputs and start thinking in states instead of one-off statements. |
| Day 05 | [Button Input, Pull-ups, and Debouncing](days/day05.md) | Read a button, understand pull-up logic, and handle mechanical bounce. |
| Day 06 | [Serial Monitor: Let the ESP32 Speak](days/day06.md) | Use Serial output as your primary debugging window. |
| Day 07 | [Week 1 Project: Adjustable Blinking Controller](days/day07.md) | Combine LEDs, buttons, and serial logs into a small interactive device. |
| Day 08 | [PWM: Make an LED Breathe](days/day08.md) | Understand PWM frequency, duty cycle, channels, and ESP32 LEDC output. |
| Day 09 | [ADC: Read a Potentiometer](days/day09.md) | Read analog voltage, understand ADC resolution, noise, and mapping. |
| Day 10 | [Sensor Basics: Temperature, Light, Sound, and Distance](days/day10.md) | Learn how to identify sensor power, interface type, signal level, and data-sheet constraints. |
| Day 11 | [I2C Bus: Many Devices on Two Wires](days/day11.md) | Understand SDA, SCL, addresses, pull-ups, and bus scanning. |
| Day 12 | [OLED Display: Text, Values, and Status](days/day12.md) | Drive an SSD1306 OLED and display useful device state. |
| Day 13 | [SPI and High-Speed Peripherals](days/day13.md) | Understand MOSI, MISO, SCLK, CS, and when SPI is better than I2C. |
| Day 14 | [Buzzers, Relays, and Actuators](days/day14.md) | Learn that outputs include sound, relay control, and motion, not just LEDs. |
| Day 15 | [Week 2 Project: Desktop Environment Monitor](days/day15.md) | Combine OLED, a button, ADC or a sensor, and an alert LED. |
| Day 16 | [Wi-Fi Basics: Connect to a Router](days/day16.md) | Connect ESP32 to Wi-Fi and understand SSID, password, IP, gateway, DNS, and reconnects. |
| Day 17 | [HTTP Client: Request Network Data](days/day17.md) | Use HTTP GET and understand URLs, status codes, response bodies, and timeouts. |
| Day 18 | [Web Server: Control an LED from Your Phone](days/day18.md) | Run a web server on ESP32 and control GPIO from a browser. |
| Day 19 | [JSON and Device State](days/day19.md) | Represent device state as structured data that can be sent over the network. |
| Day 20 | [MQTT Basics: Publish and Subscribe](days/day20.md) | Understand brokers, topics, publish, subscribe, QoS, and keepalive. |
| Day 21 | [BLE Basics: Nearby Device Communication](days/day21.md) | Understand BLE, GATT, services, characteristics, and UUIDs. |
| Day 22 | [Cloud Data and Dashboard Thinking](days/day22.md) | Understand how device data flows to cloud platforms, databases, and dashboards. |
| Day 23 | [Week 3 Project: Phone Control and Data Reporting](days/day23.md) | Combine Wi-Fi, Web, HTTP or MQTT, OLED, and LED into a connected mini system. |
| Day 24 | [Code Structure: From Working to Maintainable](days/day24.md) | Split hardware setup, input reading, output updates, display, and network logic. |
| Day 25 | [Timers, millis, and Non-Blocking Programs](days/day25.md) | Replace heavy delay calls with millis-based task scheduling. |
| Day 26 | [Low Power and Battery-Powered Thinking](days/day26.md) | Understand deep sleep, wake sources, battery capacity, and power budgets. |
| Day 27 | [Troubleshooting: Upload Failures and Wiring Bugs](days/day27.md) | Build a systematic checklist for hardware debugging. |
| Day 28 | [Industry Applications: Smart Home, Industrial, Agriculture, Wearables](days/day28.md) | Map ESP32 capabilities to real-world product scenarios. |
| Day 29 | [Final Project Design: Desktop IoT Console](days/day29.md) | Design requirements, wiring, UI, data, errors, and acceptance criteria before implementation. |
| Day 30 | [Final Project: Local Loop, Web Control, and Review](days/day30.md) | Finish the final device, add web status/control, and turn 30 days of work into a portfolio. |

## Summary Report

- [Learning Summary Report](report.md)

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
