# 高阶函数就是以其他函数作为参数的函数
# 比较有代表性的就是map和reduce函数
from collections.abc import Iterable, Iterator

print("map函数")


def f(x):
    return x * x


l = map(
    f, [1, 2, 3, 4, 5]
)  # 函数接收两个参数，一个是函数，一个是Iterable(不仅仅是列表,字典等,是Iterable都可以)，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

print(
    type(l), isinstance(l, Iterable), isinstance(l, Iterator), l
)  # 返回的是一个新的Iterator,是一个惰性序列,只有在取值的时候才会计算
print(list(l))  # 直接使用list()函数计算出所有的值并返回一个list


print("\nreduce")


def add(x, y):
    return x * 10 + y


l1 = [1, 2, 3, 4, 5]

from functools import reduce

l2 = reduce(
    add, l1
)  # reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数,计算时序列中的前两个元素先计算出一个结果,再与第三个元素计算,以此类推
print(type(l2), isinstance(l2, Iterable), isinstance(l2, Iterator), l2)


# reduce搭配map使用


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }[s]


print(reduce(fn, map(char2num, "13579")))
# map返回的是一个Iterator,reduce函数会自动调用next()函数,所以不需要再调用next()函数
# map将遍历字符串,将每个遍历的元素传入char2num函数,将返回的结果作为新的Iterator,reduce函数将新的Iterator中的元素依次传入fn函数,计算出最终的结果

# 配合lambda表达式简化

print(reduce(lambda x, y: x * 10 + y, map(char2num, "13579")))


def normalize(name):
    tmp = name.lower()  # 全部小写
    # 将首字母大写
    return tmp[0].upper() + tmp[1:]


L1 = ["adam", "LISA", "barT"]
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x * y, L)


print("3 * 5 * 7 * 9 =", prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print("测试成功!")
else:
    print("测试失败!")


# 字符串转浮点数
def str2float(s):
    s1 = s.split(".", maxsplit=2)[0]  # 整数部分
    s2 = s.split(".", maxsplit=2)[1]  # 小数部分,小数后几位,用于除成小数
    return reduce(lambda x, y: x * 10 + y, map(char2num, s1)) + reduce(
        lambda x, y: x * 10 + y, map(char2num, s2)
    ) / (10 ** len(s2))


print("str2float('123.456') =", str2float("123.456"))
if abs(str2float("123.456") - 123.456) < 0.00001:
    print("测试成功!")
else:
    print("测试失败!")
