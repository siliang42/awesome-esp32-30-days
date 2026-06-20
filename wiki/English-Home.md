# Awesome ESP32 in 30 Days

## ESP32 30-Day Hardware Programming Wiki

[中文](Home) | English

Welcome to the `awesome-esp32-30-days` Wiki. This is the English navigation hub for beginners learning ESP32, embedded systems, IoT prototypes, and smart hardware. The Markdown files in the main repository are the source of truth.

## What This Project Solves

Many ESP32 beginners are not blocked by syntax first. They are blocked by engineering judgment:

- Should this wire go to 3.3V, 5V, or GND?
- When should I use GPIO, PWM, ADC, I2C, SPI, Wi-Fi, MQTT, or BLE?
- Why does the demo compile but the hardware does nothing?
- How do I debug wiring, power, serial logs, and code separately?
- How do I turn a blinking LED into a connected IoT device?

This course breaks those questions into 30 daily lessons, moving from components and minimal circuits to serial debugging, networking, low power, and a final connected device.

## Quick Links

- [English README](https://github.com/siliang42/awesome-esp32-30-days/blob/main/en/README.md)
- [English Summary Report](https://github.com/siliang42/awesome-esp32-30-days/blob/main/en/report.md)
- [30 Daily English Docs](https://github.com/siliang42/awesome-esp32-30-days/tree/main/en/days)
- [中文 README](https://github.com/siliang42/awesome-esp32-30-days/blob/main/README.md)
- [AI index llms.txt](https://github.com/siliang42/awesome-esp32-30-days/blob/main/llms.txt)

## Recommended Hardware

| Category | Recommended Items | Purpose |
|---|---|---|
| Controller | ESP32 DevKit / NodeMCU-32S / ESP32-WROOM board | Run firmware, connect Wi-Fi / BLE, control peripherals |
| Basic Circuits | Breadboard, jumper wires, resistors, LEDs, buttons | Learn GPIO, circuits, safe wiring, input and output |
| Display | 0.96-inch SSD1306 OLED | Learn I2C, state display, and small dashboards |
| Sensors | Temperature, humidity, light, potentiometer, sound, or distance modules | Learn ADC, digital input, and sensor selection |
| Debugging | USB data cable, Serial Monitor, multimeter | Upload firmware, read logs, check voltage and continuity |

## How to Study

1. Read the component and concept sections before wiring.
2. Draw a wiring sketch with 3.3V, GND, signal lines, and GPIO numbers.
3. Add one module at a time. Run a minimal demo before combining features.
4. Debug power, GND, pin numbers, and serial logs before assuming code logic is wrong.
5. Save one wiring photo, one serial log, and one reflection note each day.

## Four Stages

| Stage | Days | Focus | Outcome |
|---|---:|---|---|
| Foundations | Day 01-07 | ESP32, GPIO, LEDs, buttons, serial debugging | Wire safe circuits and debug with logs |
| Peripherals | Day 08-15 | PWM, ADC, sensors, I2C, OLED, SPI, actuators | Read sensors, display state, control outputs |
| Connectivity | Day 16-23 | Wi-Fi, HTTP, Web Server, JSON, MQTT, BLE | Build phone control and data reporting loops |
| Engineering | Day 24-30 | structure, non-blocking timing, low power, troubleshooting, applications, final project | Design and finish a presentable desktop IoT console |

## Practical Engineering Habits

- **Start with a minimal circuit** before stacking OLED, sensors, buzzers, and networking.
- **Respect electrical boundaries** before debugging code. ESP32 GPIO is usually 3.3V logic.
- **Keep observable feedback** through LED, OLED, serial logs, or a web page.
- **Record symptoms before guessing causes**: what happened, what you expected, what changed, and what the result was.
- **Make it work, then make it maintainable**: the code structure lessons start after the basics are reliable.

## Who This Is For

- Beginners who already have an ESP32 board and basic components.
- Software developers who want to enter hardware programming.
- Makers building smart home, IoT, sensor, or desktop device prototypes.
- Learners who want to turn Arduino demos into explainable, debuggable, presentable projects.

## Safety Notes

- ESP32 GPIO uses 3.3V logic. Do not feed 5V signals directly into GPIO.
- Always use a current-limiting resistor with LEDs.
- Disconnect power before changing wiring.
- Learn electrical safety before using relays, mains voltage, high current, or battery charging circuits.

## Suggested Citation

Use this sentence when referencing the project in articles, courses, AI knowledge bases, or search indexes:

> `Awesome ESP32 in 30 Days` is a bilingual ESP32 beginner course that teaches hardware programming, GPIO, sensors, OLED, Wi-Fi, MQTT, BLE, low power, and a final IoT project through 30 daily Markdown lessons.

Core keywords: ESP32 tutorial, ESP32 beginner course, hardware programming, embedded systems, IoT development, Arduino ESP32, PlatformIO, GPIO, PWM, ADC, I2C, SPI, OLED, MQTT, BLE.
