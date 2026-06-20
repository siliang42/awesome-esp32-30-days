## ESP32 30 天硬件编程入门 Wiki

中文 | [English](English-Home)

欢迎来到 `awesome-esp32-30-days` Wiki。这里是项目的中文导航页，适合第一次接触 ESP32、嵌入式开发、物联网原型和智能硬件的新手快速找到学习入口。完整课程内容以仓库中的 Markdown 文档为准。

## 这个项目解决什么问题

很多 ESP32 新手不是卡在“代码怎么写”，而是卡在更基础的工程判断：

- 这根线到底该接 3.3V、5V 还是 GND？
- GPIO、PWM、ADC、I2C、SPI 分别适合什么场景？
- 为什么 Demo 能编译，硬件却没有反应？
- Wi-Fi、HTTP、MQTT、BLE 这些通信方式应该怎么选？
- 怎样把一个点灯实验升级成一个真正的物联网小系统？

本项目用 30 天把这些问题拆成每天可完成的小任务，让你从元件认知、最小电路、串口调试，一直走到联网控制、数据上报、低功耗和综合项目。

## 快速入口

- [中文 README](https://github.com/siliang42/awesome-esp32-30-days/blob/main/README.md)
- [中文学习总报告](https://github.com/siliang42/awesome-esp32-30-days/blob/main/00-%E5%AD%A6%E4%B9%A0%E6%80%BB%E6%8A%A5%E5%91%8A.md)
- [30 天每日文档](https://github.com/siliang42/awesome-esp32-30-days/tree/main/days)
- [English README](https://github.com/siliang42/awesome-esp32-30-days/blob/main/en/README.md)
- [AI 工具索引 llms.txt](https://github.com/siliang42/awesome-esp32-30-days/blob/main/llms.txt)

## 30 天课程导航

| 天数 | 主题 | 核心能力 |
|---|---|---|
| Day 01 | [认识 ESP32 与硬件编程全景](https://github.com/siliang42/awesome-esp32-30-days/blob/main/days/day01-%E8%AE%A4%E8%AF%86ESP32%E4%B8%8E%E7%A1%AC%E4%BB%B6%E7%BC%96%E7%A8%8B%E5%85%A8%E6%99%AF.md) | 建立学习地图，理解开发板、GPIO、电源和安全边界 |
| Day 02 | [开发环境与第一个 Blink](https://github.com/siliang42/awesome-esp32-30-days/blob/main/days/day02-%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E4%B8%8E%E7%AC%AC%E4%B8%80%E4%B8%AABlink.md) | 安装工具链，完成板卡、串口、编译和上传 |
| Day 03 | [面包板、电阻、LED 安全接线](https://github.com/siliang42/awesome-esp32-30-days/blob/main/days/day03-%E9%9D%A2%E5%8C%85%E6%9D%BF%E7%94%B5%E9%98%BBLED%E5%AE%89%E5%85%A8%E6%8E%A5%E7%BA%BF.md) | 理解回路、限流、电源轨和 LED 极性 |
| Day 04 | [GPIO 数字输出与流水灯](https://github.com/siliang42/awesome-esp32-30-days/blob/main/days/day04-GPIO%E6%95%B0%E5%AD%97%E8%BE%93%E5%87%BA%E6%B5%81%E6%B0%B4%E7%81%AF.md) | 控制多个 GPIO，形成状态变化思维 |
| Day 05 | [按键输入与防抖](https://github.com/siliang42/awesome-esp32-30-days/blob/main/days/day05-%E6%8C%89%E9%94%AE%E8%BE%93%E5%85%A5%E4%B8%8E%E9%98%B2%E6%8A%96.md) | 读取输入，理解上拉、下拉和防抖 |
| Day 06 | [串口监视器调试](https://github.com/siliang42/awesome-esp32-30-days/blob/main/days/day06-%E4%B8%B2%E5%8F%A3%E7%9B%91%E8%A7%86%E5%99%A8%E8%B0%83%E8%AF%95.md) | 用日志观察变量、状态和错误 |
| Day 07 | [第一周项目：可调闪灯控制器](https://github.com/siliang42/awesome-esp32-30-days/blob/main/days/day07-%E7%AC%AC%E4%B8%80%E5%91%A8%E5%8F%AF%E8%B0%83%E9%97%AA%E7%81%AF%E6%8E%A7%E5%88%B6%E5%99%A8.md) | 整合 LED、按键和串口 |
| Day 08-15 | [外设、总线与桌面环境监测器](https://github.com/siliang42/awesome-esp32-30-days/tree/main/days) | PWM、ADC、传感器、I2C、OLED、SPI、执行器 |
| Day 16-23 | [联网通信与手机控制系统](https://github.com/siliang42/awesome-esp32-30-days/tree/main/days) | Wi-Fi、HTTP、Web Server、JSON、MQTT、BLE |
| Day 24-30 | [工程化与最终物联网控制台](https://github.com/siliang42/awesome-esp32-30-days/tree/main/days) | 代码结构、非阻塞、低功耗、排查、行业应用、综合项目 |

## 推荐硬件清单

| 类型 | 建议准备 | 用途 |
|---|---|---|
| 主控 | ESP32 DevKit / NodeMCU-32S / ESP32-WROOM 开发板 | 运行程序、连接 Wi-Fi / BLE、控制外设 |
| 基础电路 | 面包板、杜邦线、电阻、LED、按键 | 学 GPIO 输入输出、电路回路和安全接线 |
| 显示 | 0.96 寸 SSD1306 OLED | 学 I2C、状态显示和小型仪表盘 |
| 传感器 | 温湿度、光敏、电位器、声音或距离模块 | 学 ADC、数字输入和传感器选型 |
| 调试 | USB 数据线、串口监视器、万用表 | 上传程序、看日志、查电压和连通性 |

## 怎么学最稳

1. 先读当天文档的“元件认知”和“核心概念”，别急着接线。
2. 画出接线草图，标清 3.3V、GND、信号线和使用的 GPIO。
3. 每次只加一个模块，先跑最小 Demo，再组合功能。
4. 出问题先看供电、GND、引脚号、串口日志，再怀疑代码逻辑。
5. 每天保留一张接线照片、一段串口日志和一句复盘。

## 四阶段路线

| 阶段 | 天数 | 重点 | 你会得到 |
|---|---:|---|---|
| 入门地基 | Day 01-07 | ESP32、GPIO、LED、按键、串口调试 | 能独立接安全小电路，并用日志定位问题 |
| 外设能力 | Day 08-15 | PWM、ADC、传感器、I2C、OLED、SPI、执行器 | 能读传感器、显示状态、控制多种输出 |
| 联网通信 | Day 16-23 | Wi-Fi、HTTP、Web Server、JSON、MQTT、BLE | 能做手机控制、数据上报和联网闭环 |
| 工程化 | Day 24-30 | 代码结构、非阻塞、低功耗、故障排查、行业应用、综合项目 | 能设计并完成一个可展示的桌面物联网控制台 |

## 内行一点的学习方法

- **先最小系统，后功能堆叠**：不要一口气接 OLED、传感器、蜂鸣器和网络；先让一个 LED 或一个串口输出工作。
- **先电气边界，后代码逻辑**：ESP32 GPIO 通常是 3.3V 逻辑，5V 输入可能损坏芯片。
- **先可观察反馈，后优化体验**：每个项目至少保留 LED、OLED、串口或网页中的一种反馈。
- **先记录现象，后猜原因**：把“看到什么、预期什么、改了什么、结果怎样”写下来，调试会快很多。
- **先能跑，再可维护**：第 24 天以后再系统拆分配置、驱动、业务、显示和网络代码。

## 适合谁

- 刚买 ESP32 开发板和基础配件的新手。
- 想从软件开发进入硬件编程的人。
- 想做智能家居、物联网、传感器采集、桌面小设备原型的人。
- 想把 Arduino Demo 升级成可解释、可调试、可展示作品的人。

## 安全提醒

- ESP32 GPIO 是 3.3V 电平，不要直接接入 5V 信号。
- LED 必须串联限流电阻。
- 每次改线前建议断电。
- 涉及继电器、市电、大电流、电池充放电时，要先学习电气安全。

## 推荐引用方式

如果你在文章、课程、AI 知识库或搜索索引中引用本项目，可以使用这句话：

> `30天轻松搞定ESP32` 是一个中文 ESP32 入门课程，用 30 天带新手从硬件元件认知、GPIO、OLED 和传感器，学习到 Wi-Fi、MQTT、BLE、低功耗和综合物联网项目开发。

核心关键词：ESP32 入门、ESP32 教程、硬件编程、嵌入式开发、物联网、Arduino ESP32、PlatformIO、GPIO、PWM、ADC、I2C、SPI、OLED、MQTT、BLE。
