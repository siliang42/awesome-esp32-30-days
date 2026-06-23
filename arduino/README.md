# ESP32 30 天可烧录 Arduino 工程

每个目录都是一个独立 Arduino 工程，目录名和 `.ino` 文件名保持一致，可直接用 Arduino IDE 打开、编译、上传。

## 使用前准备

1. 安装 Arduino IDE。
2. 在 Boards Manager 安装 `esp32 by Espressif Systems`。
3. 按每天目录里的 `wiring.md` 接线。
4. 打开对应 `.ino`，选择开发板和串口后上传。
5. 串口监视器默认 `115200`。

## 每日工程索引

| 天数 | 工程目录 | 目标 |
|---|---|---|
| Day 01 | [day01_esp32_overview](day01_esp32_overview/) | 建立 ESP32 学习地图，认识开发板、面包板、杜邦线、电源、GPIO 和基础安全边界。 |
| Day 02 | [day02_blink](day02_blink/) | 完成开发环境、板卡包、串口驱动、上传流程，并点亮板载 LED 或外接 LED。 |
| Day 03 | [day03_safe_led_wiring](day03_safe_led_wiring/) | 理解电路回路、限流电阻、LED 极性，独立完成外接 LED 控制。 |
| Day 04 | [day04_gpio_chaser](day04_gpio_chaser/) | 使用多个 GPIO 控制多个 LED，理解非阻塞思维的第一步。 |
| Day 05 | [day05_button_debounce](day05_button_debounce/) | 读取按键状态，理解上拉/下拉、防抖和输入不稳定的原因。 |
| Day 06 | [day06_serial_debug](day06_serial_debug/) | 掌握 Serial 输出、调试日志、变量观察和基础故障定位。 |
| Day 07 | [day07_week1_blink_controller](day07_week1_blink_controller/) | 把 LED、按键、串口整合成一个可交互小项目。 |
| Day 08 | [day08_pwm_breath_led](day08_pwm_breath_led/) | 理解 PWM 的占空比、频率、通道，用 ESP32 输出渐变亮度。 |
| Day 09 | [day09_adc_pot_pwm](day09_adc_pot_pwm/) | 读取电位器电压，理解 ADC 分辨率、量程、噪声和采样。 |
| Day 10 | [day10_sensor_catalog](day10_sensor_catalog/) | 理解传感器的输入类型、供电、电平、数据手册和选型方法。 |
| Day 11 | [day11_i2c_scanner](day11_i2c_scanner/) | 理解 SDA、SCL、地址、上拉电阻和 I2C 扫描器。 |
| Day 12 | [day12_oled_dashboard](day12_oled_dashboard/) | 驱动 SSD1306 OLED，显示项目标题、传感器数值和状态。 |
| Day 13 | [day13_spi_bus_notes](day13_spi_bus_notes/) | 理解 SPI 的 MOSI、MISO、SCLK、CS，以及它和 I2C 的区别。 |
| Day 14 | [day14_buzzer_button](day14_buzzer_button/) | 理解输出不只是灯，还可以是声音、继电器、电机等执行器。 |
| Day 15 | [day15_week2_desk_monitor](day15_week2_desk_monitor/) | 组合 OLED、按键、ADC 或传感器，做一个可显示数据的小设备。 |
| Day 16 | [day16_wifi_connect](day16_wifi_connect/) | 让 ESP32 连接 Wi-Fi，理解 SSID、密码、IP、网关和连接状态。 |
| Day 17 | [day17_http_get](day17_http_get/) | 使用 HTTP GET 请求接口，理解 URL、状态码、响应体和超时。 |
| Day 18 | [day18_web_led_control](day18_web_led_control/) | 在 ESP32 上启动网页服务器，用手机访问并控制 LED。 |
| Day 19 | [day19_json_status](day19_json_status/) | 理解 JSON 表示设备状态，学习解析和生成简单 JSON。 |
| Day 20 | [day20_mqtt_led](day20_mqtt_led/) | 理解 MQTT Broker、Topic、Publish、Subscribe，用 ESP32 上报状态。 |
| Day 21 | [day21_ble_basic](day21_ble_basic/) | 理解经典蓝牙与 BLE 的区别，认识服务、特征值和近距离控制场景。 |
| Day 22 | [day22_cloud_payload_design](day22_cloud_payload_design/) | 理解设备数据如何进入云端、数据库和仪表盘。 |
| Day 23 | [day23_week3_iot_panel](day23_week3_iot_panel/) | 把 Wi-Fi、Web、MQTT/HTTP、OLED 和 LED 组合成联网小系统。 |
| Day 24 | [day24_structured_project](day24_structured_project/) | 学习把项目拆成配置、硬件驱动、业务逻辑、网络逻辑。 |
| Day 25 | [day25_millis_scheduler](day25_millis_scheduler/) | 摆脱大量 delay，使用 millis 管理多个周期任务。 |
| Day 26 | [day26_deep_sleep](day26_deep_sleep/) | 理解深度睡眠、唤醒源、电池供电、功耗预算和应用场景。 |
| Day 27 | [day27_hardware_troubleshooting](day27_hardware_troubleshooting/) | 建立硬件调试清单，系统定位常见问题。 |
| Day 28 | [day28_industry_app_planner](day28_industry_app_planner/) | 理解 ESP32 能力如何映射到真实行业场景。 |
| Day 29 | [day29_final_project_design](day29_final_project_design/) | 设计最终项目，包括需求、接线、页面、数据、异常处理。 |
| Day 30 | [day30_final_web_console](day30_final_web_console/) | 完成最终项目的硬件输入、输出、本地显示、Web 控制、状态接口和学习复盘。 |
