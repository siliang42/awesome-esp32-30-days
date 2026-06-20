from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
DAYS_DIR = ROOT / "days"


LINKS = {
    "ESP32 Arduino Core": "https://docs.espressif.com/projects/arduino-esp32/en/latest/",
    "ESP-IDF Programming Guide": "https://docs.espressif.com/projects/esp-idf/en/latest/esp32/",
    "ESP32 Datasheet": "https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf",
    "ESP32 Technical Reference Manual": "https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf",
    "PlatformIO ESP32": "https://docs.platformio.org/en/latest/platforms/espressif32.html",
    "Wokwi ESP32 Simulator": "https://docs.wokwi.com/guides/esp32",
    "Random Nerd Tutorials ESP32": "https://randomnerdtutorials.com/projects-esp32/",
    "Adafruit SSD1306 Guide": "https://learn.adafruit.com/monochrome-oled-breakouts",
    "PubSubClient MQTT": "https://pubsubclient.knolleary.net/",
    "MQTT Essentials": "https://www.hivemq.com/mqtt-essentials/",
}


DAYS = [
    {
        "title": "认识 ESP32、开发板与硬件编程全景",
        "goal": "建立 ESP32 学习地图，认识开发板、面包板、杜邦线、电源、GPIO 和基础安全边界。",
        "parts": ["ESP32 开发板", "USB 数据线", "面包板", "杜邦线", "电阻", "LED", "按键", "OLED 屏"],
        "concepts": ["单片机是什么", "GPIO", "3.3V 与 5V", "面包板内部连通方式", "输入与输出"],
        "project": "画出你的硬件学习工作台连接草图，并整理元件清单。",
        "code": None,
        "focus": "先把硬件世界看成一个小城市：ESP32 是大脑，GPIO 是街道，电源是供水供电系统，元件是各类设备。今天不急着写复杂代码，重点是知道每个东西为什么存在。",
        "links": ["ESP32 Datasheet", "ESP32 Arduino Core", "Random Nerd Tutorials ESP32"],
    },
    {
        "title": "搭建 Arduino IDE / PlatformIO 与第一个 Blink",
        "goal": "完成开发环境、板卡包、串口驱动、上传流程，并点亮板载 LED 或外接 LED。",
        "parts": ["ESP32 开发板", "LED", "220Ω 电阻", "面包板", "杜邦线"],
        "concepts": ["固件上传", "串口端口", "setup 与 loop", "数字输出", "限流电阻"],
        "project": "上传 Blink 程序，让 LED 每秒闪烁一次。",
        "code": "blink",
        "focus": "第一个成功上传非常重要。它证明电脑、USB、驱动、开发板、代码、编译器、串口下载链路全部打通。",
        "links": ["ESP32 Arduino Core", "PlatformIO ESP32", "Wokwi ESP32 Simulator"],
    },
    {
        "title": "面包板、电阻、LED 与安全接线",
        "goal": "理解电路回路、限流电阻、LED 极性，独立完成外接 LED 控制。",
        "parts": ["LED", "220Ω/330Ω 电阻", "面包板", "杜邦线"],
        "concepts": ["闭合回路", "欧姆定律", "LED 正负极", "灌电流与拉电流", "短路风险"],
        "project": "把 LED 从板载灯换成外接灯，并尝试不同闪烁节奏。",
        "code": "multi_blink",
        "focus": "硬件编程不是只有代码。代码说 HIGH，真正发光的是电压、电流、元件方向和回路共同配合。",
        "links": ["ESP32 Datasheet", "Random Nerd Tutorials ESP32"],
    },
    {
        "title": "GPIO 数字输出：流水灯与状态机思维",
        "goal": "使用多个 GPIO 控制多个 LED，理解非阻塞思维的第一步。",
        "parts": ["3 个 LED", "3 个电阻", "面包板", "杜邦线"],
        "concepts": ["GPIO 编号", "数组控制引脚", "delay 的局限", "简单状态机"],
        "project": "制作三灯流水灯，并调整方向和速度。",
        "code": "chase_leds",
        "focus": "多个灯就是多个输出通道。你会开始把重复代码整理成数组和循环，这是嵌入式项目变大的第一道门。",
        "links": ["ESP32 Arduino Core", "Wokwi ESP32 Simulator"],
    },
    {
        "title": "按键输入、防抖与人机交互",
        "goal": "读取按键状态，理解上拉/下拉、防抖和输入不稳定的原因。",
        "parts": ["轻触开关", "LED", "电阻", "面包板", "杜邦线"],
        "concepts": ["数字输入", "INPUT_PULLUP", "机械抖动", "边沿触发", "按钮状态机"],
        "project": "按一下切换 LED 开关状态。",
        "code": "button_toggle",
        "focus": "按键看起来简单，却是理解真实世界噪声的第一课。硬件不是理想数学，它会抖、会浮空、会受线材影响。",
        "links": ["ESP32 Arduino Core", "Random Nerd Tutorials ESP32"],
    },
    {
        "title": "串口监视器：让 ESP32 学会说话",
        "goal": "掌握 Serial 输出、调试日志、变量观察和基础故障定位。",
        "parts": ["ESP32 开发板", "按键", "LED"],
        "concepts": ["串口波特率", "日志级别", "变量打印", "调试闭环"],
        "project": "按键控制 LED，并在串口输出每一次状态变化。",
        "code": "serial_button",
        "focus": "串口是嵌入式开发者的听诊器。没有屏幕时，你靠它知道芯片里面发生了什么。",
        "links": ["ESP32 Arduino Core", "ESP-IDF Programming Guide"],
    },
    {
        "title": "第一周整合项目：可调节闪灯控制器",
        "goal": "把 LED、按键、串口整合成一个可交互小项目。",
        "parts": ["LED", "按键", "电阻", "面包板", "杜邦线"],
        "concepts": ["需求拆解", "接线表", "测试清单", "项目复盘"],
        "project": "短按切换模式，长按改变闪烁速度，串口输出当前模式。",
        "code": "week1_controller",
        "focus": "今天开始像工程师一样做项目：先列需求，再画接线，再写代码，最后用清单验证。",
        "links": ["Wokwi ESP32 Simulator", "ESP32 Arduino Core"],
    },
    {
        "title": "PWM：让 LED 呼吸起来",
        "goal": "理解 PWM 的占空比、频率、通道，用 ESP32 输出渐变亮度。",
        "parts": ["LED", "电阻"],
        "concepts": ["PWM", "占空比", "频率", "LEDC", "模拟效果"],
        "project": "制作呼吸灯，并用按键切换呼吸速度。",
        "code": "pwm_breath",
        "focus": "PWM 是数字芯片模拟连续世界的魔法：不是电压真的连续变化，而是高速开关让人眼感到亮度变化。",
        "links": ["ESP32 Arduino Core", "ESP32 Technical Reference Manual"],
    },
    {
        "title": "ADC：读取电位器与模拟量",
        "goal": "读取电位器电压，理解 ADC 分辨率、量程、噪声和采样。",
        "parts": ["电位器", "杜邦线", "面包板"],
        "concepts": ["ADC", "模拟输入", "采样", "分辨率", "电压分压"],
        "project": "用电位器控制 LED 亮度，并在串口显示 ADC 数值。",
        "code": "adc_pot_pwm",
        "focus": "传感器多数最终都变成电压、电流、脉冲或数字总线。ADC 是进入模拟世界的重要入口。",
        "links": ["ESP32 Datasheet", "Random Nerd Tutorials ESP32"],
    },
    {
        "title": "常见传感器认知：温湿度、光敏、声音、距离",
        "goal": "理解传感器的输入类型、供电、电平、数据手册和选型方法。",
        "parts": ["DHT11/DHT22 或 SHT30", "光敏电阻", "超声波模块", "可选声音传感器"],
        "concepts": ["数字传感器", "模拟传感器", "校准", "采样周期", "数据手册"],
        "project": "整理 4 类传感器表格：供电、电平、接口、输出含义、应用场景。",
        "code": None,
        "focus": "今天重点不是把所有传感器都接完，而是学会读懂一个新模块。会读模块，比背一堆教程更重要。",
        "links": ["ESP32 Datasheet", "Random Nerd Tutorials ESP32"],
    },
    {
        "title": "I2C 总线：认识两根线连接多个设备",
        "goal": "理解 SDA、SCL、地址、上拉电阻和 I2C 扫描器。",
        "parts": ["OLED 屏", "可选 I2C 传感器", "杜邦线"],
        "concepts": ["I2C", "SDA/SCL", "设备地址", "总线扫描", "上拉"],
        "project": "运行 I2C Scanner，找到 OLED 地址。",
        "code": "i2c_scanner",
        "focus": "I2C 像一条公交线：SDA 传数据，SCL 给节奏，每个设备靠地址上车下车。",
        "links": ["Adafruit SSD1306 Guide", "ESP32 Arduino Core"],
    },
    {
        "title": "OLED 屏：显示文字、数值与图标",
        "goal": "驱动 SSD1306 OLED，显示项目标题、传感器数值和状态。",
        "parts": ["0.96 寸 OLED SSD1306", "杜邦线"],
        "concepts": ["显示缓冲区", "像素坐标", "字体", "刷新", "I2C 地址"],
        "project": "制作一个小仪表盘：显示运行秒数、按键状态、ADC 数值。",
        "code": "oled_dashboard",
        "focus": "有了 OLED，ESP32 就不再只是通过串口说话。它可以成为一个独立小设备。",
        "links": ["Adafruit SSD1306 Guide", "Random Nerd Tutorials ESP32"],
    },
    {
        "title": "SPI 与高速外设认知",
        "goal": "理解 SPI 的 MOSI、MISO、SCLK、CS，以及它和 I2C 的区别。",
        "parts": ["可选 SPI 屏幕/SD 卡模块", "杜邦线"],
        "concepts": ["SPI", "片选 CS", "全双工", "总线速度", "I2C vs SPI"],
        "project": "画出 I2C 与 SPI 接线对比图，并写出各自适合的应用。",
        "code": None,
        "focus": "I2C 省线，SPI 更快。很多显示屏、SD 卡、射频模块会选择 SPI。",
        "links": ["ESP32 Technical Reference Manual", "ESP-IDF Programming Guide"],
    },
    {
        "title": "蜂鸣器、继电器与执行器基础",
        "goal": "理解输出不只是灯，还可以是声音、继电器、电机等执行器。",
        "parts": ["有源蜂鸣器", "可选继电器模块", "LED"],
        "concepts": ["执行器", "驱动能力", "晶体管", "继电器隔离", "反向电动势"],
        "project": "制作按键触发提示音，并用 LED 同步显示状态。",
        "code": "buzzer_button",
        "focus": "ESP32 的 GPIO 不能直接带大负载。控制外部世界时，常常需要驱动电路或模块。",
        "links": ["ESP32 Datasheet", "Random Nerd Tutorials ESP32"],
    },
    {
        "title": "第二周整合项目：桌面环境监测器",
        "goal": "组合 OLED、按键、ADC 或传感器，做一个可显示数据的小设备。",
        "parts": ["OLED", "按键", "电位器或温湿度传感器", "LED"],
        "concepts": ["数据采集", "显示刷新", "页面切换", "模块化函数"],
        "project": "OLED 显示传感器值，按键切换页面，LED 表示阈值告警。",
        "code": "week2_monitor",
        "focus": "你开始接近真实产品形态：输入、处理、显示、告警，一个最小闭环已经形成。",
        "links": ["Adafruit SSD1306 Guide", "Wokwi ESP32 Simulator"],
    },
    {
        "title": "Wi-Fi 入门：连接路由器与理解网络参数",
        "goal": "让 ESP32 连接 Wi-Fi，理解 SSID、密码、IP、网关和连接状态。",
        "parts": ["ESP32 开发板"],
        "concepts": ["Wi-Fi STA 模式", "IP 地址", "网关", "DNS", "重连"],
        "project": "连接家中 Wi-Fi，并在串口输出 IP 地址和信号强度。",
        "code": "wifi_connect",
        "focus": "ESP32 进入物联网世界的关键能力是联网。联网后，它就能上报数据、接收命令、访问云服务。",
        "links": ["ESP32 Arduino Core", "ESP-IDF Programming Guide"],
    },
    {
        "title": "HTTP 客户端：让 ESP32 请求网络数据",
        "goal": "使用 HTTP GET 请求接口，理解 URL、状态码、响应体和超时。",
        "parts": ["ESP32 开发板", "OLED 可选"],
        "concepts": ["HTTP GET", "状态码", "JSON", "超时", "网络错误"],
        "project": "请求一个公开 API 或本地接口，并在串口输出响应。",
        "code": "http_get",
        "focus": "联网设备最常见的动作之一就是请求接口。今天你会把 ESP32 当成一个很小的网络客户端。",
        "links": ["ESP32 Arduino Core", "Random Nerd Tutorials ESP32"],
    },
    {
        "title": "Web Server：手机浏览器控制 LED",
        "goal": "在 ESP32 上启动网页服务器，用手机访问并控制 LED。",
        "parts": ["LED", "电阻", "ESP32 开发板"],
        "concepts": ["Web Server", "路由", "HTML", "局域网访问", "请求处理"],
        "project": "打开手机浏览器，点击网页按钮控制 LED 开关。",
        "code": "web_led",
        "focus": "这是很有成就感的一天：一个没有操作系统界面的开发板，自己提供网页，并能被手机控制。",
        "links": ["ESP32 Arduino Core", "Random Nerd Tutorials ESP32"],
    },
    {
        "title": "JSON 与数据结构：从字符串到设备状态",
        "goal": "理解 JSON 表示设备状态，学习解析和生成简单 JSON。",
        "parts": ["ESP32 开发板", "OLED 可选"],
        "concepts": ["JSON", "键值对", "设备状态", "序列化", "ArduinoJson"],
        "project": "把 LED 状态、ADC 数值、运行时间组织成 JSON 输出。",
        "code": "json_status",
        "focus": "物联网不是只让灯亮，而是把设备状态变成可传输、可理解、可存储的数据。",
        "links": ["ESP32 Arduino Core", "MQTT Essentials"],
    },
    {
        "title": "MQTT 入门：发布与订阅",
        "goal": "理解 MQTT Broker、Topic、Publish、Subscribe，用 ESP32 上报状态。",
        "parts": ["ESP32 开发板", "LED 可选"],
        "concepts": ["MQTT", "Broker", "Topic", "QoS", "保活"],
        "project": "向 MQTT Broker 发布运行状态，并订阅命令控制 LED。",
        "code": "mqtt_led",
        "focus": "MQTT 是物联网里非常常见的通信方式。它像消息公告板，设备不用互相直连，只要围绕主题收发消息。",
        "links": ["PubSubClient MQTT", "MQTT Essentials"],
    },
    {
        "title": "蓝牙 BLE 认知：近场设备通信",
        "goal": "理解经典蓝牙与 BLE 的区别，认识服务、特征值和近距离控制场景。",
        "parts": ["ESP32 开发板", "手机 BLE 调试 App"],
        "concepts": ["BLE", "GATT", "Service", "Characteristic", "UUID"],
        "project": "创建一个 BLE 设备，让手机发现它，并读取一个状态值。",
        "code": "ble_basic",
        "focus": "Wi-Fi 适合上网，BLE 适合近距离、低功耗、手机配网或设备控制。",
        "links": ["ESP32 Arduino Core", "ESP-IDF Programming Guide"],
    },
    {
        "title": "数据上云与仪表盘思维",
        "goal": "理解设备数据如何进入云端、数据库和仪表盘。",
        "parts": ["ESP32 开发板", "传感器或电位器"],
        "concepts": ["云平台", "时序数据", "设备 ID", "Token", "仪表盘"],
        "project": "设计一份设备上云数据格式，并选择一个平台做后续尝试。",
        "code": None,
        "focus": "行业应用里，单个设备只是起点。真正有价值的是大量设备持续产生的数据和远程管理能力。",
        "links": ["MQTT Essentials", "Random Nerd Tutorials ESP32"],
    },
    {
        "title": "第三周整合项目：手机控制 + 数据上报小系统",
        "goal": "把 Wi-Fi、Web、MQTT/HTTP、OLED 和 LED 组合成联网小系统。",
        "parts": ["ESP32", "LED", "按键", "OLED", "电位器或传感器"],
        "concepts": ["设备状态机", "远程控制", "本地显示", "错误恢复"],
        "project": "手机网页控制 LED，OLED 显示 IP 和状态，串口输出网络日志。",
        "code": "week3_iot_panel",
        "focus": "这已经是一个完整物联网雏形：本地交互、网络控制、状态显示、故障日志全部出现。",
        "links": ["ESP32 Arduino Core", "Wokwi ESP32 Simulator", "PubSubClient MQTT"],
    },
    {
        "title": "代码结构：从能跑到可维护",
        "goal": "学习把项目拆成配置、硬件驱动、业务逻辑、网络逻辑。",
        "parts": ["已有项目代码"],
        "concepts": ["模块化", "配置集中", "函数边界", "命名", "可读性"],
        "project": "重构第三周项目，把 LED、OLED、Wi-Fi 逻辑拆成独立函数。",
        "code": "structured_project",
        "focus": "硬件项目一开始容易写成一个巨大的 loop。今天你会学习如何让代码以后还能被自己看懂。",
        "links": ["ESP32 Arduino Core", "PlatformIO ESP32"],
    },
    {
        "title": "定时器、millis 与非阻塞程序",
        "goal": "摆脱大量 delay，使用 millis 管理多个周期任务。",
        "parts": ["LED", "OLED", "按键"],
        "concepts": ["非阻塞", "任务周期", "millis 溢出", "调度", "响应性"],
        "project": "同时实现 LED 闪烁、按键响应、OLED 刷新，互不阻塞。",
        "code": "millis_scheduler",
        "focus": "真实设备要一边读传感器，一边响应按键，一边联网。delay 会让设备像发呆一样错过事件。",
        "links": ["ESP32 Arduino Core", "ESP-IDF Programming Guide"],
    },
    {
        "title": "低功耗与电池供电认知",
        "goal": "理解深度睡眠、唤醒源、电池供电、功耗预算和应用场景。",
        "parts": ["ESP32 开发板", "可选电池模块"],
        "concepts": ["Deep Sleep", "唤醒", "功耗", "电池容量", "采样间隔"],
        "project": "让 ESP32 每隔一段时间醒来打印一次日志，然后重新睡眠。",
        "code": "deep_sleep",
        "focus": "物联网设备常常不是一直插电。低功耗设计决定设备能跑一天、一个月还是一年。",
        "links": ["ESP-IDF Programming Guide", "ESP32 Datasheet"],
    },
    {
        "title": "故障排查：从烧录失败到接线错误",
        "goal": "建立硬件调试清单，系统定位常见问题。",
        "parts": ["万用表可选", "ESP32", "所有常用模块"],
        "concepts": ["分层排查", "最小系统", "电源检查", "串口日志", "替换法"],
        "project": "制作自己的 ESP32 调试检查表。",
        "code": None,
        "focus": "优秀硬件开发者不是不会出错，而是能快速把问题缩小到电源、接线、代码、库、网络或元件本身。",
        "links": ["ESP32 Arduino Core", "Wokwi ESP32 Simulator"],
    },
    {
        "title": "行业应用：智能家居、工业采集、农业、穿戴",
        "goal": "理解 ESP32 能力如何映射到真实行业场景。",
        "parts": ["已有元件清单"],
        "concepts": ["边缘设备", "传感采集", "远程控制", "OTA", "安全", "量产约束"],
        "project": "选择一个行业场景，写出设备功能表、传感器、执行器、通信方式。",
        "code": None,
        "focus": "从今天开始，你不只是会接模块，还要能判断一个项目为什么需要 ESP32，需要什么外设，如何部署。",
        "links": ["ESP-IDF Programming Guide", "ESP32 Technical Reference Manual"],
    },
    {
        "title": "综合项目设计：桌面物联网控制台",
        "goal": "设计最终项目，包括需求、接线、页面、数据、异常处理。",
        "parts": ["ESP32", "OLED", "LED", "按键", "电位器或传感器", "蜂鸣器可选"],
        "concepts": ["项目设计文档", "验收标准", "风险清单", "迭代计划"],
        "project": "写出最终项目设计：本地显示、手机控制、数据采集、告警提示。",
        "code": None,
        "focus": "做复杂项目之前先设计，能让你少走很多弯路。今天只设计，明天实现。",
        "links": ["Wokwi ESP32 Simulator", "ESP32 Arduino Core"],
    },
    {
        "title": "综合项目收官：本地闭环、Web 控制与进阶复盘",
        "goal": "完成最终项目的硬件输入、输出、本地显示、Web 控制、状态接口和学习复盘。",
        "parts": ["ESP32", "OLED", "LED", "按键", "电位器或传感器", "所有项目", "笔记", "代码", "照片"],
        "concepts": ["接线实现", "分模块调试", "本地闭环", "HTTP API", "网页控制", "状态同步", "验收测试", "作品集", "技术路线", "ESP-IDF", "FreeRTOS", "PCB", "OTA"],
        "project": "完成桌面物联网控制台：本地显示传感器值，手机网页查看状态并控制 LED，最后整理作品集和下一阶段计划。",
        "code": "final_web_console",
        "focus": "最终项目变成一个真正可交互的联网设备。收官不是结束，而是把 30 天沉淀成作品、方法和下一条进阶路线。",
        "links": ["ESP32 Arduino Core", "Random Nerd Tutorials ESP32", "ESP-IDF Programming Guide", "ESP32 Technical Reference Manual", "PlatformIO ESP32"],
    },
]


