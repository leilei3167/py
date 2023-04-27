# 1.函数基本定义,参数可以省略,返回值可以省略
def my_func(arg):
    a = 100
    return arg * a


# 调用
print(my_func(10))


# 2. 函数的参数,可定义任意多个参数,参数可以有默认值

def add(x, y):
    return x + y


print(add(1, 2))
print(add(101, 200))


# 没有指定return的函数,默认返回None(也可以显式的返回None),if判断中None会被当做False
def returnNone():
    print("没有return的默认返回None")


print(type(returnNone()))


# 函数注释
def add1(x, y):
    """
    add1接收两个参数,返回两个参数的和
    :param x: 第一个参数
    :param y: 第二个参数
    :return: 两个参数的和
    """
    return x + y


# 函数默认值
def greet(name, message="Hello", times=1):
    for _ in range(times):
        print(f"{message}, {name}!")


# greet()  # 报错,因为name没有指定默认值,所以是必须参数
greet("John")  # 输出: Hello, John!
greet("John", "Hi")  # 输出: Hi, John!
greet("John", "Hi", 3)  # 输出: Hi, John! Hi, John! Hi, John!

# 局部变量和全局变量
# 局部变量:在函数内部定义的变量,只能在函数内部使用
# 全局变量:在函数外部定义的变量,可以在函数内部使用,但是不能在函数内部修改全局变量的值

all = 1


def use_add():
    all = 100
    print("函数内部修改全局变量", all)


use_add()
print("函数外部使用全局变量,不会被函数内部改变", all)


def use_add1():
    global all  # 使用global声明变量,该内部变量就会和全局变量关联
    all = 100
    print("函数内部使用global之后修改全局变量", all)


use_add1()
print("函数内部使用global声明变量,该内部变量就会和全局变量关联", all)
