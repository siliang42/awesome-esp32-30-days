# Day 10: 常见传感器认知：温湿度、光敏、声音、距离

## 今日目标

理解传感器的输入类型、供电、电平、数据手册和选型方法。

## 可烧录代码

- Arduino 工程文件：`day10_sensor_catalog.ino`
- 打开方式：用 Arduino IDE 打开本目录下的 `day10_sensor_catalog.ino`，选择 ESP32 开发板和串口后上传。
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

整理 4 类传感器表格：供电、电平、接口、输出含义、应用场景。