CODE_SNIPPETS = {
    "blink": dedent("""\
        const int LED_PIN = 2;

        void setup() {
          pinMode(LED_PIN, OUTPUT);
        }

        void loop() {
          digitalWrite(LED_PIN, HIGH);
          delay(1000);
          digitalWrite(LED_PIN, LOW);
          delay(1000);
        }
    """),
    "multi_blink": dedent("""\
        const int LED_PIN = 23;

        void setup() {
          pinMode(LED_PIN, OUTPUT);
        }

        void loop() {
          digitalWrite(LED_PIN, HIGH);
          delay(200);
          digitalWrite(LED_PIN, LOW);
          delay(200);
          digitalWrite(LED_PIN, HIGH);
          delay(600);
          digitalWrite(LED_PIN, LOW);
          delay(1000);
        }
    """),
    "chase_leds": dedent("""\
        const int LEDS[] = {18, 19, 23};
        const int LED_COUNT = 3;

        void setup() {
          for (int i = 0; i < LED_COUNT; i++) {
            pinMode(LEDS[i], OUTPUT);
          }
        }

        void loop() {
          for (int i = 0; i < LED_COUNT; i++) {
            digitalWrite(LEDS[i], HIGH);
            delay(180);
            digitalWrite(LEDS[i], LOW);
          }
        }
    """),
    "button_toggle": dedent("""\
        const int BUTTON_PIN = 27;
        const int LED_PIN = 23;
        bool ledOn = false;
        int lastReading = HIGH;
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
          }

          if ((millis() - lastDebounceTime) > debounceDelay && reading == LOW && lastReading == HIGH) {
            ledOn = !ledOn;
            digitalWrite(LED_PIN, ledOn ? HIGH : LOW);
          }

          lastReading = reading;
        }
    """),
    "serial_button": dedent("""\
        const int BUTTON_PIN = 27;
        const int LED_PIN = 23;
        bool ledOn = false;
        int previous = HIGH;

        void setup() {
          Serial.begin(115200);
          pinMode(BUTTON_PIN, INPUT_PULLUP);
          pinMode(LED_PIN, OUTPUT);
          Serial.println("Serial button demo started");
        }

        void loop() {
          int current = digitalRead(BUTTON_PIN);
          if (previous == HIGH && current == LOW) {
            ledOn = !ledOn;
            digitalWrite(LED_PIN, ledOn);
            Serial.print("LED state changed: ");
            Serial.println(ledOn ? "ON" : "OFF");
            delay(50);
          }
          previous = current;
        }
    """),
    "week1_controller": dedent("""\
        const int BUTTON_PIN = 27;
        const int LED_PIN = 23;
        int mode = 0;
        unsigned long lastBlink = 0;
        bool ledState = false;

        int intervalForMode() {
          if (mode == 0) return 1000;
          if (mode == 1) return 300;
          return 100;
        }

        void setup() {
          Serial.begin(115200);
          pinMode(BUTTON_PIN, INPUT_PULLUP);
          pinMode(LED_PIN, OUTPUT);
        }

        void loop() {
          static int lastButton = HIGH;
          int currentButton = digitalRead(BUTTON_PIN);
          if (lastButton == HIGH && currentButton == LOW) {
            mode = (mode + 1) % 3;
            Serial.print("Mode: ");
            Serial.println(mode);
            delay(60);
          }
          lastButton = currentButton;

          if (millis() - lastBlink >= intervalForMode()) {
            lastBlink = millis();
            ledState = !ledState;
            digitalWrite(LED_PIN, ledState);
          }
        }
    """),
    "pwm_breath": dedent("""\
        const int LED_PIN = 23;
        const int PWM_CHANNEL = 0;
        const int PWM_FREQ = 5000;
        const int PWM_RESOLUTION = 8;

        void setup() {
          ledcSetup(PWM_CHANNEL, PWM_FREQ, PWM_RESOLUTION);
          ledcAttachPin(LED_PIN, PWM_CHANNEL);
        }

        void loop() {
          for (int duty = 0; duty <= 255; duty++) {
            ledcWrite(PWM_CHANNEL, duty);
            delay(8);
          }
          for (int duty = 255; duty >= 0; duty--) {
            ledcWrite(PWM_CHANNEL, duty);
            delay(8);
          }
        }
    """),
    "adc_pot_pwm": dedent("""\
        const int POT_PIN = 34;
        const int LED_PIN = 23;
        const int PWM_CHANNEL = 0;

        void setup() {
          Serial.begin(115200);
          ledcSetup(PWM_CHANNEL, 5000, 8);
          ledcAttachPin(LED_PIN, PWM_CHANNEL);
        }

        void loop() {
          int raw = analogRead(POT_PIN);
          int duty = map(raw, 0, 4095, 0, 255);
          ledcWrite(PWM_CHANNEL, duty);
          Serial.printf("ADC=%d, duty=%d\\n", raw, duty);
          delay(100);
        }
    """),
    "i2c_scanner": dedent("""\
        #include <Wire.h>

        void setup() {
          Serial.begin(115200);
          Wire.begin(21, 22);
          Serial.println("I2C scanner started");
        }

        void loop() {
          for (byte address = 1; address < 127; address++) {
            Wire.beginTransmission(address);
            if (Wire.endTransmission() == 0) {
              Serial.print("Found I2C device at 0x");
              Serial.println(address, HEX);
            }
          }
          delay(3000);
        }
    """),
    "oled_dashboard": dedent("""\
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
    """),
    "buzzer_button": dedent("""\
        const int BUTTON_PIN = 27;
        const int BUZZER_PIN = 25;

        void setup() {
          pinMode(BUTTON_PIN, INPUT_PULLUP);
          pinMode(BUZZER_PIN, OUTPUT);
        }

        void loop() {
          if (digitalRead(BUTTON_PIN) == LOW) {
            digitalWrite(BUZZER_PIN, HIGH);
            delay(80);
            digitalWrite(BUZZER_PIN, LOW);
            delay(120);
          }
        }
    """),
    "week2_monitor": dedent("""\
        #include <Wire.h>
        #include <Adafruit_GFX.h>
        #include <Adafruit_SSD1306.h>

        Adafruit_SSD1306 display(128, 64, &Wire, -1);
        const int POT_PIN = 34;
        const int LED_PIN = 23;

        void setup() {
          pinMode(LED_PIN, OUTPUT);
          Wire.begin(21, 22);
          display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
          display.setTextColor(SSD1306_WHITE);
        }

        void loop() {
          int value = analogRead(POT_PIN);
          digitalWrite(LED_PIN, value > 2500 ? HIGH : LOW);
          display.clearDisplay();
          display.setCursor(0, 0);
          display.setTextSize(1);
          display.println("Desk Monitor");
          display.print("Sensor: ");
          display.println(value);
          display.print("Alert: ");
          display.println(value > 2500 ? "YES" : "NO");
          display.display();
          delay(250);
        }
    """),
    "wifi_connect": dedent("""\
        #include <WiFi.h>

        const char* SSID = "your_wifi_name";
        const char* PASSWORD = "your_wifi_password";

        void setup() {
          Serial.begin(115200);
          WiFi.begin(SSID, PASSWORD);
          Serial.print("Connecting");
          while (WiFi.status() != WL_CONNECTED) {
            delay(500);
            Serial.print(".");
          }
          Serial.println();
          Serial.print("IP address: ");
          Serial.println(WiFi.localIP());
          Serial.print("RSSI: ");
          Serial.println(WiFi.RSSI());
        }

        void loop() {
        }
    """),
    "http_get": dedent("""\
        #include <WiFi.h>
        #include <HTTPClient.h>

        const char* SSID = "your_wifi_name";
        const char* PASSWORD = "your_wifi_password";

        void setup() {
          Serial.begin(115200);
          WiFi.begin(SSID, PASSWORD);
          while (WiFi.status() != WL_CONNECTED) delay(500);

          HTTPClient http;
          http.begin("http://worldtimeapi.org/api/timezone/Asia/Shanghai");
          int code = http.GET();
          Serial.print("HTTP status: ");
          Serial.println(code);
          if (code > 0) {
            Serial.println(http.getString());
          }
          http.end();
        }

        void loop() {
        }
    """),
    "web_led": dedent("""\
        #include <WiFi.h>
        #include <WebServer.h>

        const char* SSID = "your_wifi_name";
        const char* PASSWORD = "your_wifi_password";
        const int LED_PIN = 23;
        WebServer server(80);

        void handleRoot() {
          String html = "<h1>ESP32 LED</h1><a href='/on'>ON</a><br><a href='/off'>OFF</a>";
          server.send(200, "text/html", html);
        }

        void setup() {
          Serial.begin(115200);
          pinMode(LED_PIN, OUTPUT);
          WiFi.begin(SSID, PASSWORD);
          while (WiFi.status() != WL_CONNECTED) delay(500);
          Serial.println(WiFi.localIP());

          server.on("/", handleRoot);
          server.on("/on", []() {
            digitalWrite(LED_PIN, HIGH);
            server.sendHeader("Location", "/");
            server.send(302);
          });
          server.on("/off", []() {
            digitalWrite(LED_PIN, LOW);
            server.sendHeader("Location", "/");
            server.send(302);
          });
          server.begin();
        }

        void loop() {
          server.handleClient();
        }
    """),
    "json_status": dedent("""\
        #include <ArduinoJson.h>

        const int LED_PIN = 23;
        const int POT_PIN = 34;

        void setup() {
          Serial.begin(115200);
          pinMode(LED_PIN, OUTPUT);
        }

        void loop() {
          StaticJsonDocument<200> doc;
          doc["device"] = "esp32-demo";
          doc["uptime"] = millis() / 1000;
          doc["adc"] = analogRead(POT_PIN);
          doc["led"] = digitalRead(LED_PIN) == HIGH;
          serializeJson(doc, Serial);
          Serial.println();
          delay(1000);
        }
    """),
    "mqtt_led": dedent("""\
        #include <WiFi.h>
        #include <PubSubClient.h>

        const char* SSID = "your_wifi_name";
        const char* PASSWORD = "your_wifi_password";
        const char* MQTT_HOST = "broker.hivemq.com";
        const int LED_PIN = 23;

        WiFiClient wifiClient;
        PubSubClient mqtt(wifiClient);

        void callback(char* topic, byte* payload, unsigned int length) {
          String message;
          for (unsigned int i = 0; i < length; i++) message += (char)payload[i];
          digitalWrite(LED_PIN, message == "on" ? HIGH : LOW);
        }

        void reconnect() {
          while (!mqtt.connected()) {
            if (mqtt.connect("esp32-demo-client")) {
              mqtt.subscribe("esp32/demo/led");
            } else {
              delay(2000);
            }
          }
        }

        void setup() {
          pinMode(LED_PIN, OUTPUT);
          WiFi.begin(SSID, PASSWORD);
          while (WiFi.status() != WL_CONNECTED) delay(500);
          mqtt.setServer(MQTT_HOST, 1883);
          mqtt.setCallback(callback);
        }

        void loop() {
          if (!mqtt.connected()) reconnect();
          mqtt.loop();
          mqtt.publish("esp32/demo/status", "online");
          delay(2000);
        }
    """),
    "ble_basic": dedent("""\
        #include <BLEDevice.h>
        #include <BLEServer.h>
        #include <BLEUtils.h>

        BLECharacteristic* statusCharacteristic;

        void setup() {
          BLEDevice::init("ESP32-BLE-Demo");
          BLEServer* server = BLEDevice::createServer();
          BLEService* service = server->createService("12345678-1234-1234-1234-1234567890ab");
          statusCharacteristic = service->createCharacteristic(
            "abcd1234-1234-1234-1234-abcdef123456",
            BLECharacteristic::PROPERTY_READ
          );
          statusCharacteristic->setValue("hello from esp32");
          service->start();
          BLEDevice::getAdvertising()->start();
        }

        void loop() {
        }
    """),
    "week3_iot_panel": dedent("""\
        #include <WiFi.h>
        #include <WebServer.h>

        const char* SSID = "your_wifi_name";
        const char* PASSWORD = "your_wifi_password";
        const int LED_PIN = 23;
        const int SENSOR_PIN = 34;
        WebServer server(80);

        String statusJson() {
          return String("{\\"adc\\":") + analogRead(SENSOR_PIN) +
                 String(",\\"led\\":") + (digitalRead(LED_PIN) ? "true" : "false") + "}";
        }

        void setup() {
          Serial.begin(115200);
          pinMode(LED_PIN, OUTPUT);
          WiFi.begin(SSID, PASSWORD);
          while (WiFi.status() != WL_CONNECTED) delay(500);
          Serial.println(WiFi.localIP());
          server.on("/", []() {
            server.send(200, "text/html", "<h1>ESP32 Panel</h1><a href='/on'>ON</a> <a href='/off'>OFF</a><p><a href='/status'>status</a></p>");
          });
          server.on("/status", []() { server.send(200, "application/json", statusJson()); });
          server.on("/on", []() { digitalWrite(LED_PIN, HIGH); server.send(200, "text/plain", "on"); });
          server.on("/off", []() { digitalWrite(LED_PIN, LOW); server.send(200, "text/plain", "off"); });
          server.begin();
        }

        void loop() {
          server.handleClient();
        }
    """),
    "structured_project": dedent("""\
        const int LED_PIN = 23;
        const int SENSOR_PIN = 34;

        struct DeviceState {
          bool ledOn;
          int sensorValue;
          unsigned long uptimeSeconds;
        };

        DeviceState state;

        void setupHardware() {
          pinMode(LED_PIN, OUTPUT);
          Serial.begin(115200);
        }

        void readInputs() {
          state.sensorValue = analogRead(SENSOR_PIN);
          state.uptimeSeconds = millis() / 1000;
        }

        void updateOutputs() {
          state.ledOn = state.sensorValue > 2500;
          digitalWrite(LED_PIN, state.ledOn);
        }

        void printState() {
          Serial.printf("adc=%d led=%s uptime=%lu\\n",
            state.sensorValue,
            state.ledOn ? "on" : "off",
            state.uptimeSeconds);
        }

        void setup() {
          setupHardware();
        }

        void loop() {
          readInputs();
          updateOutputs();
          printState();
          delay(500);
        }
    """),
    "millis_scheduler": dedent("""\
        const int LED_PIN = 23;
        const int BUTTON_PIN = 27;
        unsigned long lastLedTick = 0;
        unsigned long lastLogTick = 0;
        bool ledState = false;

        void setup() {
          Serial.begin(115200);
          pinMode(LED_PIN, OUTPUT);
          pinMode(BUTTON_PIN, INPUT_PULLUP);
        }

        void loop() {
          unsigned long now = millis();

          if (now - lastLedTick >= 500) {
            lastLedTick = now;
            ledState = !ledState;
            digitalWrite(LED_PIN, ledState);
          }

          if (now - lastLogTick >= 1000) {
            lastLogTick = now;
            Serial.print("button=");
            Serial.println(digitalRead(BUTTON_PIN) == LOW ? "down" : "up");
          }
        }
    """),
    "deep_sleep": dedent("""\
        #define uS_TO_S_FACTOR 1000000ULL
        #define TIME_TO_SLEEP 10

        void setup() {
          Serial.begin(115200);
          delay(1000);
          Serial.println("ESP32 woke up, doing short work...");
          esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
          Serial.println("Going to deep sleep");
          esp_deep_sleep_start();
        }

        void loop() {
        }
    """),
    "final_local_console": dedent("""\
        #include <Wire.h>
        #include <Adafruit_GFX.h>
        #include <Adafruit_SSD1306.h>

        const int LED_PIN = 23;
        const int BUTTON_PIN = 27;
        const int SENSOR_PIN = 34;
        int page = 0;
        Adafruit_SSD1306 display(128, 64, &Wire, -1);

        void setup() {
          pinMode(LED_PIN, OUTPUT);
          pinMode(BUTTON_PIN, INPUT_PULLUP);
          Wire.begin(21, 22);
          display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
          display.setTextColor(SSD1306_WHITE);
        }

        void loop() {
          static int lastButton = HIGH;
          int button = digitalRead(BUTTON_PIN);
          if (lastButton == HIGH && button == LOW) {
            page = (page + 1) % 2;
            delay(60);
          }
          lastButton = button;

          int sensor = analogRead(SENSOR_PIN);
          bool alert = sensor > 2500;
          digitalWrite(LED_PIN, alert);

          display.clearDisplay();
          display.setCursor(0, 0);
          display.setTextSize(1);
          display.println(page == 0 ? "Local Console" : "Diagnostics");
          display.print("Sensor: ");
          display.println(sensor);
          display.print("Alert: ");
          display.println(alert ? "YES" : "NO");
          display.print("Uptime: ");
          display.println(millis() / 1000);
          display.display();
          delay(120);
        }
    """),
    "final_web_console": dedent("""\
        #include <WiFi.h>
        #include <WebServer.h>

        const char* SSID = "your_wifi_name";
        const char* PASSWORD = "your_wifi_password";
        const int LED_PIN = 23;
        const int SENSOR_PIN = 34;
        bool manualLed = false;
        WebServer server(80);

        String jsonStatus() {
          return String("{\\"sensor\\":") + analogRead(SENSOR_PIN) +
                 ",\\"manualLed\\":" + (manualLed ? "true" : "false") +
                 ",\\"uptime\\":" + (millis() / 1000) + "}";
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
    """),
}


