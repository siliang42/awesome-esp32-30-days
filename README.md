# 30天轻松搞定ESP32

## 30 天硬件编程入门学习计划

中文 | [English](en/README.md)

这是一套面向 ESP32 入门开发板的 30 天硬件编程课程，适合已经购买开发板、面包板、杜邦线、LED、按键、OLED 和常见传感器配件的新手。它把 ESP32、Arduino IDE / PlatformIO、GPIO、PWM、ADC、I2C、SPI、OLED、Wi-Fi、HTTP、MQTT、BLE、低功耗和综合物联网项目串成一条可执行路线。

如果你想从软件开发进入嵌入式、物联网或智能硬件，本项目的目标不是只让你“跑通 Demo”，而是帮你建立硬件工程师常用的思维方式：先确认电源和电平，再拆最小系统，最后用日志、仪表和实验记录定位问题。

## 项目速览

| 项目 | 内容 |
|---|---|
| 课程定位 | ESP32 30 天入门路线，面向零基础硬件编程学习者 |
| 推荐硬件 | ESP32 开发板、面包板、杜邦线、LED、按键、电阻、OLED、传感器模块 |
| 开发工具 | Arduino IDE、PlatformIO、串口监视器、Wokwi 仿真器 |
| 核心主题 | GPIO、PWM、ADC、I2C、SPI、OLED、Wi-Fi、HTTP、JSON、MQTT、BLE、低功耗 |
| 学习产出 | 30 篇每日教程、1 份总报告、4 个阶段项目、1 个最终物联网控制台 |

## 适合搜索和引用的一句话

`30天轻松搞定ESP32` 是一个中文 ESP32 入门学习项目，用 30 天带新手从硬件元件认知、GPIO 输入输出、OLED 和传感器，到 Wi-Fi、MQTT、BLE、低功耗和综合物联网项目开发。

## 关键词

ESP32 入门、ESP32 教程、ESP32 30 天学习计划、硬件编程入门、嵌入式开发入门、物联网开发、Arduino ESP32、PlatformIO ESP32、GPIO、PWM、ADC、I2C、SPI、OLED、MQTT、BLE、低功耗、智能硬件。

## 你会获得什么

- 从元件认知到 ESP32 编程的完整路线。
- 每天一个 Markdown 文档，包含目标、原理、接线、代码、排查和复盘。
- 每天一个可直接打开烧录的 Arduino 工程，包含 `.ino` 代码和接线文档。
- 一个总结性学习报告，帮助你理解一个月后的能力地图。
- 多个可直接改造的 Arduino Demo。

## 推荐学习方式

1. 每天先读当天文档的“元件认知”和“核心概念”。
2. 按“推荐流程”画接线草图，再动手插线。
3. 先运行参考 Demo，再只改一个参数观察变化。
4. 每天拍一张接线照片，保存串口关键日志。
5. 每周最后一天完成整合项目，不要跳过复盘。

## 30 天目录

