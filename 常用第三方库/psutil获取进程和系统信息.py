import psutil

print(psutil.cpu_count())  # CPU逻辑数量
print(psutil.cpu_count(logical=False))  # CPU物理核心数量


print(psutil.net_if_addrs())  # 获取网络接口信息
