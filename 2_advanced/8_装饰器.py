# 函数也是对象,可以获取对象的属性等
import functools
import time
from datetime import datetime


def current():
    return datetime.now()


print(current())

print(current.__name__)  # 函数名

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改current()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator


# 定义一个装饰器,本质上就是一个函数,它可以接收一个函数作为参数,并返回一个函数
def log(fn):
    def wrapper(*args, **kw):
        print("call %s(): " % fn.__name__)
        return fn(*args, **kw)

    return wrapper


@log
def current1():
    return datetime.now()


# 相当于执行了current1 = log(current1)
print(current1())


print("\n带参数的装饰器需额外再包裹一层,注意使用functools.wraps将原始函数属性复制到包裹函数中")


def log1(text):
    def deco(func):
        # 将原始函数的__name__等属性复制到wrapper()函数中,否则有些依赖函数签名的代码执行就会出错
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return deco


@log1("execute!!")
def current2():
    return datetime.now()


# 相当于执行了current2 = log1("execute!!")(current2)
n = current2
print(n.__name__)  # 注意,这里的n是wrapper函数,所以打印出来的是wrapper
# 因为返回的那个wrapper()函数名字就是wrapper，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
# 需要使用functools.wraps

print("\n一个打印执行时间的装饰器")


def printTime(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t = datetime.now()
        try:
            return fn(*args, **kwargs)
        finally:
            print("执行时间:", datetime.now() - t)

    return wrapper


@printTime
def doSth():
    for i in range(0, 10):
        print(i)
        time.sleep(1)
    raise Exception("抛出一个异常")


doSth()
