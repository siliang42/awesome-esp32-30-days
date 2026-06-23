# Day 29: 综合项目设计：桌面物联网控制台

## 今日目标

设计最终项目，包括需求、接线、页面、数据、异常处理。

## 可烧录代码

- Arduino 工程文件：`day29_final_project_design.ino`
- 打开方式：用 Arduino IDE 打开本目录下的 `day29_final_project_design.ino`，选择 ESP32 开发板和串口后上传。
- 如果文件夹名和 `.ino` 文件名保持一致，Arduino IDE 可以直接识别为一个工程。

## 依赖库

- 无额外库，使用 Arduino-ESP32 自带库。

## 烧录前检查

1. Arduino IDE 已安装 `esp32 by Espressif Systems` 板卡包。
2. 开发板选择常见 `ESP32 Dev Module`，或选择你手头开发板对应型号。
3. 串口监视器波特率使用 `115200`。
4. 涉及 Wi-Fi 的项目，先在 `.ino` 里修改 `SSID` 和 `PASSWORD`。
5. 涉及 OLED 的项目，如果屏幕无显示，先运行 Day 11 的 I2C Scanner 确认地址。

## 对应接线

见 [`wiring.md`](wiring.md)。

## 建议实验

写出最终项目设计：本地显示、手机控制、数据采集、告警提示。
