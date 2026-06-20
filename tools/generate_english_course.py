from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
EN_ROOT = ROOT / "en"
EN_DAYS = EN_ROOT / "days"


LINKS = [
    ("ESP32 Arduino Core", "https://docs.espressif.com/projects/arduino-esp32/en/latest/"),
    ("ESP-IDF Programming Guide", "https://docs.espressif.com/projects/esp-idf/en/latest/esp32/"),
    ("ESP32 Datasheet", "https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf"),
    ("ESP32 Technical Reference Manual", "https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf"),
    ("PlatformIO ESP32", "https://docs.platformio.org/en/latest/platforms/espressif32.html"),
    ("Wokwi ESP32 Simulator", "https://docs.wokwi.com/guides/esp32"),
    ("Random Nerd Tutorials ESP32", "https://randomnerdtutorials.com/projects-esp32/"),
    ("Adafruit SSD1306 Guide", "https://learn.adafruit.com/monochrome-oled-breakouts"),
    ("PubSubClient MQTT", "https://pubsubclient.knolleary.net/"),
    ("MQTT Essentials", "https://www.hivemq.com/mqtt-essentials/"),
]


DAYS = [
    ("ESP32, Dev Boards, and the Hardware Programming Map", "Build the mental map for ESP32 learning: board, breadboard, jumper wires, power, GPIO, and safety boundaries.", "Inventory your components and sketch your first hardware workstation."),
    ("Development Environment and Your First Blink", "Install Arduino IDE or PlatformIO, configure the board and port, upload firmware, and blink an LED.", "Upload a Blink sketch and make the onboard or external LED flash once per second."),
    ("Breadboards, Resistors, LEDs, and Safe Wiring", "Understand closed circuits, LED polarity, current-limiting resistors, and safe wiring habits.", "Move from the onboard LED to an external LED on a breadboard."),
    ("GPIO Digital Output and Chaser LEDs", "Control multiple GPIO outputs and start thinking in states instead of one-off statements.", "Build a three-LED chaser and change its direction and speed."),
    ("Button Input, Pull-ups, and Debouncing", "Read a button, understand pull-up logic, and handle mechanical bounce.", "Press a button once to toggle an LED."),
    ("Serial Monitor: Let the ESP32 Speak", "Use Serial output as your primary debugging window.", "Log every button and LED state change to the serial monitor."),
    ("Week 1 Project: Adjustable Blinking Controller", "Combine LEDs, buttons, and serial logs into a small interactive device.", "Short press to switch mode, long press or mode changes to adjust blinking speed."),
    ("PWM: Make an LED Breathe", "Understand PWM frequency, duty cycle, channels, and ESP32 LEDC output.", "Create a breathing LED and tune the fade speed."),
    ("ADC: Read a Potentiometer", "Read analog voltage, understand ADC resolution, noise, and mapping.", "Use a potentiometer to control LED brightness."),
    ("Sensor Basics: Temperature, Light, Sound, and Distance", "Learn how to identify sensor power, interface type, signal level, and data-sheet constraints.", "Create a comparison table for four common sensor types."),
    ("I2C Bus: Many Devices on Two Wires", "Understand SDA, SCL, addresses, pull-ups, and bus scanning.", "Run an I2C scanner and find your OLED address."),
    ("OLED Display: Text, Values, and Status", "Drive an SSD1306 OLED and display useful device state.", "Build a tiny dashboard showing uptime, button state, and ADC value."),
    ("SPI and High-Speed Peripherals", "Understand MOSI, MISO, SCLK, CS, and when SPI is better than I2C.", "Draw an I2C vs SPI wiring comparison and list real use cases."),
    ("Buzzers, Relays, and Actuators", "Learn that outputs include sound, relay control, and motion, not just LEDs.", "Trigger a buzzer with a button and mirror the status with an LED."),
    ("Week 2 Project: Desktop Environment Monitor", "Combine OLED, a button, ADC or a sensor, and an alert LED.", "Display sensor values, switch pages, and show threshold alerts."),
    ("Wi-Fi Basics: Connect to a Router", "Connect ESP32 to Wi-Fi and understand SSID, password, IP, gateway, DNS, and reconnects.", "Connect to your 2.4GHz Wi-Fi and print IP address and RSSI."),
    ("HTTP Client: Request Network Data", "Use HTTP GET and understand URLs, status codes, response bodies, and timeouts.", "Request a public or local API and print the response."),
    ("Web Server: Control an LED from Your Phone", "Run a web server on ESP32 and control GPIO from a browser.", "Open the ESP32 IP on your phone and toggle an LED."),
    ("JSON and Device State", "Represent device state as structured data that can be sent over the network.", "Print LED state, ADC value, and uptime as JSON."),
    ("MQTT Basics: Publish and Subscribe", "Understand brokers, topics, publish, subscribe, QoS, and keepalive.", "Publish device status and subscribe to LED commands."),
    ("BLE Basics: Nearby Device Communication", "Understand BLE, GATT, services, characteristics, and UUIDs.", "Advertise a BLE device and expose a readable status value."),
    ("Cloud Data and Dashboard Thinking", "Understand how device data flows to cloud platforms, databases, and dashboards.", "Design a device-to-cloud data format and pick a platform to try later."),
    ("Week 3 Project: Phone Control and Data Reporting", "Combine Wi-Fi, Web, HTTP or MQTT, OLED, and LED into a connected mini system.", "Control an LED from a phone and display network status locally."),
    ("Code Structure: From Working to Maintainable", "Split hardware setup, input reading, output updates, display, and network logic.", "Refactor a previous project into clear functions."),
    ("Timers, millis, and Non-Blocking Programs", "Replace heavy delay calls with millis-based task scheduling.", "Blink LED, read button, and refresh display without blocking each other."),
    ("Low Power and Battery-Powered Thinking", "Understand deep sleep, wake sources, battery capacity, and power budgets.", "Wake periodically, print a log, then return to deep sleep."),
    ("Troubleshooting: Upload Failures and Wiring Bugs", "Build a systematic checklist for hardware debugging.", "Create your own ESP32 troubleshooting checklist."),
    ("Industry Applications: Smart Home, Industrial, Agriculture, Wearables", "Map ESP32 capabilities to real-world product scenarios.", "Choose one industry scenario and design its sensors, actuators, and communication path."),
    ("Final Project Design: Desktop IoT Console", "Design requirements, wiring, UI, data, errors, and acceptance criteria before implementation.", "Write the final project design document."),
    ("Final Project: Local Loop, Web Control, and Review", "Finish the final device, add web status/control, and turn 30 days of work into a portfolio.", "Build a desktop IoT console and write your next learning roadmap."),
]


