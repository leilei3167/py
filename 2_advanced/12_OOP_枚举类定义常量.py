from enum import Enum, unique

# 直接基于Enum类来定义枚举类

Month = Enum(
    "Month",
    (
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ),
)

for name, member in Month.__members__.items():
    print(name, "=>", member, ",", member.value)  # value属性则是自动赋给成员的int常量，默认从1开始计数


print(type(Month.Jan), Month.Jan)
print(type(Month(3)), Month(3))


# 自定义枚举


# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 使用
print()
print(type(Weekday.Mon), Weekday.Mon, Weekday.Mon.value)


# Python中没有严格的常量,常量命名一般使用全部大写的方式,但是仍然可以改变常量的值


class MyConstants(Enum):
    MAX_SIZE = 100
    DEFAULT_DB_NAME = "test.db"


class ServiceStatus(Enum):
    OPEN_OLD = 1
    ON_OLD = 2
    OFF = 3
    ON = 4


print(ServiceStatus.OPEN_OLD.value)
