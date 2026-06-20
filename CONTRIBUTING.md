# 贡献指南 / Contributing

欢迎提交 ESP32 学习笔记、接线图、勘误、代码改进和更多硬件模块示例。

English contributions are welcome. Please keep beginner explanations clear and include wiring, voltage, and safety notes when adding hardware examples.

## 内容原则

- 面向初学者，解释清楚“为什么这样接”和“为什么这样写”。
- 所有接线示例必须标注 ESP32 GPIO、VCC、GND 和电平风险。
- 代码示例优先保持短小、可运行、易修改。
- 涉及 220V 市电、继电器、大电流、电池充放电时，必须加入安全提醒。

## 建议提交内容

- 修正错别字、链接失效、代码编译问题。
- 增加更多开发板型号的引脚说明。
- 增加模块示例，例如 WS2812、舵机、NTP、OTA、SD 卡、摄像头。
- 增加配套图片、接线表或视频链接。

## 本地生成文档

```bash
python3 tools/generate_course.py
```

生成器会重新写入 `README.md`、`00-学习总报告.md` 和 `days/` 下的 30 天文档。
