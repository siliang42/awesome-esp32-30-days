from pathlib import Path
from html import escape

from generate_course import DAYS, CODE_SNIPPETS


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "arduino"


SLUGS = [
    "esp32_overview",
    "blink",
    "safe_led_wiring",
    "gpio_chaser",
    "button_debounce",
    "serial_debug",
    "week1_blink_controller",
    "pwm_breath_led",
    "adc_pot_pwm",
    "sensor_catalog",
    "i2c_scanner",
    "oled_dashboard",
    "spi_bus_notes",
    "buzzer_button",
    "week2_desk_monitor",
    "wifi_connect",
    "http_get",
    "web_led_control",
    "json_status",
    "mqtt_led",
    "ble_basic",
    "cloud_payload_design",
    "week3_iot_panel",
    "structured_project",
    "millis_scheduler",
    "deep_sleep",
    "hardware_troubleshooting",
    "industry_app_planner",
    "final_project_design",
    "final_web_console",
]


OVERRIDE_SNIPPETS = {
    "esp32_overview": """\
const int LED_PIN = 2;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println();
  Serial.println("Day 01 - ESP32 hardware overview");
  Serial.println("Check board, USB data cable, 3.3V, GND, GPIO labels, and breadboard rails.");
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  Serial.println("ESP32 is running. If this blinks, upload and power are OK.");
  delay(500);
  digitalWrite(LED_PIN, LOW);
  delay(1500);
}
""",
    "button_toggle": """\
const int BUTTON_PIN = 27;
const int LED_PIN = 23;

bool ledOn = false;
int lastReading = HIGH;
int stableState = HIGH;
unsigned long lastDebounceTime = 0;
const unsigned long debounceDelay = 40;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int reading = digitalRead(BUTTON_PIN);

  if (reading != lastReading) {
    lastDebounceTime = millis();
    lastReading = reading;
  }

  if ((millis() - lastDebounceTime) > debounceDelay && reading != stableState) {
    stableState = reading;
    if (stableState == LOW) {
      ledOn = !ledOn;
      digitalWrite(LED_PIN, ledOn ? HIGH : LOW);
    }
  }
}
""",
    "pwm_breath": """\
const int LED_PIN = 23;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  for (int duty = 0; duty <= 255; duty++) {
    analogWrite(LED_PIN, duty);
    delay(8);
  }
  for (int duty = 255; duty >= 0; duty--) {
    analogWrite(LED_PIN, duty);
    delay(8);
  }
}
""",
    "adc_pot_pwm": """\
const int POT_PIN = 34;
const int LED_PIN = 23;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int raw = analogRead(POT_PIN);
  int duty = map(raw, 0, 4095, 0, 255);
  analogWrite(LED_PIN, duty);
  Serial.printf("ADC=%d, duty=%d\\n", raw, duty);
  delay(100);
}
""",
    "sensor_catalog": """\
const int ANALOG_SENSOR_PIN = 34;
const int DIGITAL_SENSOR_PIN = 27;

void setup() {
  Serial.begin(115200);
  pinMode(DIGITAL_SENSOR_PIN, INPUT_PULLUP);
  Serial.println("Day 10 - Sensor catalog probe");
  Serial.println("Use GPIO34 for analog modules and GPIO27 for digital threshold modules.");
}

void loop() {
  int analogValue = analogRead(ANALOG_SENSOR_PIN);
  int digitalValue = digitalRead(DIGITAL_SENSOR_PIN);
  Serial.printf("analog=%d, digital=%s\\n", analogValue, digitalValue == LOW ? "ACTIVE" : "IDLE");
  delay(500);
}
""",
    "spi_bus_notes": """\
#include <SPI.h>

const int CS_PIN = 5;

void setup() {
  Serial.begin(115200);
  pinMode(CS_PIN, OUTPUT);
  digitalWrite(CS_PIN, HIGH);
  SPI.begin(18, 19, 23, CS_PIN); // SCK, MISO, MOSI, CS
  Serial.println("Day 13 - SPI bus wiring check");
  Serial.println("Default demo only toggles CS. Connect a real SPI device before data transfer.");
}

void loop() {
  digitalWrite(CS_PIN, LOW);
  delay(100);
  digitalWrite(CS_PIN, HIGH);
  Serial.println("CS pulse sent on GPIO5");
  delay(1000);
}
""",
    "cloud_payload_design": """\
const int SENSOR_PIN = 34;
const char* DEVICE_ID = "esp32-desk-001";

void setup() {
  Serial.begin(115200);
  Serial.println("Day 22 - Cloud payload design");
}

void loop() {
  int sensor = analogRead(SENSOR_PIN);
  unsigned long uptime = millis() / 1000;
  Serial.printf("{\\"deviceId\\":\\"%s\\",\\"sensor\\":%d,\\"uptime\\":%lu,\\"unit\\":\\"raw\\"}\\n",
                DEVICE_ID, sensor, uptime);
  delay(1000);
}
""",
    "hardware_troubleshooting": """\
const int LED_PIN = 23;
const int BUTTON_PIN = 27;
const int ADC_PIN = 34;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.println("Day 27 - Hardware troubleshooting probe");
  Serial.println("Check: power -> GND -> pin number -> minimal code -> library/network.");
}

void loop() {
  static bool led = false;
  led = !led;
  digitalWrite(LED_PIN, led);
  Serial.printf("LED=%s, button=%s, adc=%d\\n",
                led ? "ON" : "OFF",
                digitalRead(BUTTON_PIN) == LOW ? "DOWN" : "UP",
                analogRead(ADC_PIN));
  delay(1000);
}
""",
    "industry_app_planner": """\
const int SENSOR_PIN = 34;
const int LED_PIN = 23;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("Day 28 - Industry application probe");
  Serial.println("Scenario examples: smart home, agriculture, industrial data node, wearable.");
}

void loop() {
  int value = analogRead(SENSOR_PIN);
  bool alarm = value > 2600;
  digitalWrite(LED_PIN, alarm);
  Serial.printf("scenario=environment_monitor sensor=%d alarm=%s\\n", value, alarm ? "true" : "false");
  delay(1000);
}
""",
    "final_project_design": """\
const int LED_PIN = 23;
const int BUTTON_PIN = 27;
const int SENSOR_PIN = 34;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.println("Day 29 - Final project design validation firmware");
  Serial.println("Modules: sensor input, button input, LED output, OLED display, web/API control.");
}

void loop() {
  int sensor = analogRead(SENSOR_PIN);
  bool buttonDown = digitalRead(BUTTON_PIN) == LOW;
  digitalWrite(LED_PIN, buttonDown || sensor > 2500);
  Serial.printf("sensor=%d button=%s led=%s\\n",
                sensor,
                buttonDown ? "DOWN" : "UP",
                digitalRead(LED_PIN) ? "ON" : "OFF");
  delay(500);
}
""",
    "json_status": """\
const int LED_PIN = 23;
const int POT_PIN = 34;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int adc = analogRead(POT_PIN);
  bool led = digitalRead(LED_PIN) == HIGH;
  unsigned long uptime = millis() / 1000;

  Serial.print("{\\"device\\":\\"esp32-demo\\",");
  Serial.print("\\"uptime\\":");
  Serial.print(uptime);
  Serial.print(",\\"adc\\":");
  Serial.print(adc);
  Serial.print(",\\"led\\":");
  Serial.print(led ? "true" : "false");
  Serial.println("}");

  delay(1000);
}
""",
    "week3_iot_panel": """\
#include <WiFi.h>
#include <WebServer.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

const char* SSID = "your_wifi_name";
const char* PASSWORD = "your_wifi_password";
const int LED_PIN = 23;
const int SENSOR_PIN = 34;
bool ledOn = false;

WebServer server(80);
Adafruit_SSD1306 display(128, 64, &Wire, -1);

String statusJson() {
  return String("{\\"adc\\":") + analogRead(SENSOR_PIN) +
         String(",\\"led\\":") + (ledOn ? "true" : "false") +
         String(",\\"uptime\\":") + (millis() / 1000) + "}";
}

void drawDisplay() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println("Week3 IoT Panel");
  display.print("IP: ");
  display.println(WiFi.localIP());
  display.print("ADC: ");
  display.println(analogRead(SENSOR_PIN));
  display.print("LED: ");
  display.println(ledOn ? "ON" : "OFF");
  display.display();
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
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
      "<h1>ESP32 IoT Panel</h1>"
      "<p><a href='/on'>LED ON</a> <a href='/off'>LED OFF</a></p>"
      "<p><a href='/status'>JSON Status</a></p>");
  });
  server.on("/status", []() { server.send(200, "application/json", statusJson()); });
  server.on("/on", []() { ledOn = true; digitalWrite(LED_PIN, HIGH); server.sendHeader("Location", "/"); server.send(302); });
  server.on("/off", []() { ledOn = false; digitalWrite(LED_PIN, LOW); server.sendHeader("Location", "/"); server.send(302); });
  server.begin();
}

void loop() {
  server.handleClient();
  static unsigned long lastDisplay = 0;
  if (millis() - lastDisplay >= 300) {
    lastDisplay = millis();
    drawDisplay();
  }
}
""",
    "final_web_console": """\
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
  return String("{\\"sensor\\":") + analogRead(SENSOR_PIN) +
         ",\\"manualLed\\":" + (manualLed ? "true" : "false") +
         ",\\"button\\":" + (digitalRead(BUTTON_PIN) == LOW ? "true" : "false") +
         ",\\"uptime\\":" + (millis() / 1000) + "}";
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
""",
}


