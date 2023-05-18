import time
from datetime import datetime
from datetime import timedelta


now = datetime.now()
print(now, type(now))  # 类型是datetime.datetime

three_days = timedelta(days=3)
after_three_days = now + three_days  # 只有日期类才能加减timedelta
print(after_three_days)

before_three_days = now - three_days
print(before_three_days)


# 一个小时
one_hour = timedelta(hours=1)
after_one_hour = now + one_hour
print(after_one_hour)


# 时间对象必须转化为字符串才能写入文件,或者传输
ago = datetime.now() - timedelta(days=67)
print(ago, type(ago))


# 时间对象转化为字符串 使用strftime
print("\n")
a = ago.strftime("%Y-%m-%d %H:%M:%S")
print(a)
print(ago.strftime("%y-%m-%d %h:%M:%S"))
print(ago.strftime("%Y%m%d_%H%M%S"))

# 如果要计算时间,需要先把字符串转化为时间对象 strptime
print("\n")
obj = datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
print(obj, type(obj))
new_obj = obj + timedelta(days=3)
print(new_obj)

# 转化为时间戳
print("\n")
now = datetime.now()
now_tp = now.timestamp()
print(now_tp, type(now_tp))


# 时间戳转化为时间对象
d = datetime.fromtimestamp(now_tp)
print(d, type(d))