COMMON_STEPS = [
    "Restate the goal in one sentence.",
    "Draw the wiring before touching the breadboard.",
    "Build the smallest possible circuit first.",
    "Upload a minimal sketch and observe one clear output.",
    "Open the Serial Monitor and inspect state, values, or errors.",
    "Change exactly one parameter and verify the behavior changes.",
    "Record wiring, code changes, mistakes, and one open question.",
]


TROUBLESHOOTING = [
    "Upload fails: check the USB data cable, selected board, selected port, and BOOT button timing.",
    "LED does not light: check polarity, current-limiting resistor, GND, and GPIO number.",
    "Button behaves randomly: use INPUT_PULLUP, add debounce, and shorten long jumper wires.",
    "OLED is blank: check VCC/GND/SDA/SCL and run an I2C scanner for 0x3C or 0x3D.",
    "Wi-Fi fails: use 2.4GHz Wi-Fi, verify SSID/password, and check signal strength.",
    "Complex project fails: return to the smallest single-module test before combining modules again.",
]


def links_md():
    return "\n".join(f"- [{name}]({url})" for name, url in LINKS)


def day_file(index):
    return f"day{index:02d}.md"


def clean_markdown(text):
    lines = []
    for line in text.splitlines():
        while line.startswith("    "):
            line = line[4:]
        lines.append(line)
    return "\n".join(lines).strip() + "\n"


