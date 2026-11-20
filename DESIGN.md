功能目标：作为 LoopForge × Managed Agents 联合冒烟测试项目，验证多阶段流水线（设计→实现→测试）可端到端跑通，运行问候脚本并输出预期的 "hello from managed agent" 文本。
接口说明：hello.py 为 CLI 入口，用法 `python hello.py`（无参数、退出码 0），行为是向 stdout 打印一行 "hello from managed agent"；无其他对外接口。