WIRING = {
    1: [("板载 LED", "GPIO2", "开发板自带", "部分开发板没有板载 LED，可改接外部 LED 到 GPIO23。")],
    2: [("LED 长脚", "GPIO2 或 GPIO23", "串联 220Ω/330Ω 电阻", "板载 LED 可先用 GPIO2。"), ("LED 短脚", "GND", "共地", "外接 LED 必须限流。")],
    3: [("LED 长脚", "GPIO23", "串联 220Ω/330Ω 电阻", "长脚通常为正极。"), ("LED 短脚", "GND", "共地", "短脚或扁边通常为负极。")],
    4: [("LED1", "GPIO18", "串联电阻到 GND", "第 1 路输出。"), ("LED2", "GPIO19", "串联电阻到 GND", "第 2 路输出。"), ("LED3", "GPIO23", "串联电阻到 GND", "第 3 路输出。")],
    5: [("按键一脚", "GPIO27", "INPUT_PULLUP", "按下接 GND。"), ("按键另一脚", "GND", "共地", "不需要外部上拉。"), ("LED", "GPIO23", "串联电阻到 GND", "显示开关状态。")],
    6: [("按键一脚", "GPIO27", "INPUT_PULLUP", "串口观察状态变化。"), ("按键另一脚", "GND", "共地", "按下为 LOW。"), ("LED", "GPIO23", "串联电阻到 GND", "输出反馈。")],
    7: [("按键", "GPIO27 <-> GND", "INPUT_PULLUP", "切换闪烁模式。"), ("LED", "GPIO23", "串联电阻到 GND", "显示当前模式。")],
    8: [("LED", "GPIO23", "串联电阻到 GND", "PWM/analogWrite 输出亮度。")],
    9: [("电位器左脚", "3V3", "供电", "不要接 5V。"), ("电位器中脚", "GPIO34", "ADC 输入", "读取 0-4095。"), ("电位器右脚", "GND", "共地", "形成分压。"), ("LED", "GPIO23", "串联电阻到 GND", "亮度跟随 ADC。")],
    10: [("模拟传感器 AO", "GPIO34", "ADC 输入", "光敏/声音/电位器模块均可。"), ("数字传感器 DO", "GPIO27", "INPUT_PULLUP", "阈值输出，按模块可能高低相反。"), ("传感器 VCC", "3V3", "供电", "确认模块支持 3.3V。"), ("传感器 GND", "GND", "共地", "必须共地。")],
    11: [("OLED VCC", "3V3", "供电", "多数 SSD1306 模块支持 3.3V。"), ("OLED GND", "GND", "共地", "必须共地。"), ("OLED SDA", "GPIO21", "I2C 数据", "可改但代码要同步。"), ("OLED SCL", "GPIO22", "I2C 时钟", "运行扫描器找地址。")],
    12: [("OLED VCC", "3V3", "供电", "默认地址 0x3C。"), ("OLED GND", "GND", "共地", ""), ("OLED SDA", "GPIO21", "I2C 数据", ""), ("OLED SCL", "GPIO22", "I2C 时钟", ""), ("按键", "GPIO27 <-> GND", "INPUT_PULLUP", "显示按键状态。"), ("电位器中脚", "GPIO34", "ADC", "显示 ADC 数值。")],
    13: [("SPI SCK", "GPIO18", "时钟", "示例只脉冲 CS。"), ("SPI MISO", "GPIO19", "主入从出", "无设备时可空接。"), ("SPI MOSI", "GPIO23", "主出从入", "无设备时可空接。"), ("SPI CS", "GPIO5", "片选", "观察片选脉冲。")],
    14: [("按键", "GPIO27 <-> GND", "INPUT_PULLUP", "按下触发声音。"), ("有源蜂鸣器 +", "GPIO25", "数字输出", "有源蜂鸣器通电即响。"), ("有源蜂鸣器 -", "GND", "共地", "大功率蜂鸣器需驱动模块。")],
    15: [("OLED", "SDA=21, SCL=22, VCC=3V3, GND=GND", "I2C", "显示监测值。"), ("电位器中脚", "GPIO34", "ADC", "模拟传感器。"), ("LED", "GPIO23", "串联电阻到 GND", "阈值告警。")],
    16: [("ESP32", "USB 供电", "无需外接元件", "需要 2.4GHz Wi-Fi SSID 和密码。")],
    17: [("ESP32", "USB 供电", "无需外接元件", "先保证 Day16 Wi-Fi 可连接。")],
    18: [("LED", "GPIO23", "串联电阻到 GND", "手机网页控制。"), ("ESP32", "USB 供电", "Wi-Fi", "手机需在同一局域网。")],
    19: [("电位器中脚", "GPIO34", "ADC", "输出 JSON 中的 adc 字段。"), ("LED", "GPIO23", "串联电阻到 GND", "JSON 中的 led 字段。")],
    20: [("LED", "GPIO23", "串联电阻到 GND", "订阅命令控制。"), ("ESP32", "Wi-Fi", "MQTT", "需要安装 PubSubClient。")],
    21: [("ESP32", "USB 供电", "BLE", "手机安装 nRF Connect 或 LightBlue 扫描。")],
    22: [("电位器中脚", "GPIO34", "ADC", "模拟设备上云数据。"), ("电位器两边", "3V3 / GND", "分压", "串口输出云端 payload。")],
    23: [("LED", "GPIO23", "串联电阻到 GND", "网页控制。"), ("传感器/电位器", "GPIO34", "ADC", "状态接口读取。"), ("ESP32", "Wi-Fi", "Web/API", "手机同网访问。")],
    24: [("LED", "GPIO23", "串联电阻到 GND", "模块化输出。"), ("传感器/电位器", "GPIO34", "ADC", "模块化输入。")],
    25: [("LED", "GPIO23", "串联电阻到 GND", "非阻塞闪烁。"), ("按键", "GPIO27 <-> GND", "INPUT_PULLUP", "并行响应。")],
    26: [("ESP32", "USB 供电", "Deep Sleep", "串口观察醒来日志；部分开发板 USB 串口会断开重连。")],
    27: [("LED", "GPIO23", "串联电阻到 GND", "输出自检。"), ("按键", "GPIO27 <-> GND", "INPUT_PULLUP", "输入自检。"), ("电位器中脚", "GPIO34", "ADC", "模拟输入自检。")],
    28: [("传感器/电位器", "GPIO34", "ADC", "模拟行业采集点。"), ("LED", "GPIO23", "串联电阻到 GND", "告警输出。")],
    29: [("LED", "GPIO23", "串联电阻到 GND", "最终项目输出。"), ("按键", "GPIO27 <-> GND", "INPUT_PULLUP", "最终项目输入。"), ("传感器/电位器", "GPIO34", "ADC", "最终项目采集。")],
    30: [("LED", "GPIO23", "串联电阻到 GND", "网页控制。"), ("按键", "GPIO27 <-> GND", "INPUT_PULLUP", "本地切换 LED。"), ("传感器/电位器", "GPIO34", "ADC", "JSON 状态。"), ("OLED VCC/GND", "3V3/GND", "供电", "本地显示。"), ("OLED SDA/SCL", "GPIO21/GPIO22", "I2C", "显示 IP、ADC、LED、按键。"), ("ESP32", "Wi-Fi", "WebServer", "手机同网访问 IP。")],
}


