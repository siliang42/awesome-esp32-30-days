# 30天轻松搞定ESP32

## 30 天硬件编程入门学习计划

中文 | [English](en/README.md)

这是一套面向 ESP32 入门开发板的 30 天学习资料包，适合已经购买开发板、面包板、杜邦线、LED、按键、OLED 和常见传感器配件的新手。

## 你会获得什么

- 从元件认知到 ESP32 编程的完整路线。
- 每天一个 Markdown 文档，包含目标、原理、接线、代码、排查和复盘。
- 一个总结性学习报告，帮助你理解一个月后的能力地图。
- 多个可直接改造的 Arduino Demo。

## 推荐学习方式

1. 每天先读当天文档的“元件认知”和“核心概念”。
2. 按“推荐流程”画接线草图，再动手插线。
3. 先运行参考 Demo，再只改一个参数观察变化。
4. 每天拍一张接线照片，保存串口关键日志。
5. 每周最后一天完成整合项目，不要跳过复盘。

## 30 天目录

| 天数 | 主题 | 今日目标 |
|---|---|---|
| Day 01 | [认识 ESP32、开发板与硬件编程全景](days/day01-认识ESP32与硬件编程全景.md) | 建立 ESP32 学习地图，认识开发板、面包板、杜邦线、电源、GPIO 和基础安全边界。 |
| Day 02 | [搭建 Arduino IDE / PlatformIO 与第一个 Blink](days/day02-开发环境与第一个Blink.md) | 完成开发环境、板卡包、串口驱动、上传流程，并点亮板载 LED 或外接 LED。 |
| Day 03 | [面包板、电阻、LED 与安全接线](days/day03-面包板电阻LED安全接线.md) | 理解电路回路、限流电阻、LED 极性，独立完成外接 LED 控制。 |
| Day 04 | [GPIO 数字输出：流水灯与状态机思维](days/day04-GPIO数字输出流水灯.md) | 使用多个 GPIO 控制多个 LED，理解非阻塞思维的第一步。 |
| Day 05 | [按键输入、防抖与人机交互](days/day05-按键输入与防抖.md) | 读取按键状态，理解上拉/下拉、防抖和输入不稳定的原因。 |
| Day 06 | [串口监视器：让 ESP32 学会说话](days/day06-串口监视器调试.md) | 掌握 Serial 输出、调试日志、变量观察和基础故障定位。 |
| Day 07 | [第一周整合项目：可调节闪灯控制器](days/day07-第一周可调闪灯控制器.md) | 把 LED、按键、串口整合成一个可交互小项目。 |
| Day 08 | [PWM：让 LED 呼吸起来](days/day08-PWM呼吸灯.md) | 理解 PWM 的占空比、频率、通道，用 ESP32 输出渐变亮度。 |
| Day 09 | [ADC：读取电位器与模拟量](days/day09-ADC电位器模拟量.md) | 读取电位器电压，理解 ADC 分辨率、量程、噪声和采样。 |
| Day 10 | [常见传感器认知：温湿度、光敏、声音、距离](days/day10-常见传感器认知.md) | 理解传感器的输入类型、供电、电平、数据手册和选型方法。 |
| Day 11 | [I2C 总线：认识两根线连接多个设备](days/day11-I2C总线扫描.md) | 理解 SDA、SCL、地址、上拉电阻和 I2C 扫描器。 |
| Day 12 | [OLED 屏：显示文字、数值与图标](days/day12-OLED显示仪表盘.md) | 驱动 SSD1306 OLED，显示项目标题、传感器数值和状态。 |
| Day 13 | [SPI 与高速外设认知](days/day13-SPI高速外设认知.md) | 理解 SPI 的 MOSI、MISO、SCLK、CS，以及它和 I2C 的区别。 |
| Day 14 | [蜂鸣器、继电器与执行器基础](days/day14-蜂鸣器继电器执行器.md) | 理解输出不只是灯，还可以是声音、继电器、电机等执行器。 |
| Day 15 | [第二周整合项目：桌面环境监测器](days/day15-第二周桌面环境监测器.md) | 组合 OLED、按键、ADC 或传感器，做一个可显示数据的小设备。 |
| Day 16 | [Wi-Fi 入门：连接路由器与理解网络参数](days/day16-WiFi联网入门.md) | 让 ESP32 连接 Wi-Fi，理解 SSID、密码、IP、网关和连接状态。 |
| Day 17 | [HTTP 客户端：让 ESP32 请求网络数据](days/day17-HTTP客户端请求.md) | 使用 HTTP GET 请求接口，理解 URL、状态码、响应体和超时。 |
| Day 18 | [Web Server：手机浏览器控制 LED](days/day18-WebServer手机控制LED.md) | 在 ESP32 上启动网页服务器，用手机访问并控制 LED。 |
| Day 19 | [JSON 与数据结构：从字符串到设备状态](days/day19-JSON设备状态.md) | 理解 JSON 表示设备状态，学习解析和生成简单 JSON。 |
| Day 20 | [MQTT 入门：发布与订阅](days/day20-MQTT发布订阅.md) | 理解 MQTT Broker、Topic、Publish、Subscribe，用 ESP32 上报状态。 |
| Day 21 | [蓝牙 BLE 认知：近场设备通信](days/day21-BLE近场通信.md) | 理解经典蓝牙与 BLE 的区别，认识服务、特征值和近距离控制场景。 |
| Day 22 | [数据上云与仪表盘思维](days/day22-数据上云与仪表盘.md) | 理解设备数据如何进入云端、数据库和仪表盘。 |
| Day 23 | [第三周整合项目：手机控制 + 数据上报小系统](days/day23-第三周联网控制系统.md) | 把 Wi-Fi、Web、MQTT/HTTP、OLED 和 LED 组合成联网小系统。 |
| Day 24 | [代码结构：从能跑到可维护](days/day24-代码结构与可维护.md) | 学习把项目拆成配置、硬件驱动、业务逻辑、网络逻辑。 |
| Day 25 | [定时器、millis 与非阻塞程序](days/day25-millis非阻塞程序.md) | 摆脱大量 delay，使用 millis 管理多个周期任务。 |
| Day 26 | [低功耗与电池供电认知](days/day26-低功耗与深度睡眠.md) | 理解深度睡眠、唤醒源、电池供电、功耗预算和应用场景。 |
| Day 27 | [故障排查：从烧录失败到接线错误](days/day27-硬件故障排查.md) | 建立硬件调试清单，系统定位常见问题。 |
| Day 28 | [行业应用：智能家居、工业采集、农业、穿戴](days/day28-行业应用认知.md) | 理解 ESP32 能力如何映射到真实行业场景。 |
| Day 29 | [综合项目设计：桌面物联网控制台](days/day29-综合项目设计.md) | 设计最终项目，包括需求、接线、页面、数据、异常处理。 |
| Day 30 | [综合项目收官：本地闭环、Web 控制与进阶复盘](days/day30-综合项目实现联网复盘.md) | 完成最终项目的硬件输入、输出、本地显示、Web 控制、状态接口和学习复盘。 |

## 总结报告

- [00-学习总报告.md](00-学习总报告.md)

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
