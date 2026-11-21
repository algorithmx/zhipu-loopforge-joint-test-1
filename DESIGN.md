功能目标：提供零依赖的问候脚本 hello.py，执行后在 stdout 输出一行 "hello from managed agent"，用于 LoopForge 联合冒烟测试验证端到端交付链路。
接口说明：命令行入口 `python3 hello.py`（无参数、无第三方依赖），stdout 输出一行文本 "hello from managed agent"，退出码 0 表示成功，非 0 表示失败。