LIBRARIES = {
    "oled_dashboard": ["Adafruit GFX Library", "Adafruit SSD1306"],
    "week2_monitor": ["Adafruit GFX Library", "Adafruit SSD1306"],
    "mqtt_led": ["PubSubClient"],
    "ble_basic": ["ESP32 BLE Arduino / Arduino-ESP32 built-in BLE headers"],
    "week3_iot_panel": ["Adafruit GFX Library", "Adafruit SSD1306"],
    "final_web_console": ["Adafruit GFX Library", "Adafruit SSD1306"],
}


def code_for(day, index):
    key = SLUGS[index - 1]
    if key in OVERRIDE_SNIPPETS:
        return OVERRIDE_SNIPPETS[key]
    code_key = day.get("code")
    if code_key in OVERRIDE_SNIPPETS:
        return OVERRIDE_SNIPPETS[code_key]
    if code_key:
        return CODE_SNIPPETS[code_key]
    return OVERRIDE_SNIPPETS[key]


def project_dir_name(index):
    return f"day{index:02d}_{SLUGS[index - 1]}"


def make_wiring(index):
    rows = WIRING[index]
    lines = [
        f"# Day {index:02d} 接线文档",
        "",
        "## 元器件实物示意",
        "",
        "![元器件实物示意](assets/components.svg)",
        "",
        "## 连接接线图",
        "",
        "![连接接线图](assets/wiring.svg)",
        "",
        "## 接线表",
        "",
        "| 模块/引脚 | 连接到 ESP32 | 类型 | 说明 |",
        "|---|---|---|---|",
    ]
    lines += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows]
    lines += [
        "",
        "## 安全检查",
        "",
        "- 改线前先拔掉 USB 或断开外部电源。",
        "- ESP32 GPIO 通常是 3.3V 逻辑，不要把 5V 信号直接送入 GPIO。",
        "- 每个 LED 必须串联 220Ω 或 330Ω 限流电阻。",
        "- 所有模块必须和 ESP32 共地。",
        "- 如果现象异常，先退回只接一个模块的最小电路。",
    ]
    return "\n".join(lines) + "\n"


