# DESIGN.md

功能目标：提供一个最小可运行的 Python 入口（hello.py），打印问候语以验证流水线各阶段（设计、实现、测试）的协同与远程交付链路。

接口说明：`hello.py` 为无参数命令行脚本，通过 `python3 hello.py` 运行，向 stdout 输出单行字符串 `hello from managed agent`，无返回值、无外部依赖。