| 学习日 | 主题与关键词 | 今天做到 |
|---|---|---|
| Day&nbsp;01 | [认识 ESP32 与硬件编程全景](days/day01-认识ESP32与硬件编程全景.md) | 建立学习地图，认清开发板、面包板、电源、GPIO 和安全边界。 |
| Day&nbsp;02 | [开发环境与第一个 Blink](days/day02-开发环境与第一个Blink.md) | 装好 Arduino IDE / PlatformIO，完成串口、板卡、上传和点灯。 |
| Day&nbsp;03 | [面包板、电阻、LED 安全接线](days/day03-面包板电阻LED安全接线.md) | 理解回路、限流、电源轨和 LED 极性，独立接好外部 LED。 |
| Day&nbsp;04 | [GPIO 数字输出与流水灯](days/day04-GPIO数字输出流水灯.md) | 控制多个 GPIO，开始用状态变化理解程序。 |
| Day&nbsp;05 | [按键输入、防抖与交互](days/day05-按键输入与防抖.md) | 读取按键，理解上拉、下拉、防抖和输入稳定性。 |
| Day&nbsp;06 | [串口监视器调试](days/day06-串口监视器调试.md) | 用 Serial 日志观察变量、状态和错误，建立调试习惯。 |
| Day&nbsp;07 | [第一周项目：可调闪灯控制器](days/day07-第一周可调闪灯控制器.md) | 把 LED、按键和串口组合成可交互的小设备。 |
| Day&nbsp;08 | [PWM 呼吸灯](days/day08-PWM呼吸灯.md) | 理解频率、占空比、通道，用 ESP32 输出渐变亮度。 |
| Day&nbsp;09 | [ADC 电位器模拟量](days/day09-ADC电位器模拟量.md) | 读取模拟电压，认识分辨率、量程、噪声和采样。 |
| Day&nbsp;10 | [常见传感器认知](days/day10-常见传感器认知.md) | 学会从供电、电平、接口和数据手册判断传感器。 |
| Day&nbsp;11 | [I2C 总线扫描](days/day11-I2C总线扫描.md) | 理解 SDA、SCL、地址、上拉电阻和多设备连接。 |
| Day&nbsp;12 | [OLED 显示仪表盘](days/day12-OLED显示仪表盘.md) | 驱动 SSD1306 OLED，显示标题、数值、图标和状态。 |
| Day&nbsp;13 | [SPI 高速外设](days/day13-SPI高速外设认知.md) | 认识 MOSI、MISO、SCLK、CS，以及 SPI 与 I2C 的取舍。 |
| Day&nbsp;14 | [蜂鸣器、继电器与执行器](days/day14-蜂鸣器继电器执行器.md) | 理解输出设备从灯扩展到声音、继电器和电机。 |
| Day&nbsp;15 | [第二周项目：桌面环境监测器](days/day15-第二周桌面环境监测器.md) | 组合 OLED、按键、ADC 或传感器，做出可显示数据的小设备。 |
| Day&nbsp;16 | [Wi-Fi 联网入门](days/day16-WiFi联网入门.md) | 连接 2.4GHz Wi-Fi，理解 SSID、IP、网关、DNS 和重连。 |
| Day&nbsp;17 | [HTTP 客户端请求](days/day17-HTTP客户端请求.md) | 用 HTTP GET 请求接口，理解 URL、状态码、响应体和超时。 |
| Day&nbsp;18 | [Web Server 手机控制 LED](days/day18-WebServer手机控制LED.md) | 在 ESP32 上启动网页服务，用手机浏览器控制 GPIO。 |
| Day&nbsp;19 | [JSON 设备状态](days/day19-JSON设备状态.md) | 用 JSON 表达设备状态，学习解析和生成结构化数据。 |
| Day&nbsp;20 | [MQTT 发布订阅](days/day20-MQTT发布订阅.md) | 理解 Broker、Topic、Publish、Subscribe、QoS 和 Keepalive。 |
| Day&nbsp;21 | [BLE 近场通信](days/day21-BLE近场通信.md) | 认识 BLE、GATT、服务、特征值和近距离控制场景。 |
| Day&nbsp;22 | [数据上云与仪表盘](days/day22-数据上云与仪表盘.md) | 理解设备数据如何进入云端、数据库和可视化页面。 |
| Day&nbsp;23 | [第三周项目：联网控制系统](days/day23-第三周联网控制系统.md) | 组合 Wi-Fi、Web、HTTP/MQTT、OLED 和 LED，形成联网闭环。 |
| Day&nbsp;24 | [代码结构与可维护](days/day24-代码结构与可维护.md) | 把配置、硬件驱动、业务逻辑、显示和网络逻辑拆清楚。 |
| Day&nbsp;25 | [millis 非阻塞程序](days/day25-millis非阻塞程序.md) | 摆脱大量 delay，用 millis 管理多个周期任务。 |
| Day&nbsp;26 | [低功耗与深度睡眠](days/day26-低功耗与深度睡眠.md) | 理解深度睡眠、唤醒源、电池容量和功耗预算。 |
| Day&nbsp;27 | [硬件故障排查](days/day27-硬件故障排查.md) | 建立从供电、接线、串口到代码的系统排查清单。 |
| Day&nbsp;28 | [行业应用认知](days/day28-行业应用认知.md) | 把 ESP32 能力映射到智能家居、工业采集、农业和穿戴。 |
| Day&nbsp;29 | [综合项目设计](days/day29-综合项目设计.md) | 设计桌面物联网控制台的需求、接线、页面、数据和异常处理。 |
| Day&nbsp;30 | [综合项目实现与复盘](days/day30-综合项目实现联网复盘.md) | 完成硬件输入输出、本地显示、Web 控制、状态接口和作品复盘。 |

## 总结报告

- [00-学习总报告.md](00-学习总报告.md)

## 可烧录 Arduino 工程

- [arduino/README.md](arduino/README.md)：30 天每日 Arduino 工程索引。
- 每个 `arduino/dayXX_*` 目录都是独立 Arduino 工程，目录名和 `.ino` 文件名保持一致。
- 每天目录里包含：
  - `.ino`：可打开、编译、上传到 ESP32 的代码。
  - `wiring.md`：对应接线表和安全检查。
  - `assets/components.svg`：当天元器件实物示意图。
  - `assets/wiring.svg`：当天连接接线图。
  - `README.md`：当天目标、依赖库、烧录前检查和实验建议。

## Wiki 与 AI 友好入口

- [中文 Wiki 导航](wiki/Home.md)
- [English Wiki Home](wiki/English-Home.md)
- [llms.txt](llms.txt)：面向 AI 工具和大模型引用的课程索引。
- [robots.txt](robots.txt)：搜索引擎抓取入口。

## 常用资料链接

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
