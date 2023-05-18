print("返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量")


def count():
    fs = []
    # 注意,产生的闭包函数引用的是同一个变量i,在count返回时,i已经变成了3,所以调用f()时,返回的都是9
    for i in range(1, 4):

        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

print("Go中的方法也无效")


def count2():
    fs = []
    for i in range(1, 4):
        l = i

        def f():
            return l * l

        fs.append(f)
    return fs


f4, f5, f6 = count2()
print(f4(), f5(), f6())

print("如果一定要引用循环变量怎么办？方法是再创建一个函数")


def count3():
    def f(j):
        def g():
            return j * j

        return g  # 返回g这个闭包

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)会立即执行,返回g这个闭包,所以fs中存放的是g这个闭包
    return fs


f7, f8, f9 = count3()
print(f7(), f8(), f9())

print("\n对外部变量进行赋值时,需要使用nonlocal关键字")


def count4():
    x = 0

    def add():
        # 每调用一次就会在外部变量x上累加1
        nonlocal x
        x = x + 1
        return x

    return add


c = count4()
print(c(), c(), c(), c(), c(), c())


print("\n匿名函数:lambda表达式")
a = lambda x: x * x


# 等价于:
def a1(x):
    return x * x


print(a(188))


# 匿名函数用做返回值,简化闭包
def build(x, y):
    return lambda: x * x + y * y


L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
