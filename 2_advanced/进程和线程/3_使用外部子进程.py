# 外部子进程,比如说在py中调用cmd的命令

import subprocess

# 直接调用命令,返回命令执行结果
# r = subprocess.call(["nslookup", "www.python.org"])
r = subprocess.call(["docker", "ps", "-a"])

print("Exit code:", r)


print()
print("可以使用communicate()方法输入命令和获取命令执行结果")
p = subprocess.Popen(
    ["nslookup"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)

# 字符串前面的b代表这是一个bytes类型的字符串,不是unicode类型的字符串
out, err = p.communicate(b"set q=mx\npython.org\nexit\n")
print(out.decode("utf-8"))
print("Exit code:", p.returncode)
# 相当于先运行nslookup,然后输入set q=mx,python.org,exit,然后获取命令执行结果
