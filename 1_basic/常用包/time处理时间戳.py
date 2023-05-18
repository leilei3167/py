# python中的时间戳是一个浮点数，单位是秒，从1970年1月1日0时0分0秒开始算起
import random
import time

now = time.time()
print(now, type(now))

# 获取本地时间函数,也可以将时间戳转换为本地时间
t = time.localtime(now)
print(t, type(t))

# 毫秒时间戳
print(time.time() * 1000)


# sleep()函数
print("随机睡眠0-3秒")
time.sleep(random.randint(0, 3))


# 时间戳的strftime()函数,必须传入时间对象

t_str = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(t_str, type(t_str))
