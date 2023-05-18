print("\n参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数")


def f1(a, b, c=0, *args, namedAeg="I am name keyword arg", **kw):
    print("必须参数(位置参数): ", a, b)
    print("默认参数: ", c)
    print("可变参数:", args)
    print("命名关键字参数(带默认值): ", namedAeg)
    print("关键字参数: ", kw)


f1("lei", 18, 1000, ("helop", 1), job="pig", city="chengdu ")

# 还可以这么搞: 传入的参数个数必须和定义的参数个数一致
args = ("lei", 18, 1000, ("helop", 1))
kt = {"job": "pig", "city": "chengdu "}
f1(*args, **kt)


def add_end(L=[]):
    L.append("END")
    return L


print(add_end())
print(add_end())
print(add_end())  # ['END', 'END', 'END']
# 函数在定义时,参数的默认值就被计算出来了,每次调用函数都会改变[]的值,因此默认参数必须指向不变对象


def add_end2(L=None):  # 设默认值为None,在函数内部判断L是否为None,如果是,则创建一个空列表
    if L is None:
        L = []
    L.append("END")
    return L


print(add_end2())
print(add_end2())
print(add_end2())


print("\n可变参数使用*定义,在函数内部,参数接收到的是一个tuple")


def calc(name, *nums):
    res = 0
    for n in nums:
        res = res + n * n

    print(f"name:{name} is calling!")
    return res


print(calc("zhangsan", 1, 2, 3, 4, 5))
print(calc("lisi", 1, 2, 3, 4, 5))

# 如果实参已经是一个list或者tuple,可以在list或tuple前面加一个*号,把list或tuple的元素变成可变参数传进去
toAdd = (1, 2, 3, 100)
# print(calc(name="wangwu", *toAdd))  # 报错,因为同时使用了关键字参数和位置参数
print(calc("wangwu", *toAdd))


print("\n关键字参数使用**定义,在函数内部,参数接收到的是一个dict")  # 允许传入多个带参数名的参数


def person(name, age, **kw):
    print(type(kw))
    print("name:", name, "age:", age, "other:", kw)


person("lei", 19)
person("lei1", 10, city="beijing", job="engineer")
person("lei12", 29, gender="男", city="beijing", job="fucker")

extra = {"ae": 10078, "vcji": 109}
person("pig", 19, **extra)


# 限制关键字参数的名称,使用星号来分隔,星号之后的就是关键字参数的名称
print("\n限制关键字参数的名称")


def person(name, age, *, city, job):
    print(name, age, city, job)


person("lei1", 10, city="beijing", job="engineer")
# person("lei112", 1, city="chengdu", job="fuck", salary=100)# 报错,多余的参数


# 当已经有可变参数时,再引入命名关键字参数时不需要星号分隔
def person(name, age, *args, city="chengdu", job):
    print(name, age, args, city, job)


person("lei", 12, (100, "fu"), job="pug")  # 因为city有默认值,所以不传不影响