def md_link(name):
    return f"[{name}]({LINKS[name]})"


def day_filename(index, title):
    slug = [
        "认识ESP32与硬件编程全景",
        "开发环境与第一个Blink",
        "面包板电阻LED安全接线",
        "GPIO数字输出流水灯",
        "按键输入与防抖",
        "串口监视器调试",
        "第一周可调闪灯控制器",
        "PWM呼吸灯",
        "ADC电位器模拟量",
        "常见传感器认知",
        "I2C总线扫描",
        "OLED显示仪表盘",
        "SPI高速外设认知",
        "蜂鸣器继电器执行器",
        "第二周桌面环境监测器",
        "WiFi联网入门",
        "HTTP客户端请求",
        "WebServer手机控制LED",
        "JSON设备状态",
        "MQTT发布订阅",
        "BLE近场通信",
        "数据上云与仪表盘",
        "第三周联网控制系统",
        "代码结构与可维护",
        "millis非阻塞程序",
        "低功耗与深度睡眠",
        "硬件故障排查",
        "行业应用认知",
        "综合项目设计",
        "综合项目实现联网复盘",
    ][index - 1]
    return f"day{index:02d}-{slug}.md"


def clean_markdown(text):
    lines = []
    for line in text.splitlines():
        while line.startswith("        "):
            line = line[8:]
        lines.append(line)
    return "\n".join(lines).strip() + "\n"