def component_label(part):
    if "ESP32" in part:
        return "ESP32"
    if "OLED" in part:
        return "OLED"
    if "LED" in part:
        return "LED"
    if "按键" in part or "开关" in part:
        return "BUTTON"
    if "电阻" in part:
        return "RESISTOR"
    if "电位器" in part:
        return "POT"
    if "蜂鸣器" in part:
        return "BUZZER"
    if "继电器" in part:
        return "RELAY"
    if "传感器" in part or "DHT" in part or "光敏" in part or "超声波" in part:
        return "SENSOR"
    if "面包板" in part:
        return "BREADBOARD"
    if "杜邦线" in part:
        return "WIRE"
    if "USB" in part:
        return "USB"
    return "MODULE"


def make_components_svg(index, day):
    parts = day["parts"][:8]
    width = 980
    card_w = 220
    card_h = 126
    gap = 22
    rows = (len(parts) + 3) // 4
    height = 112 + rows * (card_h + gap)
    cards = []
    for i, part in enumerate(parts):
        x = 34 + (i % 4) * (card_w + gap)
        y = 80 + (i // 4) * (card_h + gap)
        label = component_label(part)
        cards.append(f"""
  <g>
    <rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="14" fill="#fffaf0" stroke="#d9d0bd"/>
    <rect x="{x + 18}" y="{y + 20}" width="62" height="48" rx="8" fill="#10241f"/>
    <circle cx="{x + 36}" cy="{y + 44}" r="5" fill="#38d9a9"/>
    <circle cx="{x + 62}" cy="{y + 44}" r="5" fill="#d99b4c"/>
    <text x="{x + 96}" y="{y + 42}" font-size="20" font-weight="800" fill="#18231f">{escape(label)}</text>
    <text x="{x + 18}" y="{y + 96}" font-size="16" fill="#4f5c56">{escape(part)}</text>
  </g>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="#f6f3ea"/>
  <text x="34" y="44" font-size="26" font-weight="800" fill="#10241f">Day {index:02d} 元器件实物示意</text>
  <text x="34" y="68" font-size="15" fill="#66736d">示意图用于识别模块外观和作用，实际模块丝印可能略有不同。</text>
  {''.join(cards)}
</svg>
"""


def wire_color(target):
    if "GND" in target:
        return "#333333"
    if "3V3" in target or "VCC" in target or "供电" in target:
        return "#c54b3f"
    if "GPIO21" in target or "SDA" in target:
        return "#2f6f9f"
    if "GPIO22" in target or "SCL" in target:
        return "#38a169"
    if "Wi-Fi" in target or "BLE" in target:
        return "#8b5cf6"
    return "#d99b4c"


def make_wiring_svg(index):
    rows = WIRING[index]
    width = 1120
    row_h = 58
    height = max(420, 140 + len(rows) * row_h)
    board_x, board_y, board_w, board_h = 56, 102, 260, max(250, len(rows) * row_h - 12)
    module_x = 720
    svg_rows = []
    for i, (module, target, kind, note) in enumerate(rows):
        y = 126 + i * row_h
        color = wire_color(target)
        svg_rows.append(f"""
  <path d="M {board_x + board_w} {y} C 450 {y}, 520 {y}, {module_x - 24} {y}" fill="none" stroke="{color}" stroke-width="4"/>
  <circle cx="{board_x + board_w}" cy="{y}" r="6" fill="{color}"/>
  <rect x="{module_x}" y="{y - 22}" width="330" height="44" rx="9" fill="#fffaf0" stroke="#d9d0bd"/>
  <text x="{module_x + 16}" y="{y - 3}" font-size="16" font-weight="800" fill="#18231f">{escape(module)}</text>
  <text x="{module_x + 16}" y="{y + 16}" font-size="13" fill="#66736d">{escape(kind)} · {escape(note[:34])}</text>
  <text x="{board_x + 24}" y="{y + 5}" font-size="15" font-weight="800" fill="#fffaf0">{escape(target)}</text>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="#f6f3ea"/>
  <text x="56" y="48" font-size="28" font-weight="800" fill="#10241f">Day {index:02d} 连接接线图</text>
  <text x="56" y="74" font-size="15" fill="#66736d">先断电接线；红色通常表示 3V3/VCC，黑色表示 GND，其他颜色表示信号线。</text>
  <rect x="{board_x}" y="{board_y}" width="{board_w}" height="{board_h}" rx="20" fill="#10241f" stroke="#d99b4c" stroke-width="3"/>
  <text x="{board_x + 66}" y="{board_y + 48}" font-size="30" font-weight="900" fill="#fffaf0">ESP32</text>
  <text x="{board_x + 40}" y="{board_y + 82}" font-size="14" fill="#cbd5d1">开发板引脚侧</text>
  <rect x="680" y="90" width="410" height="{max(280, len(rows) * row_h + 20)}" rx="18" fill="#ffffff" stroke="#d9d0bd"/>
  <text x="720" y="122" font-size="22" font-weight="800" fill="#10241f">外接模块 / 元器件</text>
  {''.join(svg_rows)}
</svg>
"""


def make_readme(index, day, ino_name):
    code_key = day.get("code") or SLUGS[index - 1]
    libs = LIBRARIES.get(code_key, [])
    library_text = "\n".join(f"- {lib}" for lib in libs) if libs else "- 无额外库，使用 Arduino-ESP32 自带库。"
    return "\n".join([
        f"# Day {index:02d}: {day['title']}",
        "",
        "## 今日目标",
        "",
        day["goal"],
        "",
        "## 可烧录代码",
        "",
        f"- Arduino 工程文件：`{ino_name}`",
        f"- 打开方式：用 Arduino IDE 打开本目录下的 `{ino_name}`，选择 ESP32 开发板和串口后上传。",
        "- 如果文件夹名和 `.ino` 文件名保持一致，Arduino IDE 可以直接识别为一个工程。",
        "",
        "## 依赖库",
        "",
        library_text,
        "",
        "## 烧录前检查",
        "",
        "1. Arduino IDE 已安装 `esp32 by Espressif Systems` 板卡包。",
        "2. 开发板选择常见 `ESP32 Dev Module`，或选择你手头开发板对应型号。",
        "3. 串口监视器波特率使用 `115200`。",
        "4. 涉及 Wi-Fi 的项目，先在 `.ino` 里修改 `SSID` 和 `PASSWORD`。",
        "5. 涉及 OLED 的项目，如果屏幕无显示，先运行 Day 11 的 I2C Scanner 确认地址。",
        "",
        "## 对应接线",
        "",
        "见 [`wiring.md`](wiring.md)。",
        "",
        "## 建议实验",
        "",
        day["project"],
        "",
    ])


def generate():
    OUT.mkdir(exist_ok=True)
    index_lines = [
        "# ESP32 30 天可烧录 Arduino 工程",
        "",
        "每个目录都是一个独立 Arduino 工程，目录名和 `.ino` 文件名保持一致，可直接用 Arduino IDE 打开、编译、上传。",
        "",
        "## 使用前准备",
        "",
        "1. 安装 Arduino IDE。",
        "2. 在 Boards Manager 安装 `esp32 by Espressif Systems`。",
        "3. 按每天目录里的 `wiring.md` 接线。",
        "4. 打开对应 `.ino`，选择开发板和串口后上传。",
        "5. 串口监视器默认 `115200`。",
        "",
        "## 每日工程索引",
        "",
        "| 天数 | 工程目录 | 目标 |",
        "|---|---|---|",
    ]
    for index, day in enumerate(DAYS, start=1):
        folder_name = project_dir_name(index)
        folder = OUT / folder_name
        folder.mkdir(parents=True, exist_ok=True)
        assets = folder / "assets"
        assets.mkdir(exist_ok=True)
        ino_name = f"{folder_name}.ino"
        (folder / ino_name).write_text(code_for(day, index).strip() + "\n", encoding="utf-8")
        (folder / "README.md").write_text(make_readme(index, day, ino_name), encoding="utf-8")
        (folder / "wiring.md").write_text(make_wiring(index), encoding="utf-8")
        (assets / "components.svg").write_text(make_components_svg(index, day), encoding="utf-8")
        (assets / "wiring.svg").write_text(make_wiring_svg(index), encoding="utf-8")
        index_lines.append(f"| Day {index:02d} | [{folder_name}]({folder_name}/) | {day['goal']} |")
    (OUT / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    generate()
