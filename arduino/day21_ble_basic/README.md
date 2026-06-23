# Day 21: 蓝牙 BLE 认知：近场设备通信

## 今日目标

理解经典蓝牙与 BLE 的区别，认识服务、特征值和近距离控制场景。

## 可烧录代码

- Arduino 工程文件：`day21_ble_basic.ino`
- 打开方式：用 Arduino IDE 打开本目录下的 `day21_ble_basic.ino`，选择 ESP32 开发板和串口后上传。
- 如果文件夹名和 `.ino` 文件名保持一致，Arduino IDE 可以直接识别为一个工程。

## 依赖库

- ESP32 BLE Arduino / Arduino-ESP32 built-in BLE headers

## 烧录前检查

1. Arduino IDE 已安装 `esp32 by Espressif Systems` 板卡包。
2. 开发板选择常见 `ESP32 Dev Module`，或选择你手头开发板对应型号。
3. 串口监视器波特率使用 `115200`。
4. 涉及 Wi-Fi 的项目，先在 `.ino` 里修改 `SSID` 和 `PASSWORD`。
5. 涉及 OLED 的项目，如果屏幕无显示，先运行 Day 11 的 I2C Scanner 确认地址。

## 对应接线

见 [`wiring.md`](wiring.md)。

## 建议实验

创建一个 BLE 设备，让手机发现它，并读取一个状态值。