def make_day(index, day):
    parts = "\n".join(f"- `{part}`：{part_description(part)}" for part in day["parts"])
    concepts = "\n".join(f"- **{concept}**：{concept_description(concept)}" for concept in day["concepts"])
    links = "\n".join(f"- {md_link(name)}" for name in day["links"])
    code = ""
    if day["code"]:
        code = f"""
## 参考 Demo

> 引脚可按你的开发板调整。ESP32 常用安全输出脚可优先选择 GPIO 18、19、21、22、23、25、26、27；ADC 输入可优先选择 GPIO 34、35、36、39。

```cpp
{CODE_SNIPPETS[day["code"]].rstrip()}
```
"""
    else:
        code = """
## 今日无需完整代码

今天以认知、设计、接线图、资料阅读或方案整理为主。建议仍然打开串口、检查开发板连接，并把今天的结论写进学习笔记。
"""

    return clean_markdown(dedent(f"""\
        # Day {index:02d}：{day["title"]}

        ## 今日目标

        {day["goal"]}

        ## 今天你会真正理解什么

        {day["focus"]}

        ## 元件认知

        {parts}

        ## 核心概念

        {concepts}

        ## 实操项目

        **项目名称：** {day["project"]}

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

        {code}

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

        {links}
    """))


def part_description(part):
    table = {
        "ESP32 开发板": "核心控制器，负责运行程序、读取输入、控制输出、连接 Wi-Fi/BLE。",
        "USB 数据线": "用于供电、烧录程序和串口调试；很多充电线不能传数据。",
        "面包板": "免焊接实验平台，适合快速搭建电路；内部孔位按行和电源轨连通。",
        "杜邦线": "连接开发板和元件的导线，分公对公、公对母、母对母。",
        "电阻": "限制电流、分压或上拉下拉；LED 串联电阻是入门必会安全动作。",
        "LED": "最基础输出元件，用来观察 GPIO 高低电平和程序状态。",
        "按键": "最基础输入元件，把人的动作转换为 GPIO 电平变化。",
        "OLED 屏": "小型显示输出，常用 I2C 接口，适合显示状态、数值和菜单。",
        "220Ω 电阻": "常用于 LED 限流，保护 LED 和 GPIO。",
        "220Ω/330Ω 电阻": "LED 限流常用阻值，阻值越大通常越暗但更安全。",
        "3 个 LED": "用于练习多路输出、流水灯和状态显示。",
        "3 个电阻": "每个 LED 独立串联一个限流电阻。",
        "轻触开关": "常见按键元件，按下时改变电路连接状态。",
        "电位器": "可变电阻，常用于产生可调模拟电压。",
        "DHT11/DHT22 或 SHT30": "温湿度传感器，适合入门环境监测项目。",
        "光敏电阻": "阻值随光照变化，常与固定电阻组成分压电路。",
        "超声波模块": "通过声波往返时间估算距离，常用于避障和液位测量。",
        "可选声音传感器": "检测声音强弱或阈值触发，适合报警、拍手灯等实验。",
        "可选 I2C 传感器": "和 OLED 共用 I2C 总线，帮助理解多设备同总线。",
        "0.96 寸 OLED SSD1306": "常见 128x64 单色 OLED，I2C 地址多为 0x3C。",
        "可选 SPI 屏幕/SD 卡模块": "用于理解高速外设和片选机制。",
        "有源蜂鸣器": "通电即可响，适合提示音；无源蜂鸣器需要 PWM 或方波驱动。",
        "可选继电器模块": "用低压控制高压或大电流设备，必须注意隔离和安全。",
        "已有项目代码": "前几天积累的代码，用来重构和提升可维护性。",
        "万用表可选": "用于测量电压、连通性和电源问题，是硬件排查利器。",
        "所有常用模块": "复盘和排查时作为测试样本，逐个验证接线、供电和功能。",
        "已有元件清单": "把手头硬件映射到真实行业功能，训练方案设计能力。",
        "所有项目": "30 天内完成的代码、接线图、照片和笔记，是作品集基础。",
        "笔记": "记录踩坑、参数、接线和复盘，形成自己的硬件知识库。",
        "代码": "整理成可复用 demo，后续做项目时直接调用。",
        "照片": "拍下接线和运行效果，方便复盘、展示和排查。",
    }
    return table.get(part, "本阶段使用的模块或材料，重点关注供电、接口、电平和接线方向。")


