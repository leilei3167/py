# 将函数作为参数传入另一个函数
def func1(c):
    r = c(5, 6)
    print(r)


def compute(x, y):
    return x + y


func1(compute)

# lambda表达式, 参数列表:函数逻辑
# 匿名函数只能有一行代码
func1(lambda x, y: x + y)


# 内部函数使用外部函数的变量,就是闭包


def counter(count=0):
    # 外部函数的变量以及参数
    def inner():
        nonlocal count  # 使用nonlocal关键字声明变量表名是外部函数的变量
        count += 1
        return count

    return inner


c = counter(100)  # c这个函数就是闭包,保留了对100的引用(这一部分会一直占用内存),每次调用c都会对100进行操作
print(c())
print(c())
print(c())
print(c())

c2 = counter(10)
print(c2())
print(c2())
print(c2())


# 装饰器


def wrapper(func):
    def inner():
        print("正在验证权限...")
        func()
        print("执行完毕...")

    return inner


@wrapper  # @wrapper等价于f = wrapper(sleep)
def sleep():
    import random
    import time

    print("睡觉中...")
    time.sleep(random.randint(1, 3))


origin_sleep = sleep
sleep()  # 因为有装饰器注解,相当于执行了wrapper(sleep)()
