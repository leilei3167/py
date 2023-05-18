import platform
import sys

# modules 返回已经加载的所有模块

m = sys.modules
print(m)


# path
p = sys.path
print(p)

# exit,退出程序,sys.exit(0)表示正常退出,sys.exit(1)表示异常退出
# sys.exit(0)


# platform 返回当前操作系统的平台
os = sys.platform
arch = platform.machine()
# print(f"You are running on {os}_{arch}")
# version 返回当前python版本
# print("python 版本:", sys.version)

# argv 返回命令行参数列表,第一个元素是程序本身路径,常用于编写命令行工具
print("命令行参数列表:", sys.argv)  # argv[0]是程序本身路径


command = sys.argv[1]
if command == "version":
    print("python 版本:", sys.version)
elif command == "platform":
    print(f"You are running on {os}_{arch}")
else:
    print("Unknown command")