def concept_description(concept):
    table = {
        "单片机是什么": "把 CPU、内存、外设接口集成在一颗芯片里，专门控制具体设备。",
        "GPIO": "通用输入输出引脚，可读取高低电平，也可输出高低电平。",
        "3.3V 与 5V": "ESP32 GPIO 通常是 3.3V 电平，5V 可能损坏芯片输入脚。",
        "面包板内部连通方式": "中间区域通常每 5 个孔横向连通，电源轨纵向连通但可能中断。",
        "输入与输出": "输入是感知外界，输出是影响外界；硬件项目通常由两者组合成闭环。",
        "固件上传": "把编译后的程序写入 ESP32 Flash，让芯片复位后运行新逻辑。",
        "串口端口": "电脑与 ESP32 通信的通道，用于烧录和日志输出。",
        "setup 与 loop": "`setup()` 启动时运行一次，`loop()` 反复运行。",
        "数字输出": "让 GPIO 输出 HIGH 或 LOW，用来控制 LED、继电器、蜂鸣器等。",
        "限流电阻": "限制通过 LED 或 GPIO 的电流，避免烧坏元件。",
        "闭合回路": "电流必须从电源出发经过负载回到电源，断一点都不会工作。",
        "欧姆定律": "`V = I * R`，用来估算电流、电压和电阻关系。",
        "LED 正负极": "长脚通常为正极，短脚和扁边通常为负极。",
        "灌电流与拉电流": "GPIO 可输出电流给负载，也可让电流流入 GPIO，接法不同逻辑可能相反。",
        "短路风险": "电源正负直接连接会导致大电流，可能烧毁线材、芯片或电源。",
        "GPIO 编号": "代码里的 GPIO 号不一定等于开发板丝印 D 编号，要看板卡定义。",
        "数组控制引脚": "把多个相似引脚放进数组，便于循环控制。",
        "delay 的局限": "`delay()` 会阻塞程序，让其他输入和任务无法及时响应。",
        "简单状态机": "用变量表示当前状态，再根据输入和时间改变状态。",
        "数字输入": "读取 GPIO 当前是 HIGH 还是 LOW。",
        "INPUT_PULLUP": "启用芯片内部上拉电阻，按键通常按下接 GND，松开为 HIGH。",
        "机械抖动": "按键接触瞬间会快速跳变，多次触发，需要软件防抖。",
        "边沿触发": "只关心从松开到按下的一瞬间，而不是一直按住的状态。",
        "按钮状态机": "记录上一次和当前按钮状态，判断是否发生有效按下。",
        "串口波特率": "串口通信速度，代码和监视器必须一致，例如 115200。",
        "日志级别": "按重要程度输出信息，例如 info、warning、error。",
        "变量打印": "把程序内部变量输出出来，帮助理解运行状态。",
        "调试闭环": "提出假设、加日志、运行观察、缩小问题范围。",
        "需求拆解": "把大目标拆成可验证的小功能。",
        "接线表": "记录每个模块的 VCC、GND、信号脚连接到哪个 ESP32 引脚。",
        "测试清单": "列出必须验证的现象，防止漏测。",
        "项目复盘": "总结成功、失败、原因和下一步改进。",
        "PWM": "用高速开关模拟不同强度的输出。",
        "占空比": "一个周期内高电平所占比例，影响 LED 亮度或电机速度。",
        "频率": "PWM 每秒重复次数，频率不合适可能闪烁或啸叫。",
        "LEDC": "ESP32 的 LED PWM 控制器，Arduino 中常用 `ledcWrite`。",
        "模拟效果": "用数字开关产生人眼或设备感受到的连续变化。",
        "ADC": "模数转换器，把模拟电压转换成数字值。",
        "模拟输入": "连续变化的电压信号，例如电位器、光敏分压。",
        "采样": "在某个时刻读取模拟值，连续采样可观察变化趋势。",
        "分辨率": "ADC 数字精细程度，ESP32 Arduino 常见范围 0-4095。",
        "电压分压": "用电阻组合把电压按比例转换，常用于传感器读取。",
        "数字传感器": "直接通过协议输出数据，例如 I2C、单总线、UART。",
        "模拟传感器": "输出电压变化，需要 ADC 读取。",
        "校准": "把原始读数和真实物理量对应起来。",
        "采样周期": "两次读取之间的时间间隔，太快可能噪声大或传感器来不及更新。",
        "数据手册": "元件最权威说明，包含电气参数、时序、引脚和限制。",
        "I2C": "两线同步串行总线，适合连接多个中低速外设。",
        "SDA/SCL": "SDA 传数据，SCL 提供时钟。",
        "设备地址": "I2C 总线上每个设备的编号，用于区分通信对象。",
        "总线扫描": "逐个地址尝试通信，找出已连接的 I2C 设备。",
        "上拉": "用电阻把信号默认拉到高电平，I2C 总线常需要上拉。",
        "显示缓冲区": "先在内存中画好内容，再刷新到屏幕。",
        "像素坐标": "屏幕上每个点的位置，例如 128x64 OLED 的 x/y 坐标。",
        "字体": "字符显示的像素形状和大小。",
        "刷新": "把缓冲区内容发送到屏幕显示。",
        "I2C 地址": "OLED 常见地址是 0x3C，错误地址会导致无显示。",
        "SPI": "高速同步串行总线，常用于屏幕、SD 卡和射频模块。",
        "片选 CS": "选择当前和哪个 SPI 设备通信。",
        "全双工": "MOSI 发送、MISO 接收，可同时传输。",
        "总线速度": "SPI 通常比 I2C 更快，但线更多。",
        "I2C vs SPI": "I2C 省线多设备方便，SPI 速度快适合大数据量。",
        "执行器": "能对外界产生动作的元件，例如灯、蜂鸣器、继电器、电机。",
        "驱动能力": "GPIO 能提供的电流有限，不能直接驱动大负载。",
        "晶体管": "用小电流控制大电流，常作为驱动开关。",
        "继电器隔离": "用电磁方式控制另一侧电路，适合隔离高低压。",
        "反向电动势": "线圈断电时可能产生高压尖峰，需要二极管等保护。",
        "数据采集": "周期性读取传感器并转换成可用数据。",
        "显示刷新": "屏幕不必每毫秒刷新，合理周期可减少闪烁和阻塞。",
        "页面切换": "用按键或状态变量切换显示内容。",
        "模块化函数": "把读取、显示、控制拆成函数，降低复杂度。",
        "Wi-Fi STA 模式": "ESP32 作为客户端连接路由器。",
        "IP 地址": "设备在网络中的地址。",
        "网关": "局域网访问外部网络的出口。",
        "DNS": "把域名转换成 IP 地址的服务。",
        "重连": "网络掉线后自动重新连接。",
        "HTTP GET": "向服务器请求资源的常见方法。",
        "状态码": "HTTP 响应结果，例如 200 成功、404 未找到。",
        "JSON": "常见结构化数据格式，适合设备状态和接口数据。",
        "超时": "网络请求不能无限等待，需要设置失败边界。",
        "网络错误": "包括连不上、DNS 失败、服务器无响应、响应格式错误等。",
        "Web Server": "ESP32 自己提供网页或接口，让浏览器访问。",
        "路由": "不同 URL 对应不同处理函数。",
        "HTML": "网页内容格式。",
        "局域网访问": "手机和 ESP32 在同一 Wi-Fi 下，通过 IP 访问。",
        "请求处理": "收到浏览器请求后执行控制逻辑并返回响应。",
        "键值对": "JSON 中用名称和值表示数据。",
        "设备状态": "设备当前传感器值、输出状态、运行时间和错误信息。",
        "序列化": "把内存中的数据结构转换成字符串发送或保存。",
        "ArduinoJson": "Arduino 生态常用 JSON 库。",
        "MQTT": "轻量消息协议，常用于物联网设备通信。",
        "Broker": "MQTT 消息中转服务器。",
        "Topic": "消息主题，用于组织发布和订阅。",
        "QoS": "消息投递质量等级。",
        "保活": "客户端周期性维持连接，避免被服务器断开。",
        "BLE": "低功耗蓝牙，适合近距离低功耗通信。",
        "GATT": "BLE 数据组织模型。",
        "Service": "一组相关能力，例如电池服务、传感器服务。",
        "Characteristic": "具体可读写的数据项。",
        "UUID": "服务或特征值的唯一标识。",
        "云平台": "接收、存储、展示和控制设备的平台。",
        "时序数据": "随时间变化的传感器数据。",
        "设备 ID": "云端识别设备的唯一编号。",
        "Token": "设备访问云服务的凭证。",
        "仪表盘": "可视化设备数据和状态的界面。",
        "设备状态机": "用明确状态管理设备当前行为和转换条件。",
        "远程控制": "通过网络从手机、网页或云平台控制设备。",
        "本地显示": "设备无需电脑也能显示关键信息。",
        "错误恢复": "网络断开、传感器失败时自动重试或降级。",
        "模块化": "把系统拆成独立、清晰、可复用部分。",
        "配置集中": "Wi-Fi、引脚、阈值集中定义，方便修改。",
        "函数边界": "每个函数只做一类事情，输入输出清楚。",
        "命名": "变量和函数名表达真实含义。",
        "可读性": "未来的你能快速理解代码意图。",
        "非阻塞": "程序不长时间停住，能同时响应多个事件。",
        "任务周期": "不同任务按不同间隔运行。",
        "millis 溢出": "`millis()` 会在很久后回绕，用减法判断时间更稳。",
        "调度": "安排各任务何时运行。",
        "响应性": "设备对按键、网络和传感器变化的反应速度。",
        "Deep Sleep": "ESP32 深度睡眠模式，大幅降低功耗。",
        "唤醒": "定时器、按键或外部信号让芯片恢复运行。",
        "功耗": "设备消耗的电流和能量。",
        "电池容量": "电池能提供的能量，常以 mAh 标示。",
        "采样间隔": "低功耗设备醒来采样的周期。",
        "分层排查": "从电源、接线、最小代码、库、网络逐层定位。",
        "最小系统": "只保留能验证问题的最少元件和代码。",
        "电源检查": "确认电压、电流能力、GND、接触可靠。",
        "串口日志": "通过日志观察内部状态。",
        "替换法": "替换线材、模块、引脚或代码来缩小故障范围。",
        "边缘设备": "部署在现场、靠近数据源的智能设备。",
        "传感采集": "从物理世界收集温度、湿度、光照、距离等信息。",
        "OTA": "无线升级固件。",
        "安全": "包括凭证保护、通信加密、设备权限和物理安全。",
        "量产约束": "成本、可靠性、认证、维护、供应链等真实产品限制。",
        "项目设计文档": "在实现前说明目标、模块、接口、风险和验收标准。",
        "验收标准": "判断项目完成的可观察条件。",
        "风险清单": "提前列出可能失败的技术点。",
        "迭代计划": "先做最小可用版本，再逐步增强。",
        "接线实现": "根据设计文档把每个模块连接到指定引脚。",
        "分模块调试": "一个模块一个模块确认，最后再组合。",
        "本地闭环": "输入、处理、输出都在设备本地完成。",
        "验收测试": "按清单逐项验证功能是否达到要求。",
        "HTTP API": "用 URL 返回机器可读的数据或执行控制命令。",
        "网页控制": "浏览器通过按钮或链接发送控制请求。",
        "状态同步": "本地状态、网页状态、实际硬件输出保持一致。",
        "作品集": "整理能展示学习成果的代码、照片、文档和视频。",
        "技术路线": "后续继续学习的方向和顺序。",
        "ESP-IDF": "Espressif 官方开发框架，比 Arduino 更底层、更工程化。",
        "FreeRTOS": "ESP32 常用实时操作系统，支持多任务调度。",
        "PCB": "把面包板电路变成可生产的电路板。",
    }
    return table.get(concept, "硬件编程中的重要概念，建议结合今天实验观察它在真实设备里的表现。")


