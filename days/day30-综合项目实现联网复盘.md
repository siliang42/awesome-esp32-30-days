# Day 30：综合项目收官：本地闭环、Web 控制与进阶复盘

## 今日目标

完成最终项目的硬件输入、输出、本地显示、Web 控制、状态接口和学习复盘。

## 今天你会真正理解什么

最终项目变成一个真正可交互的联网设备。收官不是结束，而是把 30 天沉淀成作品、方法和下一条进阶路线。

## 元件认知

- `ESP32`：本阶段使用的模块或材料，重点关注供电、接口、电平和接线方向。
- `OLED`：本阶段使用的模块或材料，重点关注供电、接口、电平和接线方向。
- `LED`：最基础输出元件，用来观察 GPIO 高低电平和程序状态。
- `按键`：最基础输入元件，把人的动作转换为 GPIO 电平变化。
- `电位器或传感器`：本阶段使用的模块或材料，重点关注供电、接口、电平和接线方向。
- `所有项目`：30 天内完成的代码、接线图、照片和笔记，是作品集基础。
- `笔记`：记录踩坑、参数、接线和复盘，形成自己的硬件知识库。
- `代码`：整理成可复用 demo，后续做项目时直接调用。
- `照片`：拍下接线和运行效果，方便复盘、展示和排查。

## 核心概念

- **接线实现**：根据设计文档把每个模块连接到指定引脚。
- **分模块调试**：一个模块一个模块确认，最后再组合。
- **本地闭环**：输入、处理、输出都在设备本地完成。
- **HTTP API**：用 URL 返回机器可读的数据或执行控制命令。
- **网页控制**：浏览器通过按钮或链接发送控制请求。
- **状态同步**：本地状态、网页状态、实际硬件输出保持一致。
- **验收测试**：按清单逐项验证功能是否达到要求。
- **作品集**：整理能展示学习成果的代码、照片、文档和视频。
- **技术路线**：后续继续学习的方向和顺序。
- **ESP-IDF**：Espressif 官方开发框架，比 Arduino 更底层、更工程化。
- **FreeRTOS**：ESP32 常用实时操作系统，支持多任务调度。
- **PCB**：把面包板电路变成可生产的电路板。
- **OTA**：无线升级固件。

## 实操项目

**项目名称：** 完成桌面物联网控制台：本地显示传感器值，手机网页查看状态并控制 LED，最后整理作品集和下一阶段计划。

### 推荐流程

1. **复述目标**：用一句话写下今天要让 ESP32 完成什么动作。
2. **画接线草图**：先在纸上画 ESP32、面包板、电源正负、信号线，再动手插线。
3. **只接最小电路**：先只接一个输入或输出，确认能工作后再加第二个模块。
4. **上传最小 Demo**：不要一开始就追求完美，先让一个小动作跑起来。
5. **打开串口监视器**：观察日志、变量、IP、传感器值或错误信息。
6. **记录现象**：记录成功现象、异常现象、最终接线和修改过的引脚。
7. **做一次变化实验**：改变延时、阈值、显示文字、引脚或网页内容，确认你真的理解了。

### 建议接线习惯

- ESP32 的大多数 GPIO 是 **3.3V 电平**，不要把 5V 信号直接送进 GPIO。
- LED 必须串联限流电阻，常用 220Ω 或 330Ω。
- 按键输入优先使用 `INPUT_PULLUP`，接线简单，稳定性更好。
- 面包板电源轨可能中间断开，接线前用万用表或观察连通标识确认。
- 每次插拔模块前先断电，尤其是 OLED、传感器、电源模块。


## 参考 Demo

> 引脚可按你的开发板调整。ESP32 常用安全输出脚可优先选择 GPIO 18、19、21、22、23、25、26、27；ADC 输入可优先选择 GPIO 34、35、36、39。

```cpp
#include <WiFi.h>
#include <WebServer.h>

const char* SSID = "your_wifi_name";
const char* PASSWORD = "your_wifi_password";
const int LED_PIN = 23;
const int SENSOR_PIN = 34;
bool manualLed = false;
WebServer server(80);

String jsonStatus() {
  return String("{\"sensor\":") + analogRead(SENSOR_PIN) +
 ",\"manualLed\":" + (manualLed ? "true" : "false") +
 ",\"uptime\":" + (millis() / 1000) + "}";
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  Serial.println(WiFi.localIP());
  server.on("/", []() {
    server.send(200, "text/html", "<h1>ESP32 Console</h1><a href='/toggle'>Toggle LED</a><p><a href='/api/status'>JSON Status</a></p>");
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
}
```


## 分步操作

1. **准备环境**：打开 Arduino IDE 或 VS Code + PlatformIO，选择正确开发板和串口。
2. **确认引脚**：检查代码中的引脚号是否与你的接线一致。
3. **编译上传**：先编译，再按需按住 BOOT 键上传。
4. **观察输出**：LED、OLED、蜂鸣器、串口或网页必须至少有一个可观察反馈。
5. **修改一个参数**：例如延时、阈值、亮度、显示文字或 MQTT Topic。
6. **重新上传验证**：确认修改确实改变了设备行为。
7. **写学习记录**：记录今天的接线、代码变化、踩坑和一个仍不懂的问题。

## 常见问题与排查

- **无法上传**：确认数据线支持数据传输；选择正确串口；必要时按住 BOOT；关闭占用串口监视器的软件。
- **LED 不亮**：检查 LED 正负极、限流电阻、GND 是否共地、引脚号是否写错。
- **按键乱跳**：使用 `INPUT_PULLUP`，增加 30-80ms 防抖，缩短过长杜邦线。
- **OLED 无显示**：确认 VCC/GND/SDA/SCL，运行 I2C Scanner，常见地址是 `0x3C` 或 `0x3D`。
- **Wi-Fi 连不上**：确认 2.4GHz 网络、SSID/密码、信号强度，避免中文或特殊字符先干扰排查。
- **代码能编译但现象不对**：把系统拆回最小模块，先验证单个 LED、单个按键、单个 OLED。

## 今日复盘

- 今天哪个概念最像“突然亮了”的灯泡？
- 哪个现象和你预期不一样？你是怎么定位的？
- 如果把今天内容用在真实产品里，它可能属于输入、输出、显示、通信还是控制？
- 明天继续前，你最想查清楚的一个问题是什么？

## 拓展阅读

- [ESP32 Arduino Core](https://docs.espressif.com/projects/arduino-esp32/en/latest/)
- [Random Nerd Tutorials ESP32](https://randomnerdtutorials.com/projects-esp32/)
- [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [ESP32 Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf)
- [PlatformIO ESP32](https://docs.platformio.org/en/latest/platforms/espressif32.html)
