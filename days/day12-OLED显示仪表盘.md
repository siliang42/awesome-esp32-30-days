# Day 12：OLED 屏：显示文字、数值与图标

## 今日目标

驱动 SSD1306 OLED，显示项目标题、传感器数值和状态。

## 今天你会真正理解什么

有了 OLED，ESP32 就不再只是通过串口说话。它可以成为一个独立小设备。

## 元件认知

- `0.96 寸 OLED SSD1306`：常见 128x64 单色 OLED，I2C 地址多为 0x3C。
- `杜邦线`：连接开发板和元件的导线，分公对公、公对母、母对母。

## 核心概念

- **显示缓冲区**：先在内存中画好内容，再刷新到屏幕。
- **像素坐标**：屏幕上每个点的位置，例如 128x64 OLED 的 x/y 坐标。
- **字体**：字符显示的像素形状和大小。
- **刷新**：把缓冲区内容发送到屏幕显示。
- **I2C 地址**：OLED 常见地址是 0x3C，错误地址会导致无显示。

## 实操项目

**项目名称：** 制作一个小仪表盘：显示运行秒数、按键状态、ADC 数值。

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
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 display(128, 64, &Wire, -1);
const int BUTTON_PIN = 27;
const int POT_PIN = 34;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Wire.begin(21, 22);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
}

void loop() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println("ESP32 Dashboard");
  display.print("Seconds: ");
  display.println(millis() / 1000);
  display.print("Button: ");
  display.println(digitalRead(BUTTON_PIN) == LOW ? "DOWN" : "UP");
  display.print("ADC: ");
  display.println(analogRead(POT_PIN));
  display.display();
  delay(200);
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

- [Adafruit SSD1306 Guide](https://learn.adafruit.com/monochrome-oled-breakouts)
- [Random Nerd Tutorials ESP32](https://randomnerdtutorials.com/projects-esp32/)