def write_readme():
    rows = []
    for i, day in enumerate(DAYS, 1):
        filename = day_filename(i, day["title"])
        rows.append(f"| Day {i:02d} | [{day['title']}](days/{filename}) | {day['goal']} |")
    day_rows = "\n".join(rows)
    link_rows = "\n".join(f"- {md_link(name)}" for name in LINKS)
    content = clean_markdown(dedent(f"""\
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
        {day_rows}

        ## 总结报告

        - [00-学习总报告.md](00-学习总报告.md)

        ## 常用资料链接

        {link_rows}
    """))
    (ROOT / "README.md").write_text(content, encoding="utf-8")


def write_report():
    weekly = [
        ("第 1 周：硬件编程入门与 GPIO 基础", "你会认识 ESP32、面包板、LED、按键、电阻和串口调试，完成第一个能交互的闪灯控制器。"),
        ("第 2 周：外设、总线与小型仪表盘", "你会使用 PWM、ADC、I2C、OLED、蜂鸣器和传感器，完成桌面环境监测器。"),
        ("第 3 周：联网能力与物联网通信", "你会连接 Wi-Fi，使用 HTTP、Web Server、JSON、MQTT 和 BLE，完成手机控制与数据上报系统。"),
        ("第 4 周：工程化、低功耗、排查与综合项目", "你会学习非阻塞程序、低功耗、故障排查、行业应用，并完成一个桌面物联网控制台。"),
    ]
    weekly_text = "\n\n".join(f"### {title}\n\n{body}" for title, body in weekly)
    links = "\n".join(f"- {md_link(name)}" for name in LINKS)
    content = clean_markdown(dedent(f"""\
        # 30天轻松搞定ESP32

        ## 30 天硬件编程入门学习计划：学习总报告

        ## 一、学习定位

        这份计划面向“已经买了 ESP32 入门开发板和基础配件，但还没有系统硬件编程经验”的学习者。目标不是让你机械复制 30 个教程，而是让你建立完整的硬件编程思维：认识元件、理解电路、会写控制程序、会读串口日志、会查资料、会排查问题、会把多个模块组合成一个小产品。

        学完 30 天后，你应该能独立完成这类项目：

        - LED、按键、蜂鸣器等基础输入输出控制。
        - OLED 小屏状态显示。
        - 电位器、温湿度、光照、距离等传感器数据采集。
        - 手机网页控制 ESP32。
        - MQTT 或 HTTP 方式上传设备状态。
        - 一个具备输入、显示、联网、告警的桌面物联网设备原型。

        ## 二、建议硬件清单

        ### 必备

        - ESP32 DevKit 类开发板 1 块。
        - USB 数据线 1 根，必须支持数据传输。
        - 面包板 1 块。
        - 杜邦线若干，建议公对公、公对母都准备。
        - LED 若干，颜色不限。
        - 220Ω 或 330Ω 电阻若干。
        - 轻触按键若干。
        - 0.96 寸 SSD1306 OLED，I2C 接口优先。

        ### 推荐

        - 电位器 1-2 个。
        - 有源蜂鸣器 1 个。
        - 温湿度传感器，例如 DHT22、SHT30 或 AHT20。
        - 光敏电阻或模拟光照模块。
        - 超声波测距模块。
        - 万用表 1 个，用于排查电源和连通性。

        ## 三、四阶段路线

        {weekly_text}

        ## 四、学习方法

        1. **先理解再接线**：每次接模块前先确认 VCC、GND、信号脚、电平要求。
        2. **先最小后组合**：单独点亮 LED、单独读取按键、单独驱动 OLED，最后再组合。
        3. **保留串口日志**：串口是嵌入式调试的主窗口，任何复杂项目都应输出关键状态。
        4. **每天只改一个变量**：例如引脚、延时、阈值、显示内容。每次只改一个，才能知道变化来自哪里。
        5. **用表格管理接线**：模块、VCC、GND、信号脚、ESP32 GPIO、备注，这张表能救你很多次。
        6. **形成排查顺序**：电源 -> GND -> 引脚 -> 最小代码 -> 库版本 -> 协议地址 -> 网络。

        ## 五、ESP32 引脚使用建议

        - 常用输出：GPIO 18、19、21、22、23、25、26、27。
        - 常用 ADC 输入：GPIO 34、35、36、39，这些多为输入专用。
        - I2C 默认常用：SDA = GPIO 21，SCL = GPIO 22。
        - 避免初学时随意使用启动相关引脚，例如 GPIO 0、2、12、15，除非你理解启动模式影响。
        - ESP32 GPIO 是 3.3V 逻辑，不能把 5V 信号直接输入 GPIO。

        ## 六、业内应用视角

        ESP32 在行业里常见于：

        - **智能家居**：灯控、窗帘、环境监测、门磁、红外网关。
        - **农业物联网**：土壤湿度、温湿度、灌溉控制、远程告警。
        - **工业采集**：设备状态采集、无线传感节点、边缘网关原型。
        - **教育与创客**：机器人、交互装置、实验教学、快速原型。
        - **可穿戴与低功耗设备**：BLE 通信、周期采样、睡眠唤醒。

        真正进入工程实践后，你还需要继续学习：电源设计、保护电路、PCB、外壳结构、OTA、日志系统、设备安全、批量生产测试。

        ## 七、一个月后的能力检查

        你可以用下面的问题检查自己：

        - 能否不用教程解释 LED 为什么要串电阻？
        - 能否根据 OLED 不亮的问题，列出 5 个排查方向？
        - 能否写出按键防抖逻辑，并说明为什么会抖？
        - 能否不用 `delay()` 同时处理 LED 闪烁、按键和屏幕刷新？
        - 能否让手机浏览器访问 ESP32 并控制一个 GPIO？
        - 能否把传感器值组织成 JSON？
        - 能否说明 I2C 和 SPI 的区别？
        - 能否设计一个从传感器到云平台的数据链路？

        ## 八、继续深入路线

        1. **Arduino ESP32 熟练阶段**：更多传感器、更多通信模块、更复杂的本地 UI。
        2. **PlatformIO 工程化阶段**：项目结构、库管理、多环境构建、版本控制。
        3. **ESP-IDF 阶段**：任务、事件循环、NVS、Wi-Fi 事件、组件化开发。
        4. **FreeRTOS 阶段**：任务、队列、信号量、定时器、并发问题。
        5. **硬件设计阶段**：原理图、PCB、电源、保护、接口、EMC 基础。
        6. **产品化阶段**：OTA、安全、日志、设备身份、云平台、量产测试。

        ## 九、精选资料

        {links}
    """))
    (ROOT / "00-学习总报告.md").write_text(content, encoding="utf-8")


def main():
    DAYS_DIR.mkdir(exist_ok=True)
    write_readme()
    write_report()
    for i, day in enumerate(DAYS, 1):
        (DAYS_DIR / day_filename(i, day["title"])).write_text(make_day(i, day), encoding="utf-8")


if __name__ == "__main__":
    main()
