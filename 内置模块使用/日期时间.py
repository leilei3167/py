from datetime import datetime

now = datetime.now()
print("now()返回的是一个datetime类的实例,由类的__new__创建: ", type(now), now)
print()

print("日期转时间戳:")

# 根据年月日创建时间对象
dt = datetime(2015, 4, 19, 12, 20)
print("dt 时间戳,注意python中时间戳是浮点数: ", type(dt.timestamp()), dt.timestamp())

print("时间戳转日期需要指定时区: ")
now_dt = now.timestamp()
local = datetime.fromtimestamp(now_dt)
print("fromtimestamp将时间戳直接转换为本地时间: ", local)

utc = datetime.utcfromtimestamp(now_dt)
print("utcfromtimestamp将时间戳直接转换为UTC时间: ", utc)
print()

print("字符串转datetime对象: ")
t = "2012-12-12 12:12:12"
t1 = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")  # str parse time
print("strptime转换的时间对象是没有时区信息的: ", t1)
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print("时间对象转换为字符串: ", now.strftime("%A, %b %d %H:%M"))


print()
print("时间的运算,需要导入timedelta类: ")
from datetime import timedelta

n = datetime.now()
after10d = n + timedelta(days=10)
print("10天后的时间: ", after10d)
after10h = n + timedelta(hours=10)
print("10小时后的时间: ", after10h)
before1d2h3m = n - timedelta(days=1, hours=2, minutes=3)
print("1天2小时3分钟前的时间: ", before1d2h3m)


print()
print("时区转换: ")
from datetime import timezone

# 先拿到当前的utc时间并设置时区,再转换为任意时区的时间
utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
print("utc_now: ", utc_now)

# astimezone()将转换时区为北京时间:
bj = utc_now.astimezone(timezone(timedelta(hours=8)))
print("北京时间: ", bj)
# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
#
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区
