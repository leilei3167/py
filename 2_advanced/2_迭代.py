# python中的for...in可以用于所有的可迭代对象，包括字符串、列表、元组、字典、集合、文件对象等,是否可迭代并不是看是否有下标,而是看是否有__iter__方法
# 其本质是通过迭代器来实现的


# 判断一个对象是否是可迭代对象

from collections.abc import Iterable

print(isinstance("abc", Iterable))  # str是否可迭代

print(isinstance(123, Iterable))
print(isinstance([1, 2, 3], Iterable))

# 如果想要对一个list进行下标循环,可以使用enumerate函数,它会将list变成索引-元素对,有了索引,可以在循环中修改list中的元素
t = [1, 2, 3, 4, 5]
for i, v in enumerate(t):
    if t[i] % 2 == 0:
        t[i] = t[i] ** 2

print(t)


def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    min = L[0]
    max = L[0]
    for v in L:
        if v < min:
            min = v
        if v > max:
            max = v
    return min, max


if findMinAndMax([]) != (None, None):
    print("测试失败!")
elif findMinAndMax([7]) != (7, 7):
    print("测试失败!")
elif findMinAndMax([7, 1]) != (1, 7):
    print("测试失败!")
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print("测试失败!")
else:
    print("测试成功!")
