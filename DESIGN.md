功能目标：为 zhipu-loopforge-joint-test-1 冒烟测试提供设计基线，保持 hello.py 打印 "hello from managed agent" 的既有行为，作为后续实现与测试阶段的统一依据。
接口说明：hello.py 为命令行入口，执行 `python3 hello.py` 不接收参数、不返回值，向 stdout 输出一行 "hello from managed agent"，进程退出码为 0。