def write_day(index, title, goal, project):
    steps = "\n".join(f"{i}. {step}" for i, step in enumerate(COMMON_STEPS, 1))
    troubleshooting = "\n".join(f"- {item}" for item in TROUBLESHOOTING)
    content = clean_markdown(dedent(f"""\
    # Day {index:02d}: {title}

    ## Goal

    {goal}

    ## What You Will Understand

    Today is about turning abstract ESP32 concepts into something observable. Hardware programming becomes easier when you always connect code, voltage, wiring, and feedback together.

    ## Hands-On Project

    **Project:** {project}

    ## Workflow

    {steps}

    ## Safety and Wiring Notes

    - ESP32 GPIO uses 3.3V logic. Do not feed 5V signals directly into GPIO pins.
    - Use a 220Ω or 330Ω resistor in series with each LED.
    - Prefer `INPUT_PULLUP` for beginner button circuits.
    - Disconnect power before changing wiring.
    - Keep a wiring table: module, VCC, GND, signal pin, ESP32 GPIO, notes.

    ## Common Problems

    {troubleshooting}

    ## Reflection

    - What did the ESP32 sense, decide, display, or control today?
    - Which symptom surprised you, and how did you debug it?
    - What would this feature become in a real product?
    - What is one question to research before the next session?

    ## Further Reading

    {links_md()}
    """))
    (EN_DAYS / day_file(index)).write_text(content, encoding="utf-8")


def write_readme():
    rows = "\n".join(
        f"| Day {i:02d} | [{title}](days/{day_file(i)}) | {goal} |"
        for i, (title, goal, _project) in enumerate(DAYS, 1)
    )
    content = clean_markdown(dedent(f"""\
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
    {rows}

    ## Summary Report

    - [Learning Summary Report](report.md)

    ## Useful Links

    {links_md()}
    """))
    (EN_ROOT / "README.md").write_text(content, encoding="utf-8")


def write_report():
    content = clean_markdown(dedent(f"""\
    # Awesome ESP32 in 30 Days

    ## 30-Day Beginner Hardware Programming Plan: Summary Report

    This learning plan is designed for beginners who own an ESP32 development board and basic hardware accessories but have not yet built a systematic hardware programming foundation.

    After 30 days, you should be able to:

    - Control LEDs, buttons, buzzers, and simple actuators.
    - Display device state on an SSD1306 OLED.
    - Read analog values and common sensor modules.
    - Connect ESP32 to Wi-Fi and expose simple web controls.
    - Represent device state as JSON and understand MQTT basics.
    - Build a small desktop IoT console with local display and phone-based control.

    ## Four Learning Stages

    ### Week 1: GPIO and Hardware Basics

    ESP32 board, breadboard, resistors, LEDs, buttons, serial debugging, and the first interactive controller.

    ### Week 2: Peripherals, Buses, and Displays

    PWM, ADC, sensors, I2C, OLED, SPI basics, buzzers, relays, and a desktop environment monitor.

    ### Week 3: Connectivity and IoT Communication

    Wi-Fi, HTTP, ESP32 WebServer, JSON, MQTT, BLE, cloud data thinking, and a connected control panel.

    ### Week 4: Engineering, Debugging, and Final Project

    Maintainable code structure, non-blocking timing, low power, troubleshooting, industry applications, and a final IoT console project.

    ## Recommended Next Steps

    - Move from Arduino-style sketches to PlatformIO projects.
    - Learn ESP-IDF for production-grade ESP32 development.
    - Study FreeRTOS tasks, queues, timers, and synchronization.
    - Learn schematic and PCB design.
    - Add OTA, device identity, logs, and security to your future projects.

    ## Useful Links

    {links_md()}
    """))
    (EN_ROOT / "report.md").write_text(content, encoding="utf-8")


def main():
    EN_DAYS.mkdir(parents=True, exist_ok=True)
    write_readme()
    write_report()
    for i, day in enumerate(DAYS, 1):
        write_day(i, *day)


if __name__ == "__main__":
    main()
